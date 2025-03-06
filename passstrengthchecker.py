import tkinter as tk
from tkinter import ttk

def check_password(*args):
    password = password_var.get()
    score = sum([
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password)
    ])
    
    progress['value'] = (score / 5) * 100
    strength_var.set(["😡 Weak", "😬 Medium", "💪 Strong"][min(score // 2, 2)])

# Initialize main Tkinter window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300+480+200")
root.configure(bg='#000')  # Background color
root.resizable(False, False)
root.iconbitmap('lock.ico')

password_var = tk.StringVar()
password_var.trace('w', check_password)

# UI Components
tk.Label(root, text="Enter Password:", font=('Poppins', 20), bg='#000', fg='white').pack(pady=10)
tk.Entry(root, textvariable=password_var, show="•", width=30).pack()
progress = ttk.Progressbar(root, length=300, mode="determinate")
progress.pack(pady=10)
strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var, font=('Interceptor', 24), bg='#000', fg='white').pack()

root.mainloop()
