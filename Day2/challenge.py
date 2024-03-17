# num_char = len(input("What is your name?\n"))
# print("Your name has " + str(num_char) + " characters.")

val = input("Give me a number, I'll add the digits: ");
strVal = str(val);
sum = 0;
for ch in strVal:
    sum += int(ch);

print("Sum of digits: " + str(sum));
