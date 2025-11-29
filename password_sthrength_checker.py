#Check the Sthrength of a Password
common_passwords = ["123456", "Password", "password", "12345678","asdfghjkl", "qwertyuiop","zxcvbnm","1111111","abc123","password1","000000","Iloveyou","Qwertyuiop","1q2w3e4r5t","123123","Monkey","Dragon","654321"]

while True:
    x = str(input("Enter your password: "))
    length = len(x)
    if length<6:
        print("Weak password")
    elif x in common_passwords:
        print("Very Weak password")    
    elif length>=6 and length<10:
        print("Moderate password")
    else:
        print("Strong password")
    choice = input("Do you want to check another password? (yes/no): ")
    if choice.lower() != 'yes':
        break    
    else :
        continue
