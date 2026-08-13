# Grocery Store Management System (Advanced)

A comprehensive grocery store point-of-sale and inventory management system with multiple implementation levels. The project progresses from a simple billing system to an advanced system featuring multi-format data support, database persistence, PDF/CSV export, and complete error handling.

## Project Overview

**Purpose:** Automate the checkout process for a grocery store, generate customer bills, manage inventory, and maintain transaction history.

**Key Features:**
- Product catalog management (JSON/CSV formats)
- Interactive customer checkout
- Automatic bill calculation with items, prices, and totals
- Discount application
- Tax (GST) calculation
- Bill export to CSV and PDF formats
- SQLite database for transaction history
- Robust error handling and data validation
- Support for multiple customers per session

**Use Cases:**
- Retail grocery store checkout counter
- Inventory tracking system
- Sales reporting and analytics
- Customer receipt generation
- Tax and discount management

## Project Structure

```
Grocery Store Management project (Advanced)/
├── src/
│   ├── grocery_intermediate.py    # Advanced implementation (production-ready)
│   ├── grocery.json               # Product catalog (JSON format)
│   ├── grocery.csv                # Product catalog (CSV format)
│   ├── customer_bill.csv          # Generated bill (CSV export)
│   ├── customer_bill.pdf          # Generated bill (PDF export)
│   └── grocery_records.db         # SQLite database (transaction history)
└── README.md                      # This file
```

## Implementation Versions

### 1. Simple Implementation (`exercise.py`) (Removed)

A basic, easy-to-understand billing system ideal for learning the fundamentals.

#### Key Components

**Global State:**
```python
grocery_items = {
    'apple': 2.99,
    'banana': 1.49,
    'milk': 3.99,
    'bread': 2.49,
}
bill = {}  # Global dictionary tracking cart items
```

**Functions:**

**`display_items()`**
- Displays all available items and their prices
- Output format: "item_name: $price"
- Called at application start

**`create_bill()`**
- Interactive loop to add items to cart
- User enters item name and quantity
- Validates item existence in catalog
- Calculates total cost per item: `cost = price × quantity`
- Stores in bill dictionary: `{item: {quantity, cost}}`
- Continues until user enters 'q' to quit
- Uses `tabulate` for formatted output

**`sort_bill()`**
- Sorts bill items alphabetically by item name
- Displays sorted bill in table format
- Columns: Item, Quantity, Unit Price, Total Cost
- Uses lambda function: `lambda x: x[0]` to sort by item name

#### Workflow

```
1. display_items()
2. create_bill()
   - Loop: add items with quantities
   - Calculate running total
3. sort_bill()
   - Display bill sorted by name
```

#### Example Session

**Catalog:**
```
apple: $2.99
banana: $1.49
milk: $3.99
bread: $2.49
```

**User Interaction:**
```
Enter item name: apple
Enter quantity: 3
[apple added: 3 × $2.99 = $8.97]

Enter item name: milk
Enter quantity: 2
[milk added: 2 × $3.99 = $7.98]

Enter item name: q
[exit loop]
```

**Output Bill (Sorted Alphabetically):**
```
┌───────┬──────────┬────────────┬─────────────┐
│ Item  │ Quantity │ Unit Price │ Total Cost  │
├───────┼──────────┼────────────┼─────────────┤
│ apple │ 3        │ $2.99      │ $8.97       │
│ milk  │ 2        │ $3.99      │ $7.98       │
└───────┴──────────┴────────────┴─────────────┘

Total cost: $16.95
```

#### Limitations

- Fixed product catalog (hardcoded)
- No discount or tax support
- No data persistence
- No export options
- Limited error handling
- Single-use (no multi-customer support)

### 2. Advanced Implementation (`src/grocery_intermediate.py`)

A production-ready system with professional features for real-world grocery store operations.

#### Key Components

**`GroceryStore` Class**

Manages product catalog with multi-format support.

**Constructor:**
```python
def __init__(self, catalog_file=None):
    self.base_path = os.path.dirname(os.path.abspath(__file__))
    self.catalog_file = catalog_file or "grocery.json"
    self.items = []
    self.load_catalog()
```

