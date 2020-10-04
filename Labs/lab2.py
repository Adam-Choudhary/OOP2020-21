# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: Adam Choudhary
# date: 02-10-2020
# purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: " + message)

        #
        # Enter your own print statements below:
        #

        # print only first and last of the sentence:
        print("\nFirst character: " + message[0] + "\nLast character: " + message[-1])

        # use slice notation:
        print("The last two characters are:", message[1:3])

        # escaping a character:
        print("He said \"that's fantastic!\"")

        # find all a's in the input word and count how many there are:
        print("The Number of occurrences of character 'a': " + str(message.count('a')))

        # replace all occurrences of the character a with the - sign
        print("Replacing all occurrences of the character 'a' with the '-' sign " + message.replace('a', '-'))

        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        # Answer: received an error saying that strings do not support replacements


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: " + message)

        # hand the input string to a list and print it out:

        my_list = list(message.split())
        print(my_list)

        # append a new element to the list and print:
        my_list.append("Test")
        print(my_list)

        # remove from the list in 3 ways:

        # my_list.remove(my_list[0])
        # my_list.pop(0)
        # del(my_list[0])

        print(my_list)
        # check if the word cake is in your input list:
        if "cake" in my_list:
            print("The word cake is in the list")
        else:
            print("The word cake is not in the list")

        # reverse the items in the list and print:
        list.reverse(my_list)
        print(my_list)

        # reverse the list with the slicing trick:
        print(my_list[::-1])


        # print the list 3 times by using multiplication:
        print(my_list*3)

tas = Types_and_Strings()
# tas.play_with_strings()
tas.play_with_lists()
