#Moises Garay
#CIS 261
#WK10 VIBE Coding

import os


def load_records():
    """
    Loads student records from student_grades.txt
    Returns a list of student dictionaries or empty list if file doesn't exist
    """
    filename = "student_grades.txt"
    records = []
    
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:  # Skip empty lines
                        parts = line.split('|')
                        if len(parts) == 7:
                            student = {
                                'name': parts[0],
                                'id': parts[1],
                                'test1': float(parts[2]),
                                'test2': float(parts[3]),
                                'test3': float(parts[4]),
                                'average': float(parts[5]),
                                'grade': parts[6]
                            }
                            records.append(student)
    except Exception as e:
        print(f"Error loading records: {e}")
    
    return records


def save_records(records):
    """
    Saves all student dictionaries to student_grades.txt
    Formats all numbers to 2 decimal places
    """
    filename = "student_grades.txt"
    
    try:
        with open(filename, 'w') as file:
            for student in records:
                line = (f"{student['name']}|{student['id']}|"
                        f"{student['test1']:.2f}|{student['test2']:.2f}|"
                        f"{student['test3']:.2f}|{student['average']:.2f}|"
                        f"{student['grade']}\n")
                file.write(line)
        print("Records saved successfully!")
    except Exception as e:
        print(f"Error saving records: {e}")


def calculate_average(test1, test2, test3):
    """
    Calculates and returns the average of three test scores
    """
    return (test1 + test2 + test3) / 3


def calculate_grade(average):
    """
    Returns a letter grade based on the average:
    A = 90–100
    B = 80–89
    C = 70–79
    D = 60–69
    F = below 60
    """
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def add_student(records):
    """
    Prompts user for student info and adds to records list
    Validates numeric input for test scores
    """
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return
        
        student_id = input("Enter student ID: ").strip()
        if not student_id:
            print("ID cannot be empty!")
            return
        
        # Get and validate test scores
        test1 = float(input("Enter Test 1 score: "))
        test2 = float(input("Enter Test 2 score: "))
        test3 = float(input("Enter Test 3 score: "))
        
        # Calculate average and grade
        average = calculate_average(test1, test2, test3)
        grade = calculate_grade(average)
        
        # Create student dictionary
        student = {
            'name': name,
            'id': student_id,
            'test1': test1,
            'test2': test2,
            'test3': test3,
            'average': average,
            'grade': grade
        }
        
        # Add to records
        records.append(student)
        print(f"\nStudent {name} added successfully!")
        print(f"Average: {average:.2f}, Grade: {grade}\n")
        
    except ValueError:
        print("Invalid input! Please enter valid numbers for test scores.\n")
    except Exception as e:
        print(f"Error adding student: {e}\n")


def display_all_students(records):
    """
    Prints a formatted table with all students
    Columns: Name, ID, Test1, Test2, Test3, Average, Grade
    """
    if not records:
        print("No students in the system.\n")
        return
    
    print("\n" + "="*100)
    print(f"{'Name':<20} {'ID':<12} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10} {'Average':<10} {'Grade':<8}")
    print("="*100)
    
    for student in records:
        print(f"{student['name']:<20} {student['id']:<12} "
              f"{student['test1']:<10.2f} {student['test2']:<10.2f} "
              f"{student['test3']:<10.2f} {student['average']:<10.2f} {student['grade']:<8}")
    
    print("="*100 + "\n")


def search_student(records):
    """
    Searches for students by name (case-insensitive)
    Shows all matching students if multiple matches found
    """
    if not records:
        print("No students in the system.\n")
        return
    
    try:
        search_name = input("Enter student name to search: ").strip().lower()
        
        if not search_name:
            print("Search name cannot be empty!\n")
            return
        
        matches = [s for s in records if search_name in s['name'].lower()]
        
        if not matches:
            print("No student found with that name.\n")
        else:
            print(f"\n Found {len(matches)} match(es):")
            print("="*100)
            print(f"{'Name':<20} {'ID':<12} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10} {'Average':<10} {'Grade':<8}")
            print("="*100)
            
            for student in matches:
                print(f"{student['name']:<20} {student['id']:<12} "
                      f"{student['test1']:<10.2f} {student['test2']:<10.2f} "
                      f"{student['test3']:<10.2f} {student['average']:<10.2f} {student['grade']:<8}")
            
            print("="*100 + "\n")
    
    except Exception as e:
        print(f"Error searching student: {e}\n")


def class_statistics(records):
    """
    Calculates and displays class statistics:
    - Class average
    - Highest average (with student name)
    - Lowest average (with student name)
    """
    if not records:
        print("No students in the system.\n")
        return
    
    try:
        # Calculate class average
        total_avg = sum(s['average'] for s in records)
        class_avg = total_avg / len(records)
        
        # Find highest and lowest
        highest_student = max(records, key=lambda s: s['average'])
        lowest_student = min(records, key=lambda s: s['average'])
        
        print("\n" + "="*50)
        print("CLASS STATISTICS")
        print("="*50)
        print(f"Number of Students: {len(records)}")
        print(f"Class Average: {class_avg:.2f}")
        print(f"Highest Average: {highest_student['average']:.2f} ({highest_student['name']})")
        print(f"Lowest Average: {lowest_student['average']:.2f} ({lowest_student['name']})")
        print("="*50 + "\n")
    
    except Exception as e:
        print(f"Error calculating statistics: {e}\n")


def main_menu():
    """
    Displays main menu and handles user choices
    Loops until user chooses to exit
    """
    records = load_records()
    
    while True:
        print("\n" + "="*50)
        print("STUDENT GRADE CALCULATOR")
        print("="*50)
        print("1. Add New Student")
        print("2. Display All Students")
        print("3. Search Student by Name")
        print("4. View Class Statistics")
        print("5. Save and Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_student(records)
        elif choice == '2':
            display_all_students(records)
        elif choice == '3':
            search_student(records)
        elif choice == '4':
            class_statistics(records)
        elif choice == '5':
            save_records(records)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.\n")


if __name__ == "__main__":
    main_menu()
