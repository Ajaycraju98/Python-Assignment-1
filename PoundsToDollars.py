# 10.Name your file: PoundsToDollars.py Write a program that asks the user to enter an amount in pounds (£)
# and the program calculates and converts an amount in dollar ($)
# An example runs of the program: Please enter amount in pounds: XXX £ XXX are $ XXX

Amount=float(input('please enter amount in pounds:'))
convert=Amount*1.27   #1 Pound=1.27 dollars
print('\u00A3',Amount,'are $',convert)