**Attributes:**
- `base_path` — Directory containing script (for relative file paths)
- `catalog_file` — Path to product catalog (JSON or CSV)
- `items` — List of product dictionaries with id, name, price

**Methods:**

**`load_catalog()`** — Multi-format file loader with error handling
- Supports JSON and CSV formats
- JSON schema: `{items: [{id, name, price}, ...]}`
- CSV schema: `id, name, price` (with header)
- Error handling:
  - `FileNotFoundError` — Catalog file missing
  - `json.JSONDecodeError` — Invalid JSON
  - `ValueError` — Unsupported format
- Graceful degradation: displays warning, continues with empty catalog

**`display_items()`** — Formatted catalog display
- Uses `tabulate` for professional table output
- Columns: ID, Item, Price (Rs.)
- Checks for empty catalog

**`get_price(item_name)`** — Case-insensitive price lookup
- Returns price if item found
- Returns `None` if item not found
- Used by Bill class during checkout

#### `Bill` Class

Manages individual customer transactions.

**Constructor:**
```python
def __init__(self, store, db_file="grocery_records.db"):
    self.store = store
    self.items = {}              # Bill items
    self.total_cost = 0.0        # After discount and tax
    self.discount = 0.0          # Absolute discount amount
    self.tax = 0.0               # Absolute tax amount
    self.db_file = db_file
    self._init_db()
```

**Attributes:**
- `store` — Reference to GroceryStore object
- `items` — Dictionary: `{item_name: {price, quantity, cost}}`
- `total_cost` — Final bill amount (after discount/tax)
- `discount` — Absolute discount in rupees
- `tax` — Absolute tax in rupees

**Methods:**

**`_init_db()`** — Database initialization
- Creates SQLite tables if not exist
- Tables:
  - `bills` — Bill metadata (date, discount, tax, total)
  - `bill_items` — Individual items per bill (foreign key relationship)
- Error handling for database errors

**`add_item(item_name, quantity)`** — Add product to bill
- Looks up price using `store.get_price()`
- Calculates cost: `cost = price × quantity`
- If item already in bill, increments quantity and cost
- Otherwise, creates new entry
- Updates running total
- Error handling: validates item exists

**`apply_discount(percent)`** — Apply percentage discount
- Parameter: discount percentage (0-100)
- Calculation: `discount_amount = (percent / 100) × total_cost`
- Subtracts from total: `total_cost -= discount_amount`
- Only applies if percent > 0

**`apply_tax(percent)`** — Apply tax (GST)
- Parameter: tax percentage (e.g., 18 for 18% GST)
- Calculation: `tax_amount = (percent / 100) × total_cost`
- Adds to total: `total_cost += tax_amount`
- Only applies if percent > 0

**`save_to_db()`** — Persist bill to SQLite database
- Inserts bill record with timestamp
- Retrieves bill_id (autoincrement)
- Inserts all items with bill_id foreign key
- Enables transaction history and reporting
- Error handling: catches SQLite errors

**`display_bill()`** — Formatted bill output
- Uses `tabulate` for professional table
- Shows items with quantities, prices, totals
- Displays discount amount applied
- Displays tax amount applied
- Shows grand total
- Error handling: checks for empty bill

**`export_csv(filename)`** — Export bill to CSV
- Creates CSV file with headers
- Rows: Item, Quantity, Price, Cost
- Includes discount, tax, and grand total
- Default filename: "customer_bill.csv"
- Uses relative path from script directory
- Error handling: catches file I/O errors

**`export_pdf(filename)`** — Export bill to PDF
- Uses `fpdf` library (requires: `pip install fpdf2`)
- Creates formatted PDF with title
- Table layout: Item, Quantity, Price, Cost
- Includes discount, tax, and grand total
- Default filename: "customer_bill.pdf"
- Error handling: catches PDF generation and file errors

#### Workflow

