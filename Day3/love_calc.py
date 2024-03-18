print("The Love Calculator is calculating your score...")
name1 = input('What is your name? ')
name2 = input('What is their name? ')
# # 🚨 Don't change the code above 👆
# Write your code below this line 👇

def countLettersInName(word, letters):
    count = 0
    wordLower = word.lower()
    lettersLower = letters.lower()
    for l in lettersLower:
        count += wordLower.count(l)
    return count

bothNames = name1 + name2
trueCount = countLettersInName(bothNames, 'true')
loveCount = countLettersInName(bothNames, 'love')
score = int(str(trueCount) + str(loveCount))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score > 40 and score < 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
