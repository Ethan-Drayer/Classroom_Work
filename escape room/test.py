import os
import tkinter as tk
from tkinter import simpledialog, messagebox


# Function to retrieve code from the flash drive
def retrieve_code_from_flash_drive():
    flash_drive_path = "E:/code.txt"  # Adjust this path based on where your flash drive is mounted

    if not os.path.exists(flash_drive_path):
        return None

    try:
        with open(flash_drive_path, "r") as file:
            code = file.read().strip()
            if len(code) == 6 and code.isdigit():
                return code
            else:
                return None
    except Exception as e:
        return None


# Function to retrieve the 4-digit number from the user
def retrieve_values():
    while True:
        digits = simpledialog.askstring("Enter Digits", "Enter the 4 digit integer:")
        try:
            digits = int(digits)
        except:
            messagebox.showerror("Input Error", "Integer value required.")
            continue
        if digits < 0:
            messagebox.showerror("Input Error", "Positive integers required.")
            continue

        digits = [int(i) for i in str(digits)]

        if len(digits) != 4:
            messagebox.showerror("Input Error", "4 digits required.")
            continue

        while True:
            increment = simpledialog.askstring("Enter Increments", "By how many increments should it be shifted:")
            try:
                increment = int(increment)
            except:
                messagebox.showerror("Input Error", "Integer value required.")
                continue

            if increment < 0:
                messagebox.showerror("Input Error", "Positive integers required.")
                continue

            digits.append(increment)
            return digits


# Function to implement the cipher transformation
def inigma(number):
    increment = number.pop(4)
    decimal_number = 0
    while increment > 0:
        increment -= 1
        if decimal_number == 15:
            decimal_number = 0
        else:
            decimal_number += 1

        for index in range(len(number)):
            if number[index] == 1:
                number[index] = 5
            elif number[index] == 2:
                number[index] = 3
            elif number[index] == 3:
                number[index] = 8
            elif number[index] == 4:
                number[index] = 6
            elif number[index] == 5:
                number[index] = 2
            elif number[index] == 6:
                number[index] = 1
            elif number[index] == 7:
                number[index] = 9
            elif number[index] == 8:
                number[index] = 7
            elif number[index] == 9:
                number[index] = 4

        binary_string = format(decimal_number, '04b')
        binary = [int(i) for i in str(binary_string)]
        binary = binary[::-1]
        if binary[0] == 1:
            if number[0] == 9:
                number[0] = 1
            else:
                number[0] += 1

        if binary[1] == 1:
            if number[1] == 9:
                number[1] = 1
            else:
                number[1] += 1

        if binary[2] == 1:
            if number[2] == 9:
                number[2] = 1
            else:
                number[2] += 1

        if binary[3] == 1:
            if number[3] == 9:
                number[3] = 1
            else:
                number[3] += 1
        print(number)
    return number


# Main GUI Application
def start_escape_room_game():
    # Initialize Tkinter root window and hide it
    root = tk.Tk()
    root.withdraw()  # Hide the main window, we will only use dialogs

    # Prompt for manual input or flash drive
    choice = simpledialog.askstring("Choose Input Method",
                                    "Enter 'manual' to input the code manually or 'flash' to use the flash drive:")

    # Validate the input choice
    if choice not in ['manual', 'flash']:
        messagebox.showerror("Input Error", "Invalid choice. Please restart the game.")
        return

    code_from_flash = None

    if choice == 'flash':
        # Use the flash drive to retrieve the code
        messagebox.showinfo("Flash Drive", "Please insert your flash drive with the code.txt file.")
        code_from_flash = retrieve_code_from_flash_drive()

    # If no code is retrieved from flash, prompt for manual input
    if choice == 'manual' or not code_from_flash:
        code_from_flash = simpledialog.askstring("Enter Code", "Enter the 6-digit code manually:")

    # Check if the retrieved code is valid
    if code_from_flash and len(code_from_flash) == 6 and code_from_flash.isdigit():
        print(f"Code from input: {code_from_flash}")

        attempt = simpledialog.askstring("Code Entry", "Enter the code to unlock:")
        if attempt == code_from_flash:
            # Retrieve the 4-digit integer from the user
            listed_digits = retrieve_values()
            test = inigma(listed_digits)
            # Display the final result
            messagebox.showinfo("Puzzle Solved", f"Puzzle Solved: {test}")
        else:
            messagebox.showerror("Wrong Code", "Wrong code. Try again.")
    else:
        messagebox.showerror("Error", "Invalid code entered. Exiting.")


# Start the escape room game
if __name__ == "__main__":
    start_escape_room_game()