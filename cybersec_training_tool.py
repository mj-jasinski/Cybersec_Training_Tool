# Cybersecurity training tool by Marcin Jasinski.
# Focuses on ports and acronyms.
# It is an edutainment tool.
# It will be helpful for a Cybersecurity (SOC) Analyst.
# Inspired by preparations for CompTIA CySA+ certification.
# Version beta, release date 27/10/2024.


import time
import os
import shutil
import random
import csv

from datetime import datetime


def greeter():
    '''Display intro message for the tool, collect user's name. 
    Provide instructions on how to use the tool.'''

    msg_1 = 'Hi, Welcome to version beta of Cybersec Training Tool by MJJ.' 
    msg_2 = 'By using this tool you\'ll practice/learn ports, acronyms;'
    msg_3 = 'and become a better Cybersecurity Analyst.'
    msg_4 = 'Prerequisites: knowledge at the level of CompTIA A+, Network+, Security+.'
    msg_5 = 'The Author hopes you enjoy the ride!'
    decor = '#' * 90
    print(f'\n{decor}\n\n{msg_1.center(90)}\n\n{msg_2.center(90)}\n{msg_3.center(90)}\n{msg_4.center(90)}\n{msg_5.center(90)}\n\n{decor}\n')
    # set user_name var to global as for any function in program its value will remain the same
    # and will need to be accessed by many functions within the program
    global user_name
    # get user name, remove potential whitespaces, change it to lowercase
    user_name = input('What is your name matey: ').strip().lower()
    print(f'Cool {user_name.upper()}, I can see you are raring to go!\n')
    print('''OK, here\'s how it works: 
          The tool displays TCP/UDP port number, or an acronym question. 
          The user enters answer.
          Answers can be case-insensitive.
          20 questions per session.\n''')
    time.sleep(4)
    print('### EXAMPLES ###')
    print('What is TCP 502? <type answer (Modbus), press "Enter">')
    print('What is IGMP? <type answer (Internet Group Management Protocol), press "Enter">\n')
    print('NB Don\'t be too serious ;) as this is an edutainment tool!\n\n')


def initialiser():
    '''Set up the environment for the tool. Create Cybersec_Training_Tool directory if it doesn't exist.
    Change to training tool directory. Move ports_acronyms csv file to this dir from Downloads,
    if not present in this dir. Display initislisation progress with delays and celebratory messages.'''
    
    home_dir = os.path.expanduser('~')
    current_dir = os.getcwd()
    # change to user's home dir if not currently there
    if current_dir != home_dir:
        os.chdir(home_dir)
    # create tool folder if it doesn't exist in user's home dir
    if not os.path.isdir('Cybersec_Training_Tool'):
        os.mkdir('Cybersec_Training_Tool')
    os.chdir('Cybersec_Training_Tool')
    # move content master file to training tool folder if not there
    if not os.path.isfile('ports_acronyms.csv'):
        downloads_dir = home_dir + '\\Downloads'
        file_path = downloads_dir + '\\ports_acronyms.csv'
        shutil.move(file_path, 'ports_acronyms.csv')
    time.sleep(4)
    print('Initialising, please wait ...\n')
    time.sleep(5)
    no_of_dots = [90, 65, 40, 20, 15, 11, 6, 1]
    for x in no_of_dots:
        print('.' * x)
        if x >=40:
            time.sleep(2)
        else:
            time.sleep(1)
    print('\nPOP!')
    print('\nWHIZZ!')
    print('\nBANG!\n')


