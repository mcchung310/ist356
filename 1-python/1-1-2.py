# Code Challenge 1-1-2 -> Let' write a program to divide up the check among diners in a party.

# Write a program to input the amount of a restaurant check, tip %, and number of diners
check_amount = float(input("Enter the amount of the check: ")) # Input for check amount
tip_percentage = float(input("Enter the tip percentage (as a whole number): ")) # Input
number_of_diners = int(input("Enter the number of diners: ")) # Input for number of diners

#AI Ask: I would like you to account for negative inputs. None of the values input should be <0 and print an error message. 
# None of the input values should be negative.
if check_amount < 0 or tip_percentage < 0 or number_of_diners < 0:
	print("Error: input values cannot be negative.")
else:
	# The program should output the total amount with tip, and the amount each diner owes.
	total_amount = check_amount + (check_amount * (tip_percentage / 100)) # Calculate total amount with tip
	amount_per_diner = total_amount / number_of_diners # Calculate amount per diner

	print(f"The total amount with tip is: ${total_amount:.2f}") # Output total amount with tip
	print(f"Each diner owes: ${amount_per_diner:.2f}") # Output amount