```
1. Initialize GroceryStore with catalog
2. Load and display catalog
3. Create Bill object
4. Interactive loop:
   - Add items with quantities
   - Validate each item
5. Apply discount percentage
6. Apply tax percentage
7. Display final bill
8. Save to database
9. Export to CSV
10. Export to PDF
11. Ask for next customer
```

#### Error Handling Strategy

| Error Type | Handling |
|-----------|----------|
| Catalog file missing | Warning message, empty catalog, continue |
| Invalid JSON/CSV | Error message, empty catalog, continue |
| Item not in catalog | Error message, skip item, continue |
| Invalid quantity | Message, re-prompt, continue |
| Invalid discount/tax | Skip field, continue with default (0) |
| Database error | Warning, continue without persistence |
| File I/O error | Warning, continue without export |
| PDF generation error | Warning, continue without PDF |

#### Advanced Features

**Multi-Format Catalog Support**

Automatically detect and load catalog format:
```python
# JSON format (default)
main()

# CSV format
main("grocery.csv")
```

**Transaction History**

SQLite database stores all transactions:
```sql
SELECT * FROM bills WHERE date BETWEEN '2026-01-01' AND '2026-01-31';
SELECT * FROM bill_items WHERE bill_id = 5;
```

**Multiple Export Formats**
- CSV for spreadsheet analysis
- PDF for customer receipts

**Flexible Discount/Tax**
- Can apply both discount and tax
- Apply discount first, then tax
- Or apply tax first, then discount
- User controls application via input

## Data Formats

### Catalog (JSON Format)

**File:** `src/grocery.json`

```json
{
    "items": [
        {"id": 1, "name": "Rice", "price": 50},
        {"id": 2, "name": "Wheat Flour", "price": 40},
        {"id": 3, "name": "Sugar", "price": 45},
        ...
    ]
}
```

**Schema:**
- `id` (integer) — Unique product identifier
- `name` (string) — Product name
- `price` (integer/float) — Price in rupees

### Catalog (CSV Format)

**File:** `src/grocery.csv`

```
id,name,price
1,Rice,50
2,Wheat Flour,40
3,Sugar,45
4,Milk,25
```

**Format:**
- Header row required: `id, name, price`
- One product per line
- Comma-separated values
- Numeric id and price

### Bill Export (CSV Format)

**File:** `customer_bill.csv`

```
Item,Quantity,Price (Rs.),Cost (Rs.)
Rice,5,50,250
Milk,2,25,50
Bread,3,30,90

Discount,- Rs. 46.40
GST,+ Rs. 83.16
Grand Total,Rs. 376.76
```

**Format:**
- CSV export of bill items
- Summary lines for discount, tax, total
- Suitable for spreadsheet analysis

### Bill Export (PDF Format)

**File:** `customer_bill.pdf`

Professional receipt format with:
- Title "Grocery Bill"
- Table: Item, Qty, Price (Rs.), Cost (Rs.)
- Summary: Discount, GST, Grand Total
- Print-ready format

### Transaction Database (SQLite)

**File:** `grocery_records.db`

**Tables:**

**bills table:**
```sql
CREATE TABLE bills (
    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,              -- Timestamp of transaction
    discount REAL,          -- Discount amount
    tax REAL,              -- Tax amount
    total REAL             -- Final total
)
```

**bill_items table:**
```sql
CREATE TABLE bill_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER,        -- Foreign key to bills
    item_name TEXT,         -- Product name
    quantity INTEGER,       -- Quantity purchased
    price REAL,            -- Unit price
    cost REAL,             -- Total cost (price × qty)
    FOREIGN KEY (bill_id) REFERENCES bills (bill_id)
)
```

## How to Run

### Simple Version (`exercise.py`)

**Requirements:**
- Python 3.6+
- `tabulate` library: `pip install tabulate`

**Execution:**
```bash
python exercise.py
```

**Workflow:**
1. View available items
2. Add items to cart (name and quantity)
3. Enter 'q' to finish
4. View bill sorted by item name

### Advanced Version (`src/grocery_intermediate.py`)

**Requirements:**
- Python 3.6+
- Libraries:
  - `tabulate` — Table display
  - `fpdf2` — PDF generation (`pip install fpdf2`)

