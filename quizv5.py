class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer


print("This is a multiple choice quiz you can create for someone else!")
print("You will be prompted to enter the questions, possible answers, and correct answers. \n")

while True:
    try:
        num_questions = int(input("How many questions long would you like your quiz to be?"))
        break
        while int(num_questions) <= 0:
            if num_questions == 0:
                print("Really? You want a quiz with 0 questions?")
            else:
                print("How do you have a quiz with a negative number of questions?")
            num_questions = int(input("How many questions long would you like the quiz to be?"))
    except ValueError:
        print("Please enter an integer")

questions = []

for i in range(num_questions):
    Q = input("Enter Question #" + str(i+1)+":")
    Q_A = input("Enter A):")
    Q_B = input("Enter B):")
    Q_C = input("Enter C):")
    Q_D = input("Enter D):")
    Q_Answer = input("Is A, B, C, or D the correct answer?")
    Q_Answer = Q_Answer.upper()
    while Q_Answer != "A" and Q_Answer != "B" and Q_Answer != "C" and Q_Answer != "D":
        print("Error. Please make sure to input a letter from A-D. Try again.")
        Q_Answer = input("Is A, B, C, or D the correct answer?")
        Q_Answer = Q_Answer.upper()
    choice_list = [Q_A, Q_B, Q_C, Q_D]
    questions.append(Question(Q, choice_list, Q_Answer))


retake_test = input("Can the test-taker retake your test?")
while retake_test.upper() != "YES" and retake_test.upper() != "NO":
    print("Please give a yes or no response")
    retake_test = input("Can the test-taker retake your test?")

if retake_test.upper() == "YES":
    while True:
        try:
            retake_num = int(input("How many times can the test-taker retake the test?"))
            break
        except ValueError:
            print("Please enter an integer")
    while retake_num <= 0:
        if retake_num == 0:
            print("How can you retake the test zero times?")
        else:
            print("How can you retake the next negative times?")
        retake_num = int(input("How many times can the test-taker retake the test?"))
    retake_test = True
else:
    retake_num = 0
    retake_test = False

print("\nTime for someone to take your quiz!")
print("For ever question, enter a letter from A-D\n")


def run_test(question_set):
    score = 0
    q_num = 0
    for question in question_set:
        q_num += 1
        guess = input("Question #" + str(q_num) + ": " + str(question.prompt) + "\nYour choices are:\nA): " +
                      str(question.choices[0]) + "\nB): " + str(question.choices[1]) + "\nC): "
                      + str(question.choices[2]) + "\nD): " + str(question.choices[3]) + "\n")
        if guess.upper() == question.answer:
            score += 1
    percent = round(score/len(question_set)*100)
    print("You got", str(score), "out of", str(len(question_set)), "correct! \nThat is a " + str(percent) + "%\n")


run_test(questions)

if not retake_test:
    print("The quiz is completed. Thank you for playing!")
    exit()
else:
    if retake_num == 1:
        time = "time"
    else:
        time = "times"
    print("The person who made your test allows you to retake the test a maximum " + str(retake_num) + " " + time)


def retake(retake_bool, num_retake):
    times_retaken = 1
    while retake_bool and times_retaken <= num_retake:
        retake_string = ""
        while retake_string.upper() != "YES" and retake_string.upper() != "NO":
            retake_string = input("Would you like to retake the same test?")
            if retake_string.upper() == "YES":
                print("Time to take the same quiz!\n")
                run_test(questions)
                print("That was retake #" + str(times_retaken))
                times_retaken += 1
            elif retake_string.upper() == "NO":

                retake_bool = False
                print("Thank you for playing!")
                exit()
            else:
                print("Please give a yes or no response:")
        print("Your retakes are over. Thank you for playing!")


retake(retake_test, retake_num)
