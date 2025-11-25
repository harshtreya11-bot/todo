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
    "sem2": {
        "human_values": 2,
        "human_values_activities_&_ports": 1,
        "engineering_mathematics_II": 4,
        "engineering_physics":  4,
        "engineering_physics_lab": 1,
        "programming_for_problem_solving": 2,
        "basic_civil_engineering": 2,
        "computer_programming_lab": 1.5,
        "basic_civil_engineering_lab": 1,
        "computer_aided_machine_drawing": 1.5,
        "sports": 0.5
     }
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

def second_sem_SGPA():
    human_values = getCgpa(input("Enter the grade of Human Value :"))
    human_values_activities_ports = getCgpa(input("Enter the grade of Human Values Activities & Sports :"))
    engineering_mathematics = getCgpa(input("Enter the grade of Engineering Mathematics-II :"))
    engineering_physics = getCgpa(input("Enter the grade of Engineering Physics :"))
    engineering_physics_lab = getCgpa(input("Enter the grade of Engineering Physics Lab :"))
    programming_for_problem_solving = getCgpa(input("Enter the grade of Programming For Problem Solving :"))
    basic_civil_engineering = getCgpa(input("Enter the grade of Basic Civil Engineering :"))
    computer_programming_lab = getCgpa(input("Enter the grade of Computer Programming Lab :"))
    basic_civil_engineering_lab = getCgpa(input("Enter the grade of Basic Civil Engineering Lab :"))
    computer_aided_machine_drawing = getCgpa(input("Enter the grade of Computer Aided Machine Drawing :"))
    sports = getCgpa(input("Enter the grade of Sports :"))

    sgpaq = calculate_sgpa( 
        [ human_values,
          human_values_activities_ports,
          engineering_mathematics,
          engineering_physics,
          engineering_physics_lab,
          programming_for_problem_solving,
          basic_civil_engineering,
          computer_programming_lab,
          basic_civil_engineering_lab,
          computer_aided_machine_drawing,
          sports,
        ],
        list(credits["sem2"].values()),
    )
    print("SGPA:", sgpaq)


while True:
    print("Welcome to SGPA Calculater")
    print("Press 1. for calculate 1st Sem SGPA")
    print("Press 2. for Calculate 2nd Sem SGAP")
    x = int(input("Select the semester which you want to find the SGPA"))
    if x == 1:
        print("Welcome to 1sem SGPA calculator")
        first_sem_SGPA()
    elif x == 2:
        print("Welcome to 2nd Sem SGPA calculator")
        second_sem_SGPA()
    else:
        print("Ooooops you enter wrong value try again :(")    
