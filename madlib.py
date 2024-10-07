"""
Name: Kaden Meir
Date: 10/3/24
Description: Mad Lib project
"""

person_name = input("What is your name?:")
players_date = input("What is the date?:")


# At least 5 nouns, 5 verbs, 3 adjectives, and 2 adverbs.
noun_1 = input("I need a noun (place):")
noun_2 = input("I need a noun (person or thing):")
noun_3 = input("I need a noun:")
noun_4 = input("I need a noun (place):")
noun_5 = input("I need a noun:")

verb_1 = input("I need a verb:")
verb_2 = input("I need a verb:")
verb_3 = input("I need a verb:")
verb_4 = input("I need a verb:")
verb_5 = input("I need a verb:")

adjective_1 = input("I need a adjective:")
adjective_2 = input("I need a adjective:")
adjective_3 = input("I need a adjective:")

adverb_1 = input("I need a adverb:")
adverb_2 = input("I need a adverb (manners):")

print(f"Name:{person_name.title()}")

print("Today\'s Date is {players_date}")

print(f"We start off this story in {adjective_1} {noun_1} with a very {adjective_2} and {adjective_3} {noun_2}. We are here to watch {noun_3} {verb_1} really fast, but in the mean time
\n we should {verb_2} to {noun_4} because I forgot to get food for dinner. We got to {noun_4} were we {adverb_1} walked around the place. The place reminded me of {noun_5} because
\n you could {verb_3} and {verb_4} all around the place. After exploring {noun_4} we {adverb_2} {verb_5} to the event, so we could watch {noun_3} {verb_1}.")
