
def calculate_total(row):
    total = row["Python"] + row["SQL"] + row["Statistics"] + row["Computer_Networks"] + row["Web_Technology"]
    return total


def calculate_average(total):
    return total / 5


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_result(row):
    if row["Average"] >= 50 and row["Python"] >= 40 and row["SQL"] >= 40 and row["Statistics"] >= 40 and row["Computer_Networks"] >= 40 and row["Web_Technology"] >= 40:
        return "Pass"
    else:
        return "Fail"
