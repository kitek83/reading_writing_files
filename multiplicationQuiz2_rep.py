import time, random
import pyinputplus as pyip
correctAnswer = 0
nrOfQuestions = 10
for questionNr in range(nrOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    multip = '%s=%sx%s enter the reult:' % (questionNr+1,num1,num2)

    try:
        pyip.inputStr(multip,allowRegexes=['^%s$' % (num1*num2)],blockRegexes=[('*','Incorrect!')], timeout=5, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        correctAnswer += 1
        print('Great!Correct answer!')
        time.sleep(1)
print('Correct answers: %s / Number of questions: %s' % (correctAnswer,nrOfQuestions))
