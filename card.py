# Marco Gonzalez
# CS 3035-01
# This program is an implementation of the Luhn algorithm and creating a GUI using the Tkinter module
# Changes made upon resubmission: Added arguments to the validation_label widget to change its background color
# green/red which is determined by if the user input is valid/invalid. Valid = Green; Invalid = Red

# Import the Tkinter module
from tkinter import *

# Set up the window of the GUI, setting up the windows title, window dimensions, and it's background color
window = Tk()
window.title('Card Identifier')
window.geometry('730x300')
window.configure(bg='navy')

# Create a label widget for the "title label" that will be displayed in the GUI
label_title = Label(window, text='Welcome to Card Identifier! The perfect app to identify your card!', fg='white',
                    font=('Arial', 20))
label_title.config(bg='black')
label_title.grid(row=1, column=3, padx=75, pady=10)

# Create a label Widget where instructions for the user is shown
label_1 = Label(window, text='Enter your credit card number: ', fg='black', font=('Arial', 14))
label_1.config(bg='white')
label_1.grid(row=2, column=3, padx=75, pady=10)
# This variable is storing user input
data = StringVar()

# Created an Entry widget so the user would be able to enter user input on the GUi
textbox1 = Entry(window, textvariable=data, fg='white', font=('Arial', 14))
# Organized the Entry widget
textbox1.grid(row=3, column=3, padx=75, pady=10)

# Label widget to display results. The Label shows pre defined text but the Label's text will change based on input.
validation_label = Label(window, text='Your result will be displayed here', fg='black', font=('Arial', 14))
validation_label.config(bg='white')
validation_label.grid(row=4, column=3, padx=75, pady=10)


# This method implements the Luhn Algorithm
def validate():
    # Validate credit card length
    if 13 <= len(data.get()) <= 16:
        total_sum = 0
        list_odds = []
        list_even = []

        # Iterate through the string of the odd index and add to the list that contains odds.
        for digit in data.get()[0::2]:
            list_odds.append(digit)
        # Convert items in list to ints
        list_odds_ints = list(map(int, list_odds))

        # Iterate though the list, multiply each item by 2, if greater than 9, add the digits of the integer
        for digit in list_odds_ints:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
            # Add to the total sum
            total_sum += digit

        # Iterate through the string of even indexes and add to the list that contains evens.
        for digit in data.get()[1::2]:
            list_even.append(digit)
        # Convert the items in the list to integers
        list_even_ints = list(map(int, list_even))

        # Add all numbers in the list of even indexes to the total_sum variable
        for digits in list_even_ints:
            total_sum += digits

        # Validate if total_sum == 10 if modulo 10. If so, identify CC provider by index
        if total_sum % 10 == 0:
            if data.get()[0] == '4':
                validation_label.config(text='Credit Card is VALID and belongs to VISA cards', bg='green', fg='white')
            elif data.get()[0] == '5':
                validation_label.config(text='Credit Card is VALID and and belongs to MASTER CARDS', bg='green', fg='white')
            elif data.get()[0] == '3' and data.get()[1] == '7':
                validation_label.config(text='Credit Card is VALID and and belongs to AMERICAN EXPRESS', bg='green', fg='white')
            elif data.get()[0] == '6':
                validation_label.config(text='Credit Card is VALID and and belongs to DISCOVER CARDS', bg='green', fg='white')
        else:
            validation_label.config(text='Credit Card is INVALID', bg='red', fg='white')
    else:
        validation_label.config(text='Credit Card length is INVALID', bg='red', fg='white')


# Button widget to handle event handling based on user input. The command arguments calls the pre defined validate()
button1 = Button(window, command=validate, text='Submit', fg='white', bg='black', font=('Arial', 14))
button1.config(bg='green')
button1.grid(row=5, column=3, padx=305, pady=10)

window.mainloop()
