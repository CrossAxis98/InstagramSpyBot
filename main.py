import tkinter as tk
from instabot_class import InstaBot


def phrase_display():
    login = str(entry_field1.get())
    pw = str(entry_field2.get())
    my_bot = InstaBot(login, pw)
    message = my_bot.get_unfollowers()
    message_display = tk.Text(master=window, height=10, width=30)
    message_display.grid(column=0, row=5, columnspan=3)
    for x in range(len(message)):
        message_display.insert(tk.END, message[x] + '\n')


window = tk.Tk()

window.title("InstagramSpyBot")

window.geometry("400x400")

window.configure(bg='white')

# LABEL
title = tk.Label(text="", height=3, width=50, bg='white')
title.grid(column=0, row=0, columnspan=3)

# LABEL
title = tk.Label(text="Username:", bg='white')
title.grid(column=0, row=2)

# Entry field
entry_field1 = tk.Entry()
entry_field1.grid(column=1, row=2)

# LABEL
title = tk.Label(text="Password:", bg='white')
title.grid(column=0, row=3)

# Entry field
entry_field2 = tk.Entry(show="*")
entry_field2.grid(column=1, row=3)

# BUTTON
button1 = tk.Button(text="Search", command=phrase_display)
button1.grid(column=0, row=4, columnspan=2, padx=10, pady=10)


window.mainloop()
