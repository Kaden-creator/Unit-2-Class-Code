"""
Date: 9-16-24
Assignment: Unit 1 Lesson 1 Notes

"""


# Variables

message = "Hello, user"
print(message)

#snake_case
user_name = input("Enter your name: ")
user_id =int(input("Enter user id: "))

# variable type
#print(type(user_name))

# Strings
# Can use ' or " to indicate string - be consistent

# f-strings are formatted strings that help with combining string
# Way 1 to combine string use + (concatenation)
# Caution: all numbers have to have str() around them
message_one = "Welcome" + user_name + "with ID" + str(user_id)
print(message_one)

# The 2 - use f strings
# put variables in curly braces
message_two = f"Welcome {user_name} eith ID {user_id}"
print(message_two)

#possible errors
# apostrophes inside of single quotes
# resolution: use escape sequence \ - tells python next symbol is
# literally that thing, Pythonic meaning
famous_quotation = 'Quotations are hard to find in the middle of lessons - it\'s annoying. Mr Smith'

# raw strings
bird = r"""

             /'{>
         ____) (____
       //'--;   ;--'\\
      ///////\_/\\\\\\\
             m m
"""
print(bird)