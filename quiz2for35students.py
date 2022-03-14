import random;

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne' }

for fileNr in range(35):
   questionFile = open(f'questionFile{fileNr + 1}.txt','w')
   answerFile = open(f'answerFile{fileNr + 1}.txt','w')
   questionFile.write(f'Name:\n\nDate:\n\nPeriod:\n\n'
                      f'                  State Capitals Quiz (Form{fileNr+1})\n\n')
   states = list(capitals.keys())
   random.shuffle(states)
   #remember about indentation
   #creating 50 questions with correct and wrong answers
   for questionNr in range(50):
      #correct asnwer
      correctAnswer = capitals[states[questionNr]]
      wrongAnswer = list(capitals.values())
      #delete correct answer from wrong answers
      del wrongAnswer[wrongAnswer.index(correctAnswer)]
      #choose only 3 wrong answers from the list
      wrongAnswer = random.sample(wrongAnswer,3)
      answerOption = wrongAnswer + [correctAnswer]
      random.shuffle(answerOption)

      #Writing questions to the question file
      questionFile.write(f'{questionNr+1}.Whats is the capital of the state {states[questionNr]}?\n')
      for i in range(4):
         questionFile.write(f"{'ABCD'[i]}.{answerOption[i]}\n")

      #Writing answers to the answer file.
      answerFile.write(f"{questionNr+1}.{'ABCD'[answerOption.index(correctAnswer)]}\n")



































