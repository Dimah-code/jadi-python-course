# Create an empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Create dictionary with initial values
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}
print("Initial student grades:", student_grades)

# Add new key-value pairs
student_grades["Eve"] = 88
student_grades["Frank"] = 91
print("After adding new students:", student_grades)

# Update existing value
student_grades["Charlie"] = 82
print("After updating Charlie's grade:", student_grades)

# =============================================================================
# DICTIONARY MODIFICATION METHODS
# =============================================================================

# Remove specific key-value pair
removed_grade = student_grades.pop("Bob")
print(f"Removed Bob's grade: {removed_grade}")
print("After removing Bob:", student_grades)

# Remove and return last inserted item (Python 3.7+)
last_student = student_grades.popitem()
print(f"Removed last student: {last_student}")
print("After popitem:", student_grades)

# Remove all items
student_grades.clear()
print("After clearing dictionary:", student_grades)

# =============================================================================
# ADVANCED DICTIONARY OPERATIONS
# =============================================================================

# Reinitialize dictionary
course_grades = {"Math": 90, "Science": 85, "History": 88, "English": 92}

# Dictionary comprehension - increase all grades by 5
boosted_grades = {subject: grade + 5 for subject, grade in course_grades.items()}
print("Original grades:", course_grades)
print("Boosted grades:", boosted_grades)

# Filter dictionary - only grades above 87
high_grades = {subject: grade for subject, grade in course_grades.items() if grade > 87}
print("Grades above 87:", high_grades)

# Merge dictionaries
additional_grades = {"Art": 89, "Music": 94}
course_grades.update(additional_grades)
print("After merging with additional grades:", course_grades)

# =============================================================================
# DICTIONARY COPYING AND REFERENCES
# =============================================================================

# Reference assignment (both point to same dictionary)
grades_reference = course_grades
print("Original:", course_grades)
print("Reference:", grades_reference)

# Modifying original affects reference
course_grades["Math"] = 95
print("After modifying original - Reference:", grades_reference)

# Create independent copy
grades_copy = course_grades.copy()
print("Original:", course_grades)
print("Independent copy:", grades_copy)

# Modifying original doesn't affect copy
course_grades["Science"] = 87
print("After modifying original:")
print("Original:", course_grades)
print("Independent copy:", grades_copy)

# =============================================================================
# SETDEFAULT AND DEFAULTDICT USAGE
# =============================================================================

# setdefault - get value or set default if key doesn't exist
student_attendance = {"Alice": 15, "Bob": 12}
print("Alice's attendance:", student_attendance.setdefault("Alice", 0))
print(
    "Charlie's attendance (set default):", student_attendance.setdefault("Charlie", 0)
)
print("Attendance after setdefault:", student_attendance)
