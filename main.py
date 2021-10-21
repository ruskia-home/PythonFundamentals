import tkinter as tk

import json

from screens import render_my_screen

if __name__ == '__main__':
    # obj = {
    #     "username": "marto",
    #     "password": "123123",
    #     "firstName": "Martin",
    #     "lastName": "Georgiev"
    # }
    # print(json.dumps(obj))
    window = tk.Tk()
    window.geometry("300x200")
    window.title("My First App")
    render_my_screen(window)
    window.mainloop()
