import random
import time
import pyttsx3
# Create a game Cow and Bull
random_number = str(random.randint(10,20))

number_guesses = 0

def check_guess(guess):
  global number_guesses
  number_guesses += 1

  Cow = 0
  Bull = 0

  for i in range(2):
    if guess[i] == random_number[i]:
      Cow += 1
    elif guess[i] in random_number:
      Bull += 1

  if Cow == 2:
        #time.sleep
    for second in range(3,0,-1):
        print(second)
        time.sleep(0.5)
    print("You are the winner"+" "+ " !>_<!"+"\nỜ Mây Zing Gut Chop Em"+ " " + ">^-^<")
        
    #Ro_bot say " "
    robot_brain="You are a winer...Ờ Mây Zinh Gút Chóp  Em"

    robot_mouth = pyttsx3.init()
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
  else:
    print(f"{Cow} Cows, {Bull} Bulls")

user_guess = input("Mời bạn dự đoán số trong khoảng 10-20: ")

while True:
  if user_guess == random_number:
    break
  else:
    check_guess(user_guess)
    print("Guess again:")
    user_guess = input("Mời bạn dự đoán số trong khoảng 10-20: ")


check_guess(user_guess)
