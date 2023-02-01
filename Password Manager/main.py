from tkinter import *  # import all of the classes, constants, but does not import message box
from tkinter import messagebox  # import the message box module
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # for char in range(randint(8, 10)):
    #   password_list.append(random.choice(letters))
    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    # for char in range(randint(2, 4)):
    #   password_list += random.choice(symbols)
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    # for char in range(randint(2, 4)):
    #   password_list += random.choice(numbers)
    password_numbers = [choice(numbers) for _ in range(randint(1, 2))]

    # combine three lists into one list and shuffle the password list
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    # insert the random password into input
    password_input.insert(0, password)
    pyperclip.copy(password)  # auto copy the password when generate a new password, so can paste directly


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()

    # if one of the input is empty, create a message box to remind user the input is empty
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="please make sure you haven't left any fields empty.")

    else:
        # create a message box to check that details are correct
        # messagebox.showinfo(title="Title", message="message")  # show the information
        is_ok = messagebox.askokcancel(title=website, message=f"There are details entered: \nEmail: {email}"
                                                      f"\nPassword: {password}\n Is it ok to save?")

        if is_ok:  # if user press ok button then add into data.txt, otherwise do nothing
            with open("data.txt", "a") as data_file: # "a" represents append mode
                data_file.write(f"{website} | {email} | {password}\n")
                # after save the data into data.txt file, the input (except email input) should become empty
                web_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

name_label = Label(text="Email/Username: ")
name_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entry
web_input = Entry(width=38)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()  # focus the cursor into that particular entry

email_input = Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2)
# insert(0/END, ""), END represent the very last character inside that entry, 0 is the start character
email_input.insert(0, "example@gmail.com")  # pre-populated email as a default value

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

