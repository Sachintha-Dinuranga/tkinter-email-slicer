from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

def email_slicer(email):
    try:
        username, domain = email.split('@')
        # print(f'Your email address domain is {domain} and service is {service}')
        return username, domain
    except ValueError:
        return None, None

def is_valid_email(email):
    # Regex pattern
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.fullmatch(pattern, email):
        return True
    return False
    

def slice_email():
    email = entry.get().strip()

    if not email:
        messagebox.showwarning('Warning', 'Please Enter Valid Email!')
        return

    if is_valid_email(email):
        username, domain = email_slicer(email)

        if username and domain:
            result_label.config(text=f'\nUsername: {username}\nDomain: {domain}')
        else:
            messagebox.showwarning('Error', 'Invalid email Use: example@gmail.com')
    else:
        messagebox.showwarning('Error', 'Invalid email Use: example@gmail.com')

# initialization
root = Tk()
root.title("Email Slicer")
root.geometry('400x250')
frm = ttk.Frame(root, padding=10)
frm.pack(fill=BOTH, expand=True)

#Title
ttk.Label(frm, text='Email Slicer', font=('Arial', 18 , 'bold')).pack(pady=10)

#email input
ttk.Label(frm, text='Enter your email: ').pack()
entry = ttk.Entry(frm, width=30)
entry.pack(pady=5)

# slice button
ttk.Button(frm, text='Slice Email', command=slice_email).pack(pady=10)

# Result label
result_label = ttk.Label(frm, text='', font=('Arial', 12), justify=CENTER, foreground='cornflower blue')
result_label.pack(pady=10)

root.mainloop()