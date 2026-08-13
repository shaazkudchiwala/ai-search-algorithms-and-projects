# Attendance System Project

An automated attendance tracking and management system for academic courses. The project provides functionality to record student attendance, calculate attendance percentages, and automatically categorize students into performance groups based on attendance thresholds.

## Project Overview

**Purpose:** Simplify attendance management for educational institutions by automating the tracking, calculation, and categorization of student attendance across multiple courses.

**Key Features:**
- Track student attendance per session
- Calculate attendance percentages automatically
- Categorize students into 4 attendance groups
- Display attendance summaries and grouped reports
- Support for multiple courses and students
- Data persistence via JSON

**Problem Statement:** Write a program to track student attendance for a course across multiple sessions and group students into 4 categories based on attendance percentage:
- Group 1: 91-100% attendance
- Group 2: 75-90% attendance
- Group 3: 60-75% attendance
- Group 4: Below 60% attendance

## Project Structure

```
Attendance System project/
├── src/
│   ├── main.py             # Interactive system framework (partial)
│   └── courses.json        # Course data and session counts
└── README.md               # This file
```

## Implementation Overview

### 1. Complete Implementation (`exercise.py`)

A fully functional attendance tracking system with working implementations of all core features.

#### Key Classes

**`Student` Class**
```python
class Student:
    def __init__(self, name, attendance):
        self.name              # Student name
        self.attendance        # List of 1s (present) and 0s (absent)
        self.total_sessions    # Total number of sessions
        self.present_days      # Count of sessions attended
        self.percentage        # Calculated attendance percentage (0-100)
        self.group            # Assigned group (1-4)
```

**Attributes:**
- `name` — Student identifier
- `attendance` — List of binary values (1=present, 0=absent) for each session
- `total_sessions` — Total number of sessions (length of attendance list)
- `present_days` — Sum of attendance list (total sessions attended)
- `percentage` — Calculated as `(present_days / total_sessions) * 100`, rounded to 2 decimals
- `group` — Dynamically assigned based on percentage thresholds

**Methods:**
- `assign_group()` — Returns group classification based on percentage:
  - ≥91% → "Group 1"
  - ≥75% → "Group 2"
  - ≥60% → "Group 3"
  - <60% → "Group 4"

**`AttendanceTracker` Class**
```python
class AttendanceTracker:
    def __init__(self):
        self.students        # List of Student objects
        self.groups          # Dictionary grouping students by attendance category
```

**Attributes:**
- `students` — List containing all Student instances
- `groups` — Dictionary with keys "Group 1"-"Group 4"; values are lists of student names in each group

**Methods:**
- `add_student(name, attendance)` — Creates Student object, adds to tracker, and groups them
  - Parameters: `name` (string), `attendance` (list of 1s and 0s)
  - Calculates percentage and group automatically
  
- `display_attendance_summary()` — Prints formatted table of all students
  - Columns: Name, Present (count), Total Sessions, Attendance %, Group
  - Uses `tabulate` library for grid formatting
  - Sorted by input order

- `display_grouped_table()` — Prints 4-column table organized by groups
  - Columns: Group 1 (91-100%), Group 2 (75-90%), Group 3 (60-75%), Group 4 (<60%)
  - Handles groups of different sizes with padding
  - Uses `tabulate` library for grid formatting

#### Attendance Calculation Logic

```
Attendance % = (Present Sessions / Total Sessions) × 100
```

**Example:**
- Student attended 4 sessions out of 5
- Percentage = (4/5) × 100 = 80%
- Group = "Group 2" (75-90% range)

#### Sample Output

**Attendance Summary Table:**
```
📋 Attendance Summary:

┌────────┬─────────┬────────────────┬────────────────┬─────────┐
│ Name   │ Present │ Total Sessions │ Attendance %   │ Group   │
├────────┼─────────┼────────────────┼────────────────┼─────────┤
│ Shaaz  │ 5       │ 5              │ 100.0%         │ Group 1 │
│ Aarav  │ 4       │ 5              │ 80.0%          │ Group 2 │
│ Ishita │ 2       │ 5              │ 40.0%          │ Group 4 │
│ Riya   │ 3       │ 5              │ 60.0%          │ Group 3 │
│ Kabir  │ 1       │ 5              │ 20.0%          │ Group 4 │
│ Zoya   │ 4       │ 5              │ 80.0%          │ Group 2 │
└────────┴─────────┴────────────────┴────────────────┴─────────┘
```

