year = int(input('Enter a year: '));

isLeapYear = False;
if year % 4 == 0:
    isLeapYear = True;
    if year % 100 == 0:
        isLeapYear = False;
        if year % 400 == 0:
            isLeapYear = True;

if isLeapYear:
    print('Leap year');
else:
    print('Not leap year');
