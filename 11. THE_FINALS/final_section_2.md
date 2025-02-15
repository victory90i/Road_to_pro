# Student Grade Management System Challenge (70 Marks)
Create a command-line grade management system using Python fundamentals.

## Helpful Resources
- [PrettyTable Documentation](https://ptable.readthedocs.io/en/latest/tutorial.html)
- [Python File Handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python String Formatting](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
- [ASCII Art Generator](http://patorjk.com/software/taag/) - For program title
- [ASCII Charts Examples](https://www.text-image.com/convert/ascii.html) - For grade distribution

## Core Requirements (50 marks)

### 1. Basic Setup (10 marks)
- Clear screen functionality using `os.system('cls')` or `os.system('clear')`
- Main menu with ASCII art title
- PrettyTable for data display
- Error handling for file operations
- Input validation

### 2. Student Management (15 marks)
- Add new student (validate name)
- View all students in tabular format
- Search for student
- Delete student
- Data saved in CSV format

### 3. Grade Operations (15 marks)
- Add grades (0-100 only)
- Calculate individual averages
- Calculate class average
- Show highest/lowest scores
- Grade categorization (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)

### 4. Reporting (10 marks)
- Display grades in PrettyTable
- Show basic statistics
- Generate simple ASCII grade distribution
- Export report to text file

## Bonus Features (20 marks)
- Subject tracking (+5)
- Date stamps for grades (+5)
- Grade improvement tracking (+5)
- Custom ASCII art for menus (+5)

## Implementation Steps

### Step 1: Setup (Required)
```python
from prettytable import PrettyTable
import os
import csv
from datetime import datetime

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
```

### Step 2: Data Structure
```csv
# students.csv format:
name,grade1,grade2,grade3,date_added
John,85,90,88,2024-02-15
Sarah,92,88,95,2024-02-15
```

### Step 3: Basic Menu
```
===== STUDENT GRADE MANAGER =====
1. Add Student
2. View Students
3. Add Grade
4. View Reports
5. Exit
================================
```

## Grading Criteria

### Technical (40 marks)
- Working file operations (10)
- Correct grade calculations (10)
- Input validation (10)
- Error handling (10)

### User Interface (20 marks)
- Clear screen implementation (5)
- PrettyTable usage (5)
- Menu navigation (5)
- Data presentation (5)

### Code Quality (10 marks)
- Code organization (5)
- Error messages (5)

## Submission Requirements
1. Single Python file named `grade_manager.py`
2. Comments explaining major functions
3. Sample `students.csv` with test data

## Testing Requirements
Your program should handle:
1. Invalid inputs
2. Missing files
3. Empty data
4. Invalid grades
5. Duplicate students

## Hints
1. Use PrettyTable for all tabular data:
```python
table = PrettyTable()
table.field_names = ["Student", "Grade 1", "Grade 2", "Grade 3", "Average"]
```

2. Clear screen before each menu:
```python
def display_menu():
    clear_screen()
    # Show menu options
```

3. For ASCII grade distribution, insert your chart here:
```python
def show_grade_distribution():
    # Insert ASCII chart from website here
    # Example placement:
    # A: ███████ (7)
    # B: ████ (4)
    # etc.
```

## Time Management
- Basic setup: 1 hour
- Core features: 2-3 hours
- Testing: 1 hour
- Bonus features: 1-2 hours

Remember:
- Start with core features
- Test frequently
- Backup your code
- Comment your work
