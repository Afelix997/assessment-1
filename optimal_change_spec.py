from optimal_change import optimal_change


print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

print("3:", optimal_change(2, 300) == "The optimal change for an item that costs $2 with an amount paid of $300 is 2 $100 bills, 1 $50 bill, 2 $20 bills, 1 $5 bill, and 3 $1 bills.")

print("4:", optimal_change(76.10, 76.11) == "The optimal change for an item that costs $76.1 with an amount paid of $76.11 is 1 penny.")

print("5:", optimal_change(0,3) == "The item is Free! You will be refunded your $3.")

print("6:", optimal_change(3,0) == "Insufficent Funds.")

print("7:", optimal_change(100,100) == "Exact payment recieved. Have a good day!")