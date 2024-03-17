print('Welcome to the tip calculator!');
bill = float(input('What was the total bill? '))
percent = float(input('What percentage would you like to tip, as a whole number? '))
splits = int(input('How many people are splitting the check? '))
if splits == 0:
    print("You can't split a bill amongst 0 people.")
else:
    # Compute the total including tip
    total = bill + (bill * (percent / 100))
    each = round(total / splits, 2)
    each_str = "{:.2f}".format(each);
    print(f"Each person should pay: ${each_str}")