**Installation:**
```bash
pip install tabulate fpdf2
```

**Execution (Default Catalog - JSON):**
```bash
cd src
python grocery_intermediate.py
```

**Execution (CSV Catalog):**
```bash
cd src
python grocery_intermediate.py
# Or modify line in code: main("grocery.csv")
```

**Interactive Session:**
1. View available items
2. Add items one by one
3. Enter item name and quantity
4. Continue until entering "done"
5. Enter discount percentage (or 0)
6. Enter GST percentage (or 0)
7. View final bill
8. Bill automatically saved to database
9. Bill exported to CSV and PDF
10. Prompted for next customer

### Example Session

```
Available Grocery Items:
┌────┬───────────────┬────────────┐
│ ID │ Item          │ Price (Rs.)│
├────┼───────────────┼────────────┤
│ 1  │ Rice          │ 50         │
│ 2  │ Wheat Flour   │ 40         │
│ 3  │ Sugar         │ 45         │
│ 4  │ Milk          │ 25         │
│ 5  │ Eggs          │ 6          │
│ 6  │ Bread         │ 30         │
└────┴───────────────┴────────────┘

Enter item name to add (or 'done' to finish): Rice
Enter quantity: 5
[Item added]

Enter item name to add (or 'done' to finish): Milk
Enter quantity: 2
[Item added]

Enter item name to add (or 'done' to finish): Bread
Enter quantity: 3
[Item added]

Enter item name to add (or 'done' to finish): done

Enter discount % (0 if none): 10
Enter GST % (0 if none): 18

Final Bill:
┌───────────────┬─────┬──────────┬────────────┐
│ Item          │ Qty │ Price    │ Cost (Rs.) │
├───────────────┼─────┼──────────┼────────────┤
│ Rice          │ 5   │ 50       │ 250        │
│ Milk          │ 2   │ 25       │ 50         │
│ Bread         │ 3   │ 30       │ 90         │
└───────────────┴─────┴──────────┴────────────┘

Discount Applied: Rs.46.40
GST Applied: Rs. 83.16
Grand Total: Rs. 376.76

✅ Bill saved to database with Bill ID: 1
✅ Bill exported to /path/to/customer_bill.csv
✅ Bill exported to /path/to/customer_bill.pdf

Next customer? (y/n): n
```

## Data Structures and Algorithms

### Bill Item Storage

**Dictionary Structure:**
```python
self.items = {
    "Rice": {
        "price": 50,
        "quantity": 5,
        "cost": 250
    },
    "Milk": {
        "price": 25,
        "quantity": 2,
        "cost": 50
    }
}
```

**Time Complexity:**
- Add item: O(1) average
- Display bill: O(n) where n = number of items
- Total calculation: O(1) (running total)

**Space Complexity:** O(n) for n items

### Catalog Lookup

**Linear Search:** `O(n)` where n = number of products
```python
for item in self.items:
    if item["name"].lower() == item_name.lower():
        return item["price"]
```

For large catalogs, could optimize with dictionary indexing.

### Sorting in Simple Version

**Algorithm:** Python's built-in sort (Timsort)
```python
sorted_bill = sorted(bill.items(), key=lambda x: x[0])
```

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

### Discount/Tax Calculation

**Order of Operations:**
1. Apply discount to subtotal
2. Apply tax to discounted subtotal

**Calculation:**
```
Subtotal = Sum of (price × quantity)
After Discount = Subtotal × (1 - discount_percent/100)
After Tax = After Discount × (1 + tax_percent/100)
```

**Example:**
```
Items: 250 + 50 + 90 = 390
10% Discount: 390 × 0.90 = 351
18% Tax: 351 × 1.18 = 414.18
```

## File I/O Operations

### Loading Catalog

**JSON Loading:**
```python
with open(file, "r") as f:
    data = json.load(f)
    self.items = data["items"]
```

**CSV Loading:**
```python
with open(file, "r") as f:
    reader = csv.DictReader(f)
    self.items = [
        {"id": int(row["id"]), "name": row["name"], "price": float(row["price"])}
        for row in reader
    ]
```