**Grouped Table:**
```
📊 Students Grouped by Attendance:

┌───────────────────┬────────────────┬────────────────┬────────────┐
│ Group 1 (91-100%) │ Group 2 (75-90%)│ Group 3 (60-75%)│ Group 4 (<60%)│
├───────────────────┼────────────────┼────────────────┼────────────┤
│ Shaaz             │ Aarav          │ Riya           │ Ishita     │
│                   │ Zoya           │                │ Kabir      │
└───────────────────┴────────────────┴────────────────┴────────────┘
```

### 2. Interactive Framework (`src/main.py`)

A skeleton implementation providing a menu-driven interface for attendance management. Currently incomplete but demonstrates intended architecture.

#### Key Classes (Framework)

**`Student` Class**
```python
class Student:
    def __init__(self, student_name, student_roll):
        self.student_name    # Student name
        self.student_roll    # Roll number (integer)
```

**`CourseRecords` Class**
- Manages JSON file for a specific course
- Plans to store course data and student enrollment
- Handles file creation and path management

**`AttendanceManager` Class**
- Central manager for multiple courses and students
- Maintains lists of courses and students
- Provides methods for:
  - `add_student(name, roll)` — Add student to system
  - `mark_attendance(roll)` — Mark student present (stub)
  - `find_student_attendance(roll)` — Query student attendance (stub)
  - `add_course(course_name, total_sessions)` — Register new course (stub)
  - `show_groups_table()` — Display grouped report (stub)

#### Interactive Menu

The `main()` function provides an interactive loop with options:
1. Mark Attendance
2. Show categorized table of students
3. Find Attendance of a student
4. Add New Student to course
5. Add a New Course
6. Exit System

Input validation for menu choices and roll numbers (must be positive integers).

#### Design Considerations

- **File Management:** Uses `os.path` for cross-platform path handling
- **Error Handling:** Try-except blocks for invalid input
- **Extensibility:** Modular class structure allows future expansion
- **Data Persistence:** Plans to use JSON for course and enrollment data

### 3. Course Data (`src/courses.json`)

Pre-defined course list with metadata:

```json
{
    "courses": [
        {
            "course_id": 1,
            "course_name": "Robotics",
            "total_sessions": 12
        },
        {
            "course_id": 2,
            "course_name": "AI",
            "total_sessions": 6
        },
        {
            "course_id": 3,
            "course_name": "A&D Electronics",
            "total_sessions": 12
        },
        {
            "course_id": 4,
            "course_name": "BMFA",
            "total_sessions": 12
        },
        {
            "course_id": 5,
            "course_name": "Machine Drawing",
            "total_sessions": 24
        }
    ]
}
```

**Schema:**
- `course_id` — Unique course identifier
- `course_name` — Name of the course
- `total_sessions` — Total number of sessions for the course

## How to Run

### Complete Implementation (`exercise.py`)

**Requirements:**
- Python 3.6+
- `tabulate` library: `pip install tabulate`

**Execution:**
```bash
python exercise.py
```

**Output:**
The program automatically runs with sample data (6 students, 5 sessions each) and displays:
1. Attendance Summary table with all students
2. Grouped table showing students organized by attendance category

**Modify Sample Data:**
Edit the sample data at the bottom of `exercise.py`:
```python
tracker.add_student("StudentName", [1, 1, 0, 1, 1])  # 1=present, 0=absent
```

### Interactive Framework (`src/main.py`)

**Note:** Currently incomplete; stub methods not fully implemented.

**Execution:**
```bash
cd src
python main.py
```

**Interactive Menu:**
```
Enter option number for the task you want to perform:
1. Mark Attendance
2. Show catogorized table of students
3. Find Attendance of a student
4. Add New Student to course
5. Add a New Course
6. Exit System
```

## Data Structures and Design Patterns

### Attendance Representation

**Binary List Format:**
```python
attendance = [1, 1, 0, 1, 1]  # 1=present, 0=absent
```
- **Advantages:** Simple, compact, easy to calculate
- **Disadvantages:** No date information; no session labels

**Alternative Representation (not used):**
```python
attendance = {"Session 1": True, "Session 2": True, ...}  # More descriptive
```

### Grouping Strategy

**Dictionary-based Organization:**
```python
self.groups = {
    "Group 1": ["Shaaz", "Riya"],
    "Group 2": ["Aarav", "Zoya"],
    "Group 3": [],
    "Group 4": ["Ishita", "Kabir"]
}
```
- **Time Complexity:** O(1) for group assignment; O(n) for display
- **Space Complexity:** O(n) for storing all students

### File Management (`src/main.py`)

