credits = {
    "sem1": {
        "communiction_skill": 2,
        "engineering_mathematics": 4,
        "engineering_chemistry": 4,
        "basic_electrical_engineering": 2,
        "basic_machanical_engineering": 2,
        "language_lab": 1,
        "engineering_chemistry_lab": 1,
        "practice_manufacturing_workshop": 1.5,
        "electrical_lab": 1,
        "caeg": 1.5,
        "sports": 0.5,
    },
}


def getCgpa(grade):
    if grade == "A++":
        return 10
    elif grade == "A+":
        return 9
    elif grade == "A":
        return 8.5
    elif grade == "B+":
        return 8
    elif grade == "B":
        return 7.5
    elif grade == "C+":
        return 7
    elif grade == "C":
        return 6.5
    elif grade == "D+":
        return 6
    elif grade == "D":
        return 5.5
    elif grade == "E+":
        return 5
    elif grade == "E":
        return 4
    elif grade == "F":
        return 0


def calculate_sgpa(grade_points: list, credits: list):
    print(credits)
    submission_grade_points_credits = 0
    submission_credits = 0
    for idx, grade_point in enumerate(grade_points):
        submission_grade_points_credits += credits[idx] * grade_point
        submission_credits += credits[idx]

    return submission_grade_points_credits / submission_credits


def first_sem_SGPA():
    communication_skill = getCgpa(input("Entre the grade of Communication Skill :"))
    engineering_mathematics = getCgpa(
        input("Entre the grade og Engineering Mathematics :")
    )
    engineering_chemistry = getCgpa(
        input("Entre the grade of Engineering Cheistry I :")
    )
    bee = getCgpa(input("Entre the grade of Basic Electrical engineering :"))
    bme = getCgpa(input("Entre the Grade of Basic Mechanical Engineering :"))
    language_lab = getCgpa(input("Enter the grade of Languade Lab :"))
    engineering_chemistry_lab = getCgpa(input("Enter the grade of Chemistry Lab :"))
    manufature_lab = getCgpa(input("enter the grade of Practice Workshop: "))
    electrical_lab = getCgpa(input("Enter the grade of Electrical Lab :"))
    caeg = getCgpa(input("Enter the marks of Computer Aided Engineering Graphics :"))
    sports = getCgpa(input("Enter the marks of Sports Activities :"))

    sgpa = calculate_sgpa(
        [
            communication_skill,
            engineering_mathematics,
            engineering_chemistry,
            bee,
            bme,
            language_lab,
            engineering_chemistry_lab,
            manufature_lab,
            electrical_lab,
            caeg,
            sports,
        ],
        list(credits["sem1"].values()),
    )
    print(credits["sem1"].values())

    print("SGPA:", sgpa)


while True:
    print("Welcome to SGPA Calculater")
    print("Press 1. for calculate 1st Sem SGPA")
    print("Press 2. for Calculate 2nd Sem SGAP")
    x = int(input("Select the semester which you want to find the SGPA"))
    if x == 1:
        print("Welcome to 1sem SGPA calculator")
        first_sem_SGPA()
    if x == 2:
        print("Welcome to 2nd Sem SGPA calculator")
