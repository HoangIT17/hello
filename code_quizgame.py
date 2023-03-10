import pyttsx3

#--------------------------------------

def quiz_game():
    guesses=[]
    correct_guesses=0
    question_num=1
    for key in questions:
        print("--------------------------------------")
        print(key)
        for i in opptions[question_num-1]:
            print(i)
        guess=input("Enter Your Answer (A,B,C or D): ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses +=check_answers(questions.get(key),guess)

        question_num+=1
        display_score(correct_guesses,guesses)
        

        
            
    #--------------------------------------
def check_answers(answer,guess):
    if answer==guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

#--------------------------------------
def display_score(correct_guesses,guesses):
    print("--------------------------------------")
    print("RESULTS")
    print("--------------------------------------")
    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score=int((correct_guesses)/len(questions)*100)
    print("Your Score: "+ str(score) +"%")

    
#--------------------------------------
def play_again():
    
    response=input("Would you like to play again? (Y/N): ")
    response.upper()
    if response=="Y":
        return True
    else:
        return False


#--------------------------------------


questions = {
    "1, Ai là người phát minh ra trò chơi này": "C",
    "2, Who is created Python planguage?":"B",
    "3, When was the Python programming language created?":"C",
    "4, Which country is the largest in the world?" :"D",
    "5, Which country is the most populous in the world?" :"A"
}

opptions = [
    ["A. Google", "B. Develop", "C. Hoang", "D. Tesla"],
    ["A. Elon Musk", "B. Guido Van Rossum", "C. Mark Zuckerburg", "D. Pitago"],
    ["A. 12-1990", "B. 5-1991", "C. 2-1991", "D.7/1995"],
    ["A. America", "B. France", "C. China", "D. Russia"],
    ["A. India", "B. Chine", "C. America", "D. Russia"]]

quiz_game()
while play_again():
    quiz_game()

print("Thanks for playing with me!")

robot_brain="Thanks for playing with me!"
robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()