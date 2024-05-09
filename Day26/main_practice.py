
from random import randint

list = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [n + 12 for n in list]
print(list2)

word = "everything"
# navy_word = [navy[e] for e in word]
# print(navy_word)

range_list = [n * 2 for n in range(1, 20) if n % 2 == 0]
print(range_list)

names = ["Dave", "Richard", "Mary", "Antonius", "Bob", "Stephen"]

names2 = [name.upper() for name in names if len(name) > 4]
print(names2)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared = [n * n for n in numbers]
print(squared)

input = "1, 1, 2, 3, 5, 8, 13, 21, 34, 55".split(',')
nums = [int(c) for c in input]
result = [n for n in nums if n % 2 == 0]
print(result)

names = ["Dave", "Richard", "Mary", "Antonius", "Bob", "Stephen"]

dict = {name: randint(50, 100) for name in names}
print(dict)

# adj = { name: val - 5 for (name, val) in dict.items()}
# print(adj)

passed = { name: val for (name, val) in dict.items() if val > 80 }
print(passed)


