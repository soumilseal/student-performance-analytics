
# Student Performance Analytics System

## Project Objective

The Student Performance Analytics System is a Python project that analyzes student marks and attendance data. It calculates total marks, average marks, grades, pass/fail results, subject-wise performance, and class performance.

## Technologies Used

- Python
- Pandas
- NumPy

## Dataset

The project uses a dataset containing 20 student records.

Each record contains:

- Student ID
- Name
- Department
- Python marks
- SQL marks
- Statistics marks
- Computer Networks marks
- Web Technology marks
- Attendance

## Main Features

- Read student data using Pandas
- Calculate total marks
- Calculate average marks
- Assign grades
- Check pass/fail result
- Calculate subject-wise averages
- Find highest and lowest total marks
- Calculate class average
- Calculate average attendance
- Count passed and failed students
- Find the best and lowest performing subject

## Grading Rule

| Average Marks | Grade |
|---|---|
| 90-100 | A+ |
| 80-89 | A |
| 70-79 | B |
| 60-69 | C |
| 50-59 | D |
| Below 50 | F |

## Pass/Fail Rule

A student passes when:

- Average marks are 50 or above
- Marks in every subject are 40 or above

Otherwise, the student fails.

## Project Files

- `main.py` - Main program
- `functions.py` - Reusable functions
- `students.csv` - Student dataset

## Final Result

The project successfully analyzes the student dataset and displays student performance, class statistics, subject-wise analysis, and the final outcome.
