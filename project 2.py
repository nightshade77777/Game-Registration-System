# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 16:10:01 2022

@author: SUHAANI
"""

'''
Task 1: Registering a new player
Players need to enter their personal details 
in order to enter the league.
Requirements
Here is an outline design for your program.
• Display a title stating: League registration.
• Ask the player to enter: first name, last name, nickname, and email address.
• Ask the player to enter a skill level, using E for ‘Expert’ or C for ‘Casual’.
• Display the player’s personal details on the screen.
• If the player entered E then ‘Expert’ should be displayed; if they entered C then
‘Casual’ should be displayed.
• Ask the player to confirm that all of the personal details are correct.
• If any detail is incorrect, ask the player to re-enter all of the personal details and
display them again.
• Return to the title message.
'''

print("League Registration ")
print()
class Details:
    def __init__(self, fname, lname, nickname, email):
        self.fname = fname
        self.lname = lname
        self.nickname = nickname
        self.email = email
    
    def show_details(self):
        print()
        print("Welcome! ")
        print(self.fname)
        print(self.lname)
        print(self.nickname)
        print(self.email)

fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")
nickname = input("Please enter your nickname: ")
email = input("Please enter your email: ")


register = Details(fname, lname, nickname, email)
register.show_details()
print()
print("Thank you! ")
print()

'''
Task 2: Calculating an entry fee
The program should calculate an entry fee for each player. 
This calculation should take
into account the skill level of the player.

The system should display the fee in the appropriate currency, using these exchange rates:
• £ sterling for all UK players; no exchange rate required
• £1 = 1.50 US dollars
• £1 = 2.00 AU dollars.

The entry fee will consist of:
• £10 per player
• an additional fee of £35 for ‘Expert’ players or £20 for ‘Casual’ players.

Fee calculator requirements
• The fee calculator should start with a welcome message.
• It should ask the user for the player’s:
• email address
• skill level (E for expert, C for casual)
• country (UK, US, AU).
• It should then calculate the entry fee.
• The fee should be displayed in the correct currency, using the following
abbreviations: USD, AUD, GBP.
• It should then ask if the user wishes to calculate another fee.

'''



DOLLAR_US = 1.50
DOLLAR_AU = 2.00
STANDARD = 10
EXPERT_FEE = 35
CASUAL_FEE = 20 

print()

print("The entry fee will consist of: ")
print("• £10 per player")
print("• an additional fee of £35 for ‘Expert’ players or £20 for ‘Casual’ .")
print()

print("Please choose from one of the skill level options. ")
print("[E] : Expert ")
print("[C] : Casual ")
print()


validated = "false"

while validated == "false":
    skill_level = input("Enter your skill level: ")
    if skill_level == "E" or skill_level == "e":
        print("Expert ")
        skill_level = "E"
        expert = STANDARD + EXPERT_FEE
        print()
        print("It will cost you: ", expert)
        validated == "true"
        break
    if skill_level == "C" or skill_level == "c":
        print("Casual ")
        skill_level = "C"
        casual = STANDARD + CASUAL_FEE
        print()
        print("It will cost you: ", casual)
        validated == "true"
        break
    else:
        print("Invalid input. Try again! ")
        skill_level = input("Enter your skill level: ")

print("Your registered skill level is: ", skill_level)
print()


print("Exchange rates: ")
print("£1 = 1.50 US dollars. ")
print("£1 = 2.00 AU dollars.")
print()
  
def menu():
    print("Please type in your country code (AU/UK/US) ")
    print("[AU]: Australia ")
    print("[UK]: United Kingdom ")
    print("[US]: United States ")

menu()

def fees():
    cost = 0
    flag = "false"
    
    while flag == "false": 
        country = input("Type in where you are from: ").upper()
        
        if country == "AU" and skill_level == "C":
            cost = casual * DOLLAR_AU
            print("Total cost: ", cost)
            flag = "true"
            break
        if country == "AU" and skill_level == "E":
            cost = expert * DOLLAR_AU
            print("Total cost: ", cost)
            flag = "true"
            break


        if country == "US" and skill_level == "C":
            cost = casual * DOLLAR_US
            print("Total cost: ", cost)
            flag = "true"
            break
        if country == "US" and skill_level == "E":
            cost = expert * DOLLAR_US
            print("Total cost: ", cost)
            flag = "true"
            break


        if country == "UK" and skill_level == "C":
            cost = casual
            print("Total cost: ", cost)
            flag = "true"
            break
        if country == "US" and skill_level == "E":
            cost = expert
            print("Total cost: ", cost)
            flag = "true"
            break
        
        else:
            print("Invalid. Try again! ")
            print()
            country = input("Type in where you are from: ").upper()



'''

'''
opener = open("firesideResults.txt", "r")
for line in opener:
    print(line)
opener.close











