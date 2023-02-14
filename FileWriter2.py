quizNum = 0
quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w') # this % symbol is a place holder for whatever will be placed after the % symbol 
quizFile.write("This is the first text written\n and the file has been created automatically")
quizFile.close()