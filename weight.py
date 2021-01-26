# weight.py
# A program to convert kiligrams to pounds
# Written by Sarah Doyle

def main():
    kilograms = eval(input("What is the weight in kilograms? "))
    pounds = 2.2046226218 * kilograms
    print("The weight is", pounds, "pounds.")
main()
