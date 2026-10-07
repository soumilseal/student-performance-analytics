
import pandas as pd
import numpy as np
from functions import calculate_total, calculate_average, calculate_grade, check_result

data = pd.read_csv("students.csv")

for i in range(len(data)):
    data.loc[i, "Total"] = calculate_total(data.loc[i])

for i in range(len(data)):
    data.loc[i, "Average"] = calculate_average(data.loc[i, "Total"])

for i in range(len(data)):
    data.loc[i, "Grade"] = calculate_grade(data.loc[i, "Average"])

for i in range(len(data)):
    data.loc[i, "Result"] = check_result(data.loc[i])

performance = data[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]]

subject_averages = data[["Python", "SQL", "Statistics", "Computer_Networks", "Web_Technology"]].mean()

class_average = np.mean(data["Average"])
highest_total = np.max(data["Total"])
lowest_total = np.min(data["Total"])
average_attendance = np.mean(data["Attendance"])

pass_count = 0
fail_count = 0

for result in data["Result"]:
    if result == "Pass":
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

if subject_averages["Python"] >= subject_averages["SQL"] and subject_averages["Python"] >= subject_averages["Statistics"] and subject_averages["Python"] >= subject_averages["Computer_Networks"] and subject_averages["Python"] >= subject_averages["Web_Technology"]:
    best_subject = "Python"
else:
    if subject_averages["SQL"] >= subject_averages["Statistics"] and subject_averages["SQL"] >= subject_averages["Computer_Networks"] and subject_averages["SQL"] >= subject_averages["Web_Technology"]:
        best_subject = "SQL"
    elif subject_averages["Statistics"] >= subject_averages["Computer_Networks"] and subject_averages["Statistics"] >= subject_averages["Web_Technology"]:
        best_subject = "Statistics"
    elif subject_averages["Computer_Networks"] >= subject_averages["Web_Technology"]:
        best_subject = "Computer Networks"
    else:
        best_subject = "Web Technology"

if subject_averages["Python"] <= subject_averages["SQL"] and subject_averages["Python"] <= subject_averages["Statistics"] and subject_averages["Python"] <= subject_averages["Computer_Networks"] and subject_averages["Python"] <= subject_averages["Web_Technology"]:
    lowest_subject = "Python"
else:
    if subject_averages["SQL"] <= subject_averages["Statistics"] and subject_averages["SQL"] <= subject_averages["Computer_Networks"] and subject_averages["SQL"] <= subject_averages["Web_Technology"]:
        lowest_subject = "SQL"
    elif subject_averages["Statistics"] <= subject_averages["Computer_Networks"] and subject_averages["Statistics"] <= subject_averages["Web_Technology"]:
        lowest_subject = "Statistics"
    elif subject_averages["Computer_Networks"] <= subject_averages["Web_Technology"]:
        lowest_subject = "Computer Networks"
    else:
        lowest_subject = "Web Technology"

print("==================================================")
print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("==================================================")
print()
print("========== STUDENT DATA ==========")
print(data[["Student_ID", "Name", "Department", "Python", "SQL", "Statistics", "Computer_Networks", "Web_Technology", "Attendance"]])
print()
print("========== STUDENT PERFORMANCE ==========")
print(performance)
print()
print("========== ANALYSIS ==========")
print("Class Average:", round(class_average, 2))
print("Highest Total:", highest_total)
print("Lowest Total:", lowest_total)
print("Average Attendance:", round(average_attendance, 2))
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)
print("Best Subject:", best_subject)
print("Lowest Subject:", lowest_subject)
print()
print("========== FINAL OUTCOME ==========")
print("The student performance analysis has been completed successfully.")
