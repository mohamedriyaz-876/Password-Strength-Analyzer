import tkinter as tk
from tkinter import messagebox

from password_checker import check_password_strength
from password_generator import generate_password
from database import (
    create_database,
    password_exists,
    save_password
)

create_database()


def analyze_password():

    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "Warning",
            "Please enter a password"
        )
        return

    score, feedback = check_password_strength(password)

    result_text = ""

    if score <= 2:
        result_text += "Weak Password\n"
    elif score <= 4:
        result_text += "Medium Password\n"
    else:
        result_text += "Strong Password\n"

    result_text += f"Score: {score}/6\n\n"

    if password_exists(password):
        result_text += "⚠ Password was used before!\n\n"

    if feedback:
        result_text += "Suggestions:\n"
        for item in feedback:
            result_text += f"- {item}\n"

    result_label.config(text=result_text)

    save_password(password)


def suggest_password():

    strong_password = generate_password()

    password_entry.delete(0, tk.END)
    password_entry.insert(0, strong_password)


# GUI Window

root = tk.Tk()

root.title("Password Strength Analyzer")

root.geometry("500x450")

root.resizable(False, False)

title = tk.Label(
    root,
    text="Password Strength Analyzer",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)

password_entry = tk.Entry(
    root,
    width=40,
    show="*",
    font=("Arial", 12)
)

password_entry.pack(pady=10)

analyze_button = tk.Button(
    root,
    text="Analyze Password",
    command=analyze_password,
    width=20
)

analyze_button.pack(pady=5)

generate_button = tk.Button(
    root,
    text="Generate Strong Password",
    command=suggest_password,
    width=20
)

generate_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    justify="left",
    font=("Arial", 11)
)


result_label.pack(pady=20)


root.mainloop()
