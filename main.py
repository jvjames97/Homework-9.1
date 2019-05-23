while True:
    print("Hello there! Welcome to this unit converter!")
    km = int(input("Please enter the number of km you want to convert into miles: "))
    miles = float(km * 0.621371)
    print(miles)
    user_answer = input("Would like to keep converting? ")
    if user_answer == "no" and user_answer != "yes":
        print("See you soon!")
        break
    else:
        input("Please say yes or no: ")