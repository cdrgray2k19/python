from random import randint
from os import system
import time

'''short and formal quiz.'''



name = input('What is your name?\n')
print('Welcome', name + '!\n')

QnA_Dict = {'What does CPU stand for?': 'central processing unit', 'What does RAM stand for?': 'random access memory', 'What does SSD stand for?': 'solid state drive', 'What does ROM stand for?\nA: read only mentioning\nB: read only memory\nC: reliable ordinary machine': 'b'}

while True:

    mark = 0

    question_number = 1

    questions = []

    answers = []

    for i in QnA_Dict.keys():
        questions.append(i)

    for i in QnA_Dict.values():
        answers.append(i)

    while questions:

        number = randint(0, len(questions) - 1)
        current_Q = questions[number]
        current_A = answers[number]

        questions.pop(number)
        answers.pop(number)

        ask = input('Question ' + str(question_number) + ':\n' + current_Q + '\n\nAnswer:\n').lower()

        if ask == current_A:
            print('\nCorrect, well done!\n')
            mark += 1
        else:
            print('\nIncorrect, the answer was', current_A)

        question_number += 1
        time.sleep(2)
        system('clear')

    print('Thank you for taking the quiz.\n')
    print('Your mark:', str(int(float(mark/(len(QnA_Dict)))*100)) + '%\n')

    again = input('Would you like to take the quiz again? If so press 1.\n')
    if again == '1':
        system("clear")
        print('Welcome back', name + '!\n')
    
    else:
        print('\nGoodbye', name + ', thank you for playing!')
        break