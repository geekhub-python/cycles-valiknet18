listOfChars = []
numberCharsInLine = 0
line = ""

for key in range(97, 123):
    if numberCharsInLine == 5:
        numberCharsInLine = 0
        listOfChars.append(line)
        line = ""
    line += " " + chr(key)
    numberCharsInLine += 1


for line in listOfChars:
    print(line)

