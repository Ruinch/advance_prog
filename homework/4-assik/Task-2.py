import json

# read json
with open("homework/4-assik/students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

i = 0
while i < len(students):
    grades = students[i]["grades"]

    # count sum of grades
    s = 0
    j = 0
    while j < len(grades):
        s = s + grades[j]
        j = j + 1

    avg = s / len(grades)

    # add avg
    students[i]["average"] = int(avg)

    i = i + 1


# write new file
with open("homework/4-assik/students_avg.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)