def tester():
    '''Create test content from master ports acronyms file.
    Deliver test, throw in randomly chosen motivators. Display 'half way through the test' message.
    Return score, incorrect answers, questions for them and what answers should be.'''

    with open ('ports_acronyms.csv', 'r') as master_file:
        csv_reader = csv.reader(master_file, delimiter=';')
        # skip first three lines of master file, as they contain 'bad data'
        next(csv_reader)
        next(csv_reader)
        next(csv_reader)
        # create empty lists
        ports_acronyms = []
        answers = []
        # create a counter for how many ports are in a master file
        number_of_ports = 0
        # then add all items to lists (master lists)
        for line in csv_reader:
            port_acr, answer = line[0], line[1]
            # check if there is any port number in a line
            if any(chr.isdigit() for chr in port_acr):
                number_of_ports += 1
            ports_acronyms.append(port_acr)
            # strip a leading space before 2nd item in a line in csv file
            answers.append(answer.strip())
        # disregard 'C2' as it is the only acronym containing a digit
        # so adjust counter of ports in a master file
        number_of_ports -= 1
    
    # create lists with indexes of ports and indexes of acronyms
    # ports are listed before acronyms in a master file
    indexes_ports = [n for n in range(number_of_ports)]
    indexes_acronyms = [n for n in range(int(number_of_ports), int(len(ports_acronyms)))]
    # choose random 8 port indexes and 12 acronym indexes
    rand_indxs_ports = random.sample(indexes_ports, 8)
    rand_indxs_acronyms = random.sample(indexes_acronyms, 12)
    # combine two lists to get 20 indexes to choose items from master list
    indexes = rand_indxs_ports + rand_indxs_acronyms

    score = 0
    failed_indexes = []
    incorrect_answers = []
    iteration = 0
    motivators = ['Keep going!', 'Dig in!', 'You are smashing it!', 'Go hard or go home!',\
                  'When going gets tough, the tough get going!', 'Hard work pays off!',\
                  'The more sweat at a training ground, the less bloodshed on a battlefield!',\
                  'Good effort in, great results out!', 'Have fun!', 'Try harder!',\
                  'Having fun?', 'You can do it!', 'You\'ve got to put the reps in!',\
                  'Onwards and upwards!', 'Sweat now, shine later!', 'No pain, no gain!']
    # get 4 random motivators from the motivators list
    random_motivators = random.sample(motivators, 4)
    
    # generate 4 random testing loop iteration numbers when to throw in motivators
    # for iterations from 2 to 18 incl.
    runs = [n for n in range(2,19)] 
    random_iterations = random.sample(runs, 4)

    for index in indexes:
        answer = input(f'\nWhat is {ports_acronyms[index]}? ')
        # clean user's input
        answer = answer.strip().lower()
        correct_answer = answers[index]
        if answer == correct_answer.lower():
            score += 1
        else:
            incorrect_answers.append(answer)
            failed_indexes.append(index)
        iteration += 1
        if iteration == random_iterations[0]:
            print(f'** {random_motivators[0]} **')
            time.sleep(1)
        if iteration == random_iterations[1]:
            print(f'** {random_motivators[1]} **')
            time.sleep(1)
        if iteration == random_iterations[2]:
            print(f'** {random_motivators[2]} **')
            time.sleep(1)
        if iteration == random_iterations[3]:
            print(f'** {random_motivators[3]} **')
            time.sleep(1)
        if iteration == 10:
            half_way_msgs = ['HALF WAY POINT IS NOW!', 'YOU\'RE DOING GREAT, AT HALF WAY POINT NOW!',
                             'LOVING IT OR HATING IT? HALF WAY THROUGH IT.', 
                             'HALF WAY THROUGH THE TEST!\nYou\'re doing well! How well? Well, you\'ll find out after the test.']
            print(f'** {user_name.title()}, {random.choice(half_way_msgs)} **')
            time.sleep(2)

    failed_ports_acronyms = []
    correct_answers = []
    for index in failed_indexes:
        port_acr = ports_acronyms[index]
        failed_ports_acronyms.append(port_acr)
        correct_answer = answers[index]
        correct_answers.append(correct_answer)

    return score, incorrect_answers, failed_ports_acronyms, correct_answers


