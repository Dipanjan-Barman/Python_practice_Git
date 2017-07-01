#!/usr/bin/env python3
from datetime import date

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
multi_print = int(input("Enter the no of times you want to print the message: "))
currentYear = date.today().year

year100 = (currentYear - age + 100)
print(multi_print * (name + " will be 100 years old in the year " +
str(year100) + "\n" ))

