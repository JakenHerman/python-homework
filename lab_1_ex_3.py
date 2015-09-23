#__author__: Jaken Herman
#__class___: COSC 2347
#_professor: Dr. Ji
#___date___: Aug 27, 2015

#
#       LAB/QUIZ PROBLEM 3
#

user_name = input("What is your name? ")
user_height_inches = eval(input("Please tell me your height in inches: "))
user_height_feet = (user_height_inches / 12)

print("Goodmorning " + user_name + ". You are " +
      str(user_height_feet)[0:1] + " feet and " +
      str(user_height_feet)[2:3] + " inches tall.")

