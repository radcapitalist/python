
list= ['a', 'b', 'c']
try:
    print(list[5])
except FileNotFoundError:
    print("FileNotFoundException")
except IndexError as msg:
    print("Got an index error: ", msg)
else:  #This happens if there was not actually an exception
    print("Else block")
finally:
    print("finally block")

