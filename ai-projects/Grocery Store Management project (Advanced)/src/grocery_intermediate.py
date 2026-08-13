# Program to generate customer bill (in csv and pdf formats) 
# by extracting items data from json/csv file (grocery.json) 
# and recording past bills in SQLite database with error handling.


# Understand the code here:
# https://chatgpt.com/s/t_68b956375d4c819191e4227959e1979f


#Prompt for explaination:
# Let's decipher the meaning of this code step by step. Explain in whichever sequence according to what is understandable. Let's break down different elements of the code to understand in detail, the utility, usecase in ourcase, datatype of a variable, etc etc of each function through multiple prompts. Explain to me like I am a beginner:

import os
import json
import csv
import sqlite3
from datetime import datetime
from fpdf import FPDF
from tabulate import tabulate


class GroceryStore:
    def __init__(self, catalog_file=None):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        if catalog_file is None:
            catalog_file = os.path.join(self.base_path, "grocery.json")
        else:
            # Always load relative to script folder
            catalog_file = os.path.join(self.base_path, catalog_file)
        self.catalog_file = catalog_file
        self.items = []
        self.load_catalog()


    def load_catalog(self):
        """Load items from JSON or CSV file with error handling"""
        try:
            if self.catalog_file.endswith(".json"):
                with open(self.catalog_file, "r") as f:
                    data = json.load(f)
                    self.items = data["items"]
            elif self.catalog_file.endswith(".csv"):
                with open(self.catalog_file, "r") as f:
                    reader = csv.DictReader(f)
                    self.items = [
                        {"id": int(row["id"]), "name": row["name"], "price": float(row["price"])}
                        for row in reader
                    ]
            else:
                raise ValueError("Unsupported catalog format. Use JSON or CSV.")
        except FileNotFoundError:
            print(f"❌ Catalog file '{self.catalog_file}' not found.")
            self.items = []
        except (json.JSONDecodeError, ValueError) as e:
            print(f"❌ Error loading catalog: {e}")
            self.items = []

    def display_items(self):
        if not self.items:
            print("\n⚠️ No items available to display!")
            return
        print("\nAvailable Grocery Items:")
        table = [(item["id"], item["name"], item["price"]) for item in self.items]
        print(tabulate(table, headers=["ID", "Item", "Price (Rs.)"], tablefmt="grid"))

    def get_price(self, item_name):
        for item in self.items:
            if item["name"].lower() == item_name.lower():
                return item["price"]
        return None