**JSON-based Storage:**
```python
course_records_file = f"course_{course_name}.json"
```
- Per-course JSON files for enrollment and attendance data
- Uses `os.path.join()` for cross-platform compatibility
- Creates file if doesn't exist; warns if already exists

## Attendance Grouping Logic

### Threshold-Based Categorization

| Group | Attendance Range | Typical Meaning | Action |
|-------|-----------------|-----------------|--------|
| Group 1 | 91-100% | Excellent attendance | No action needed |
| Group 2 | 75-90% | Good attendance | Monitor borderline cases |
| Group 3 | 60-75% | Average attendance | Advise improvement |
| Group 4 | <60% | Poor attendance | Intervention required |

### Calculation Example

**Student: Aarav**
- Attendance list: `[1, 1, 0, 1, 1]`
- Sessions attended: 4
- Total sessions: 5
- Percentage: (4/5) × 100 = 80%
- Group assignment: 80% falls in 75-90% range → **Group 2**

## Key Implementation Details

### Percentage Calculation

```python
self.percentage = round((self.present_days / self.total_sessions) * 100, 2)
```
- Rounded to 2 decimal places for readability
- Uses standard rounding (0.5 rounds up)
- Ranges from 0.0% to 100.0%

### Group Assignment Logic

```python
def assign_group(self):
    if self.percentage >= 91:
        return "Group 1"
    elif self.percentage >= 75:
        return "Group 2"
    elif self.percentage >= 60:
        return "Group 3"
    else:
        return "Group 4"
```
- Uses sequential if-elif for efficiency (O(1) worst case 4 comparisons)
- Boundary values (91, 75, 60) are inclusive (≥)
- No gap between thresholds; all percentages covered

### Table Formatting

Uses `tabulate` library for professional output:
```python
from tabulate import tabulate
print(tabulate(table_data, headers=[...], tablefmt="grid"))
```
- Grid format provides clear visual separation
- Unicode box-drawing characters
- Headers automatically formatted
- Flexible column widths

### Variable-Length Group Handling

```python
max_len = max(len(names) for names in self.groups.values())
for i in range(max_len):
    row = []
    for group in [...]:
        row.append(self.groups[group][i] if i < len(self.groups[group]) else "")
```
- Handles groups of different sizes
- Pads with empty strings for shorter groups
- Ensures aligned columns in output

## Potential Extensions

### 1. Session Details
```python
# Store dates and session information
self.attendance = {
    "2026-01-15": True,
    "2026-01-22": True,
    "2026-01-29": False,
}
```

### 2. Multiple Courses
```python
# Track student enrollment and attendance across courses
student.courses = {
    "AI": [1, 1, 0, 1],
    "Robotics": [1, 0, 1, 1]
}
```

### 3. Attendance Trends
```python
# Analyze attendance patterns over time
def get_attendance_trend(self):
    return [sum(self.attendance[:i]) / i for i in range(1, len(self.attendance) + 1)]
```

### 4. Notifications
```python
# Alert when attendance drops below threshold
if new_percentage < 75:
    notify_guardian(student.name, new_percentage)
```

### 5. Exemptions
```python
# Handle medical leaves, special circumstances
student.exemptions = ["2026-02-05", "2026-02-12"]
adjusted_percentage = calculate_with_exemptions()
```

## Technical Stack

- **Language:** Python 3.6+
- **Libraries:** 
  - `tabulate` — Formatted table display
  - `os` — File path handling
  - `json` — Data persistence (courses.json)
- **Data Format:** JSON for course configuration and future enrollment data
- **No Database:** Currently uses in-memory data structures and JSON files

## Use Cases

1. **Educational Institutions**
   - Track class attendance for regulatory compliance
   - Identify students at risk of academic failure
   - Generate attendance reports for administration

2. **Corporate Training**
   - Monitor attendance for training programs
   - Identify engaged vs. disengaged participants

3. **Research Participation**
   - Track subject attendance for longitudinal studies
   - Ensure adequate participation for valid data

## Summary

This project provides a complete, working attendance tracking system (`exercise.py`) with automatic categorization and formatted reporting. It also includes a framework for a more sophisticated, interactive system (`src/main.py`) that demonstrates extensible architecture for future development.

**Key Strengths:**
- Simple, clear data representation
- Automatic calculation and categorization
- Professional formatted output
- Well-organized class structure
- Extensible design

**Current Limitations:**
- Interactive framework incomplete (stub methods)
- No persistent storage in complete version
- No date/time tracking for sessions
- No multi-course support
- No attendance modification after input

**Best Use:** Educational context where attendance is tracked per session and students are grouped for intervention or recognition based on attendance performance.
