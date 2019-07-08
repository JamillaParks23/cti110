# CTI-110 
# P3HW2 - MealTipTax 
# Jamilla Parks 
# June 30, 2019
#Write a program that will calculate a 20% tip, 18%, and 15% and a 7% tax on a meal price.
#The user will enter the meal price and the program will calculate tip, tax, and the total.
#The total is the meal price plus the tip plus the tax.


#this function will print tip, tax, the mealprice, and #the total)
mealprice = float(input ('Enter the meal price: $'))
tip = mealprice * .15
tip = mealprice * .18
tip = mealprice * .20

def calc_tax(mealprice):
    tax = mealprice*.07

def calc_total(mealprice, tip, tax):
    total = mealprice + tip + tax

def print_info(mealprice, tip, tax, total):
    print ('The meal price is $:'), mealprice
    print ('The tip is $:'), tip
    print ('The tax is $:'), tax
    print ('The total is $:'), total
 
