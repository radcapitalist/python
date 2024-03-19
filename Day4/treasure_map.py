line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letters = ['A', 'B', 'C'];
uc_pos = position.upper()
if uc_pos[0] in letters:
    x = letters.index(uc_pos[0])
else:
    print(f'"{uc_pos[0]}" is not a valid map X-coordinate, must be in {letters}')
    raise SystemExit

y = int(uc_pos[1]) - 1
if y < 0 or y > 2:
    print(f'"{uc_pos[1]}" is not a valid map Y-coordinate, must be 1-3')
    raise SystemExit

map[y][x] = 'X';

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
