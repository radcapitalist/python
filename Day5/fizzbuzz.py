
# Write your code here 👇

for num in range(1, 101):
  fizz = num % 3 == 0
  buzz = num % 5 == 0
  if fizz and buzz:
    print("FizzBuzz")
  elif fizz:
    print("Fizz")
  elif buzz:
    print("Buzz")
  else:
    print(num)