class Bill:
    def __init__(self, store, db_file="grocery_records.db"):
        self.store = store
        self.items = {}
        self.total_cost = 0.0
        self.discount = 0.0
        self.tax = 0.0
        self.db_file = os.path.join(self.store.base_path, db_file)
        self._init_db()

    def _init_db(self):
        """Create database tables if not exist"""
        try:
            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS bills (
                    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    discount REAL,
                    tax REAL,
                    total REAL
                )
            """)
            c.execute("""
                CREATE TABLE IF NOT EXISTS bill_items (
                    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    bill_id INTEGER,
                    item_name TEXT,
                    quantity INTEGER,
                    price REAL,
                    cost REAL,
                    FOREIGN KEY (bill_id) REFERENCES bills (bill_id)
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"❌ Database init error: {e}")
        finally:
            conn.close()

    def add_item(self, item_name, quantity):
        price = self.store.get_price(item_name)
        if price is None:
            print(f"❌ {item_name} not found in store!")
            return
        cost = price * quantity
        if item_name in self.items:
            self.items[item_name]["quantity"] += quantity
            self.items[item_name]["cost"] += cost
        else:
            self.items[item_name] = {"price": price, "quantity": quantity, "cost": cost}
        self.total_cost += cost

    def apply_discount(self, percent):
        if percent > 0:
            self.discount = (percent / 100) * self.total_cost
            self.total_cost -= self.discount

    def apply_tax(self, percent):
        if percent > 0:
            self.tax = (percent / 100) * self.total_cost
            self.total_cost += self.tax

    def save_to_db(self):
        """Save bill and items to database"""
        try:
            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()
            # Insert bill
            c.execute("INSERT INTO bills (date, discount, tax, total) VALUES (?, ?, ?, ?)",
                      (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.discount, self.tax, self.total_cost))
            bill_id = c.lastrowid
            # Insert items
            for item, details in self.items.items():
                c.execute("INSERT INTO bill_items (bill_id, item_name, quantity, price, cost) VALUES (?, ?, ?, ?, ?)",
                          (bill_id, item, details["quantity"], details["price"], details["cost"]))
            conn.commit()
            print(f"✅ Bill saved to database with Bill ID: {bill_id}")
        except sqlite3.Error as e:
            print(f"❌ Database save error: {e}")
        finally:
            conn.close()

    def display_bill(self):
        if not self.items:
            print("\n⚠️ No items in bill!")
            return
        table = [(item, details["quantity"], details["price"], details["cost"])
                 for item, details in self.items.items()]
        print("\nFinal Bill:")
        print(tabulate(table, headers=["Item", "Qty", "Price (Rs.)", "Cost (Rs.)"], tablefmt="grid"))
        print(f"\nDiscount Applied: Rs.{self.discount:.2f}")
        print(f"GST Applied: Rs. {self.tax:.2f}")
        print(f"Grand Total: Rs. {self.total_cost:.2f}")

    def export_csv(self, filename="bill.csv"):
        try:
            path = os.path.join(self.store.base_path, filename)
            with open(path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Item", " Quantity", " Price (Rs.)", "Cost (Rs.)"])
                for item, details in self.items.items():
                    writer.writerow([item, details["quantity"], details["price"], details["cost"]])
                writer.writerow([])
                writer.writerow(["Discount", f"- Rs. {self.discount:.2f}"])
                writer.writerow(["GST", f"+ Rs. {self.tax:.2f}"])
                writer.writerow(["Grand Total", f"Rs. {self.total_cost:.2f}"])
            print(f"✅ Bill exported to {path}")
        except OSError as e:
            print(f"❌ Failed to export CSV: {e}")

    def export_pdf(self, filename="bill.pdf"):
        try:
            path = os.path.join(self.store.base_path, filename)
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Grocery Bill", ln=True, align="C")

            pdf.ln(10)
            pdf.set_font("Arial", size=10)
            pdf.cell(60, 10, "Item", 1)
            pdf.cell(30, 10, "Qty", 1)
            pdf.cell(40, 10, "Price (Rs.)", 1)
            pdf.cell(40, 10, "Cost (Rs.)", 1)
            pdf.ln()

            for item, details in self.items.items():
                pdf.cell(60, 10, item, 1)
                pdf.cell(30, 10, str(details["quantity"]), 1)
                pdf.cell(40, 10, str(details["price"]), 1)
                pdf.cell(40, 10, str(details["cost"]), 1)
                pdf.ln()

            pdf.ln(5)
            pdf.cell(100, 10, f"Discount: Rs. {self.discount:.2f}", 0, 1)
            pdf.cell(100, 10, f"GST: Rs. {self.tax:.2f}", 0, 1)
            pdf.cell(100, 10, f"Grand Total: Rs. {self.total_cost:.2f}", 0, 1)

            pdf.output(path)
            print(f"✅ Bill exported to {path}")
        except OSError as e:
            print(f"❌ Failed to export PDF: {e}")
        except Exception as e:
            print(f"❌ Unexpected PDF export error: {e}")


# Main
def main(catalog_file=None):
    store = GroceryStore(catalog_file)
    if not store.items:
        print("⚠️ Cannot continue without catalog items. No items in store.")
        return

    while True:
        bill = Bill(store)

        while True:
            try:
                store.display_items()
                choice = input("\nEnter item name to add (or 'done' to finish): ").strip()
            except KeyboardInterrupt:
                print("\n❌ Program interrupted by user.")
                return

            if choice.lower() == "done":
                break
            if not choice:
                print("Item name cannot be empty!")
                continue
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive!")
                    continue
                bill.add_item(choice, quantity)
            except ValueError:
                print("Invalid quantity! Please enter a number.")
                continue

        try:
            d = float(input("\nEnter discount % (0 if none): "))
            bill.apply_discount(d)
        except ValueError:
            print("Invalid discount, skipped.")

        try:
            t = float(input("Enter GST % (0 if none): "))
            bill.apply_tax(t)
        except ValueError:
            print("Invalid GST, skipped.")

        bill.display_bill()
        bill.save_to_db()
        bill.export_csv("customer_bill.csv")
        bill.export_pdf("customer_bill.pdf")

        cont = input("\nNext customer? (y/n): ").lower()
        if cont != "y":
            break


if __name__ == "__main__":
    main()  #can pass any grocery file in json or csv format as argument. If not given, then it will automatically consider the grocery.json file by default. 
    # main("grocery.csv")  ##try it out 