def evaluator_trainer():
    '''Call tester function. Display and evaluate result. Create a csv record file if non-existent. 
    Write user's name, result and date to record file. Display some performance stats. 
    Provide feedback.'''
    
    # call tester fctn, unpack items it returns
    score, incorrect_answers, failed_ports_acronyms, correct_answers = tester()

    # display countdown and result
    print(f'\n\n{user_name.title()}, the quiz is over.')
    msg_1 = 'Drum roll!'
    decor = '#' * 90
    print(f'\n\n{decor}\n\n{msg_1.center(90)}\n')
    counts = ['** 3 **', '** 2 **', '** 1 **']
    for count in counts:
        print(f'{count.center(90)}')
        time.sleep(1)
    msg_2 = 'Now, the moment of TRUTH.'
    print(f'\n{msg_2.center(90)}\n')
    time.sleep(2)
    msg_4 = f'Your SCORE is {score} out of 20.'
    print(f'{msg_4.center(90)}\n')
    print(f'{decor}\n')
    
    # evaluate score
    if score >= 19:
        performance = 'brilliant!'
    elif score >= 15:
        performance = 'very good!'
    elif score >= 12:
        performance = 'quite good.'
    else:
        performance = 'not so good, keep working on it.'
    print(f'Your performance at this test today was {performance.upper()}')
    time.sleep(3)

    today = datetime.now()
    todays_date = today.date()

    # fields to be used in csv record file
    fields = ['name', 'score', 'date']
    # create record file if non-existent and write a header of it
    if not os.path.exists('results_record.csv'):
        with open('results_record.csv', 'w', newline='') as all_scores:
            csv_writer = csv.DictWriter(all_scores, fieldnames=fields, delimiter=',')
            csv_writer.writeheader()

    # append details of today's test to record file
    entry = {'name': user_name, 'score': score, 'date': todays_date}
    with open('results_record.csv', 'a+', newline='') as all_scores:
        csv_writer = csv.DictWriter(all_scores, fieldnames=fields)
        csv_writer.writerow(entry)

    # read user's tests' details from record file, calculate no of tests taken
    with open('results_record.csv', 'r', newline='') as all_scores:
        csv_reader = csv.DictReader(all_scores)
        no_of_tests = 0
        for line in csv_reader:
            if line['name'] == user_name:
                no_of_tests += 1
     
        # calculate and display stats, if user has taken the test at least twice
        if no_of_tests >= 2:
            all_scores.seek(0, os.SEEK_SET)
            csv_reader = csv.DictReader(all_scores)
            total_all_scores = 0
            unique_scores = set()
            for line in csv_reader:
                if line['name'] == user_name:
                    total_all_scores += int(line['score'])
                    unique_scores.add(int(line['score']))
            
            max_score = max(unique_scores)
            avg_score = round((total_all_scores / no_of_tests),2)

            all_scores.seek(0, os.SEEK_SET)
            csv_reader = csv.DictReader(all_scores)
            dates_of_max_score = []
            for line in csv_reader:
                if line['name'] == user_name and line['score'] == str(max_score):
                    max_d = line.get('date')
                    dates_of_max_score.append(max_d)

            print('\n\nNB all info below includes today\'s test.')
            print(f'\nYour average score is: {avg_score}')
            print(f'\nNo of tests done so far: {no_of_tests}')
            print(f'\nYour max score is: {max_score} and was/were achieved on:')
            for day in dates_of_max_score:
                print(f' # {day}')
            print('\nAll unique scores so far: ')
            asc_unique_scores = sorted(unique_scores)
            for score in asc_unique_scores:
                print(f' # {score}')
            time.sleep(7)
    
    # deliver teaching component if there were any incorrect answers
    if incorrect_answers:
        msg_1 = 'A BIT OF TEACHING NOW'
        decor = '#' * 90
        print(f'\n\n{decor}\n\n{msg_1.center(90)}\n\n{decor}\n')
        for port_acr, correct_answer, wrong_answer in zip(failed_ports_acronyms, correct_answers, incorrect_answers):
            print(f'{port_acr} is {correct_answer}. \nYour answer was: \'{wrong_answer}\'.\n')
            time.sleep(3)


def finalizer():
    '''Display a closing message.'''

    msg_1 = f'Thank you {user_name.title()}!' 
    msg_2 = 'I hope you find this tool useful and have learnt something.' 
    msg_3 = '** Remember: PRACTICE MAKES PERFECT! **'
    msg_4 = 'Feedback will be appreciated!'
    msg_5 = 'linkedin.com/in/marcin-jasinski-cyber'
    msg_6 = 'martin.j.jasinski@gmail.com'
    msg_7 = 'github.com/mj-jasinski'
    decor = '#' * 90
    print(f'\n{decor}\n\n{msg_1.center(90)}\n\n{msg_2.center(90)}\n{msg_3.center(90)}\n\n{msg_4.center(90)}\n{msg_5.center(90)}\
          \n{msg_6.center(90)}\n{msg_7.center(90)}\n\n{decor}\n')


greeter()
initialiser()
evaluator_trainer()
finalizer()