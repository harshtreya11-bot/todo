# First we will a List with the name Expense
import json
Expense = []11

def load_expense():
    result = None
    try:
        with open("Expense.json","r") as E:
            result = json.load(E)
    except:
            result=[]    

    return  result   
def update_file():
    with open("Expense.json","w") as E:
        json.dump(Expense,E)   
# then we define a fuunction to add expenses properties which we will take input from user
def expenses_tracker():
    Expense_price = input("Entre the  Expense Price :")
    Expense_Discription = input("Discribe your Expense  :")
    serial = len(Expense) + 1
    Expense.append(
        {
            "Sr.No": serial,
            "Expense Price : ": Expense_price,
            "Expense Discription :": Expense_Discription,
        }
    )
    print("Expenses add Successfully")  # we append the the all assin value in the list


# def add_more_Expenses(): #to add more expense in the list we ddd this function
#  def


def view_expenses():
    print(Expense)


def delete_expenses():
    expense_no = int(input("Entre the expense serial no you want ro delete"))
    for idx, Expense in enumerate(Expense):
        if Expense["Sr.No"] == expense_no:
            Expense.pop(idx)
            print("Expense Deleted Successfully")
            break


# def delete_all_task():
#     expense


# Expense tracker Entry
while True:
    print(
        "___________________________________Welcome to Expense tracker__________________________________"
    )
    print("1. For enter the epenses press 1 :")
    print("2. for View the expenses press 2 :")
    print("3. for delete the expenss press 3 :")
    print("4. Press the 4 for delete all Expenses: ")
    print("5. press 5 for exit :")
    x = int(
        input("Entre the task you want to perform :")
    )  # here we define the funtion to entre the value from user

    if x == 1:
        print("Enter your Expense")
        expenses_tracker()
        update_file()
        # add_more_Expenses()
    elif x == 2:
        print("View your Expenses")
        view_expenses()
    elif x == 3:
        print("Delete the Expenses")
        delete_expenses()
        update_file()
    elif x == 4:
        print("Thankyou for chooshing this app")
        break
