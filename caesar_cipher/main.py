# TASK DETAILS #
#-------------------------------------------------------------#

# Caesar Cipher

# Implement a Caesar cipher, both encoding and decoding.
# The key is an integer from 1 to 25.
# This cipher rotates letters of the alphabet (A-Z).
# The encoding replaces each letter with the 1st to 25th next letter in the alphabet
# So key 2 encrypts “HI” to “JK”, but key 20 encrypts “HI” to “BC”.

#-------------------------------------------------------------#

import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import simpledialog

with open("/Users/pmkhambhaita/Developer/caesar_cipher/words.txt", "r") as file:
        dictionary = set(word.strip() for word in file)

# --- Entry widget configuration --- #

placeholder_msg = 'Enter message: '


def erase(event=None):
    if msg_entry.get() == placeholder_msg:
        msg_entry.delete(0, 'end')


def add(event=None):
    if msg_entry.get() == '':
        msg_entry.insert(0, placeholder_msg)


# --- Command configuration for buttons --- #


def encrypt_clicked():
    text = msg_entry.get()
    if text == '':
        messagebox.showwarning(title="Error", message="No message entered!")
        return
    shift = simpledialog.askinteger("Key",
                                    "Enter the key you wish to use: ",
                                    minvalue=1,
                                    maxvalue=26)
    if shift is None:
        return
    warning_encrypt = simpledialog.askstring(
        "Warning", "Are you sure you want to encrypt? Loss of the key will result in a lost message! Enter the word CONFIRM to continue. ")
    if warning_encrypt is not None and warning_encrypt.lower() == 'confirm':
            if shift is not None:
                output = caesar_cipher(text, shift)
                messagebox.showinfo(title="Result", message="Encrypted msg: " + output)
                save_msg = messagebox.askquestion(
                    title="Save encryption",
                    message="Would you like to save the message?")
                if save_msg is not None:
                    with open("encrypted_msg.txt", "w") as save_file:
                        save_file.write(output)
                        save_file.close()
                        messagebox.showinfo(title="Complete!", message="Operation complete - message encrypted.")
    elif warning_encrypt is None or warning_encrypt.lower() != 'confirm':
        messagebox.showinfo(title="ABORT", message="Aborted! Message not encrypted.")

def decrypt_clicked():
    text = msg_entry.get()
    if text == '':
        messagebox.showwarning(title="Error", message="No message entered!")
        return
    if text.lower() == "fetch":
        with open("encrypted_msg.txt", "r") as save_file:
            text=save_file.read()
            save_file.close()
    shift = simpledialog.askinteger("Key",
                                    "Enter the key: ")
    if shift is not None and shift > 0 and shift < 26:
        output = caesar_cipher(text, -shift)
        messagebox.showinfo(title="Result", message="Decrypted msg: " + output)
        save_msg = messagebox.askquestion(
            title="Save decryption",
            message="Would you like to save the message?")
        if save_msg is not None:
            with open("decrypted_msg.txt", "w") as save_file:
                save_file.write(output)
                save_file.close()
    elif isinstance(shift, int):
        bforce = simpledialog.askstring(title="Error", prompt="Invalid key! Enter the word CONFIRM to brute-force, or anything else to abort")
        if bforce is not None and bforce.lower() == 'confirm':
            with open("brute_force.txt", "w") as save_file:
                for i in range(0,26):
                    output = caesar_cipher(text, -i)
                    split_out = output.split()
                    for word in split_out:
                        if word.lower() in dictionary:
                            messagebox.showinfo(title="Word found in dictionary", message="The message contents have been found in a dictionary with key " + str(i) + ". See txt file.")
                            save_file.write("-----> Key: " + str(i) + " | Output: " + output + '\n')
                        else:
                            save_file.write("Key: " + str(i) + " | Output: " + output + '\n')
            save_file.close()
            messagebox.showwarning(title="Result", message="Brute force complete. The output has been saved as brute_force.txt")
        else:
            messagebox.showwarning(title="ABORT", message="Brute force aborted. No action taken.")
# --- Window initialisation and alignment --- #

root = tk.Tk()
custom_font = font.Font(family="Ubuntu", size=16)

root.title('CCE/D')
root.geometry('1000x300')
program_title = tk.Label(text='Caesar Cipher Encrypter/Decrypter',
                         font=custom_font)
msg_entry = tk.Entry()

add()

msg_entry.bind('<FocusIn>', erase)
msg_entry.bind('<FocusOut>', add)

encrypt_button = tk.Button(text="Encrypt", command=encrypt_clicked)
decrypt_button = tk.Button(text="Decrypt", command=decrypt_clicked)

program_title.pack(anchor="center")
msg_entry.pack()
encrypt_button.pack()
decrypt_button.pack()

# --- The Caesar Cipher function --- #
# It uses ASCII values and adds the value of the key to the ASCII value
# It then reconverts the value into a standard letter
# This process is applied to all letters in the string
# Non-letter characters (eg. : | ; | , | . | etc.) are ignored


def caesar_cipher(text, shift):
    result = ''  # Empty variable to store result
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Ensure the shift is within the alphabet's range
            if char.islower():
                shifted_char = chr(
                    ((ord(char) - ord('a') + shift_amount) % 26) +
                    ord('a'))  # Lower case shift
            else:
                shifted_char = chr(
                    ((ord(char) - ord('A') + shift_amount) % 26) +
                    ord('A'))  # Upper case shift
            result += shifted_char
        else:
            result += char  # Leaves non-letter characters as they are

    return result


# --- Window closing --- #
root.mainloop()
