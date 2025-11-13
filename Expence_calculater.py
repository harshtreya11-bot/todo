class Expense:
    expenses = []
    def Expences_data_holder(self,price,Discription):
        self.price = price
        self.Discription = Discription

    
       
#The Expence Calculater app which Calculate the expences and show your all expences 
print("Welcome to Expence Collector")
while True :
    price = int(input("Entre the price "))
    Discription = (input("Discribe your ecpences"))
    expenses.append(price,Discription)



# class Expense:
#     expenses = []

#     def __init__(self, price, description):
#         self.price = price
#         self.description = description

#     @classmethod
#     def add_expense(cls, price, description):
#         cls.expenses.append(Expense(price, description))

#     @classmethod
#     def show_expenses(cls):
#         print("\nAll Expenses:")
#         for i, exp in enumerate(cls.expenses, start=1):
#             print(f"{i}. Price: {exp.price}, Description: {exp.description}")

# print("Welcome to Expense Collector")

# while True:
#     try:
#         price = int(input("Enter the price: "))
#         description = input("Describe your expense: ")
#         Expense.add_expense(price, description)
#         more = input("Add another expense? (yes/no): ").lower()
#         if more != 'yes':
#             break
#     except ValueError:
#         print("Invalid price. Please enter a number.")

# Expense.show_expenses()


    
    

    




