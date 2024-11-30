# 1.Write Python code that prints your name, student number and email address.
print ("Ajay")
print("ST10A")
print("ajaycraju98@gmail.com")

# 2.Write Python code that prints your name, student number and email address using escape sequences.
print ("Ajay\nST10A\najaycraju98@gmail.com\n")

# 3.Write Python code that add, subtract, multiply and divide the
# two numbers.You can use the two numbers 14 and 7

a= 14
b= 7
print(" 14+7=",a+b,"\n"" 14-7=",a-b,"\n",'14*7=',a*b,"\n",'14/7=',a/b)

# # 4.Write Python code that displays the numbers from 1 to 5 as steps.
# # # An example runs of the program: 1 2 3 4 5
print ("1\n2\n3\n4\n5\n")

# 5 Write Python code that outputs the following sentence
# (including the quotation marks and line break) to the screen
# "SDK" stands for "Software Development Kit", whereas
# "IDE" stands for "Integrated Development Environment".

print('"SDK" stands for "Software Development Kit",whereas \n"IDE" stands for "Integrated Development Environment".')

# 6.Practice and check the output
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# 7.Define the variables below.Print the types of each variable
# What is the sum of your variables? (Hint: use a type conversion function.)
# What datatype is the sum?
num = 23
textnum = "57"
decimal = 98.3

print(type(num))
print(type(textnum))
print(type(decimal))
sum_result=num+int(textnum)+decimal
print(sum_result)
print("data type",type(sum_result))

# 8.calculate the number of minutes in a year using variables for each unit of time.
# print a statement that describes what your code does also.
# Create three variables to store no of days in a year, minute in a hour, hours in a day,
# then calculate the total minutes in a year and print the values
# (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour

No_of_days_in_an_year=365
Hours_in_a_day=24
Minutes_in_an_hour=60
Total_number_of_minutes_in_an_year=No_of_days_in_an_year*Hours_in_a_day*Minutes_in_an_hour

print("This code calculates the total number of minutes in a year.")
print(f"Total no of minutes in a year = {No_of_days_in_an_year} days * {Hours_in_a_day} hours * {Minutes_in_an_hour} minutes")
print(f"Total no of minutes in a year: {Total_number_of_minutes_in_an_year}")

#9.Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
#An example runs of the program: Please enter you name: Tony Hi Tony, welcome to Python programming :)

name=input("Please enter your name:")
print("Hi {}".format(name),'welcome to python programming')

