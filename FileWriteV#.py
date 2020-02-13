import re

import banner

from datetime import datetime

import os

import SimpleAnimation

# stored for post-run to give total run-time
startTime = datetime.now()


Invalid_Phone_Number_Exp = r'^(?![( ](\d{3})[)][ ](\d{3})[-](\d{4})$|(\d{3})[. ](\d{3})[.-](\d{4})$|(?<!\d)\d{10}(?!\d)).*$'

mil_file = open('C:\\Users\\eliana.lopez\\OneDrive - JANUS Research Group, LLC\\RealisticExtrema.txt')

# For every line in the large phone number file, enumerate the lines 0-___. If the line number is divisible by the selected constant, then print out a progress report of the added invalid phone numbers and then empty the list. That way every time it reaches a divisible number, the program prints the most recently collected invalid phone numbers since the last print of invalid phone numbers. If the number is a match to the regex line, then append the phone number to the invalid input list, and append the line number as well. This makes it possible to print out both the line number and invalid phone number for easier understanding of the data being seen.
invalid_input = open("InvalidNumbers.txt", "w+")


def EnumeratedInspector():
    banner.Title()

    SimpleAnimation.load_animation()

    for lineNumber, line in enumerate(mil_file):

        z = re.match(Invalid_Phone_Number_Exp, line)

        # if the line contents are a match, attach them to invalid_input_list with the corresponding line number.
        if z:
            invalid_input.write(str(lineNumber) + ' ')

            invalid_input.write(line)

        # if a key on the keyboard is touched, the program terminates

    else:

        pass


# Runs the EnumeratedInspector function that was created above.
EnumeratedInspector()

# shows ascii DONE!! to how program is done processing the phone numbers.
banner.DoneBanner()

# Prints the time it took to run and finish the program.
print("The program took " + str((datetime.now() - startTime)) + " minutes to run. ")

everyMatch = input("Would you like to see every match? (y)yes (n)no >> ")

if everyMatch == 'y':

    # opens the file in notepad.
    os.startfile('InvalidNumbers.txt')
    banner.Quit()
    quit()

if everyMatch == 'n':
    banner.Quit()
    quit()
else:
    pass
