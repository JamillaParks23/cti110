# Get the projected total sales.
# June 18, 2019
# CTI-110 P2T1 - Sales Prediction
# Jamilla Parks
#
#Input the total sales
#Calculate the profit as 23 percent
#Display the profit
#Get the projected total sales.
total_sales= float(input('Enter the projected sales:'))

#Calculate the profit as 23 percent of total.
profit= total_sales * 0.23

#Display the profit.
print('The profit is $', format(profit,',.2f'))