### Exporting Bill

**CSV Export:**
- Opens file in write mode
- Writes header row
- Writes item rows
- Appends summary lines
- Closes file

**PDF Export:**
- Creates FPDF object
- Adds page with Arial font
- Creates table with cells
- Fills cells with data
- Outputs to file

### Database Operations

**Connection Pattern:**
```python
conn = sqlite3.connect(db_file)
c = conn.cursor()
# Execute SQL
conn.commit()
conn.close()
```

**Insert Bill:**
```sql
INSERT INTO bills (date, discount, tax, total) 
VALUES (timestamp, discount_amount, tax_amount, total_cost)
```

**Insert Bill Items:**
```sql
INSERT INTO bill_items (bill_id, item_name, quantity, price, cost)
VALUES (bill_id, name, qty, price, total_cost)
```

## Comparison: Simple vs. Advanced

| Feature | Simple (`exercise.py`) | Advanced (`grocery_intermediate.py`) |
|---------|----------------------|--------------------------------------|
| **Catalog Source** | Hardcoded | JSON/CSV file |
| **Discount Support** | ✗ | ✓ |
| **Tax Support** | ✗ | ✓ |
| **Export Options** | Display only | CSV + PDF |
| **Data Persistence** | None | SQLite database |
| **Multi-Customer** | ✗ | ✓ (loop) |
| **Error Handling** | Basic | Comprehensive |
| **Sorting** | Yes (alpha) | Items as added |
| **File Formats** | None | JSON + CSV |
| **Code Complexity** | ~70 lines | ~300 lines |
| **Learning Curve** | Beginner | Intermediate-Advanced |
| **Production Ready** | No | Yes |

## Extension Ideas

### 1. Inventory Management
```python
class Inventory:
    def __init__(self, stock_file):
        self.stock = {}  # {item: quantity}
    
    def update_after_sale(self, bill):
        for item, details in bill.items.items():
            self.stock[item] -= details["quantity"]
            if self.stock[item] < 10:
                alert_low_stock(item)
```

### 2. Customer Database
```python
class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.purchases = []  # List of bill IDs
        self.loyalty_points = 0
```

### 3. Promotions
```python
class Promotion:
    def apply(self, bill):
        # Buy 5 rice bags, get 10% discount
        if bill.items["Rice"]["quantity"] >= 5:
            return 0.10  # 10% discount
```

### 4. Analytics
```python
def get_sales_report(date_from, date_to):
    query = "SELECT * FROM bills WHERE date BETWEEN ? AND ?"
    # Generate graphs, statistics
```

### 5. Multi-Store Support
```python
class MultiStoreSystem:
    def __init__(self):
        self.stores = {}
    
    def add_store(self, store_name):
        self.stores[store_name] = GroceryStore()
```

## Technical Stack

- **Language:** Python 3.6+
- **Libraries:**
  - `tabulate` — Professional table formatting
  - `fpdf2` (or `fpdf`) — PDF generation
  - `csv` — CSV file handling (standard library)
  - `json` — JSON file handling (standard library)
  - `sqlite3` — Database (standard library)
  - `os` — File path operations (standard library)
  - `datetime` — Timestamps (standard library)

## Summary

This project demonstrates two levels of complexity:

1. **Simple Version** (`exercise.py`):
   - Good for learning basic Python concepts
   - Hardcoded data, simple algorithms
   - Suitable for educational purposes

2. **Advanced Version** (`grocery_intermediate.py`):
   - Production-ready system
   - Multi-format data handling
   - Robust error handling
   - Database persistence
   - Export capabilities
   - Extensible architecture

The progression from simple to advanced shows how a concept scales with features, complexity, and robustness in real-world applications. The advanced version serves as a template for building professional point-of-sale systems.

**Key Takeaways:**
- Multi-format data handling increases flexibility
- Error handling is critical for production systems
- Database persistence enables analytics and history
- Structured exports (CSV/PDF) improve usability
- Modular design allows easy extension
- User input validation prevents crashes
