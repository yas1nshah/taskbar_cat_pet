
import tkinter as tk
from tkinter import font


def MessageBox(text1, text2, fade = 0.01, time = 5000):
    window = tk.Tk()
    window.configure(bg='black')
    window. configure(padx=25, pady= 25)
    window.title("Message Box")

  
    # print(str(func))
    
    
    # Set the font to appear like pixels
    
    font1 = ('Courier', 20, font.BOLD)
    font2 = ('Courier', 12)
    
    label1 = tk.Label(window, text=text1, font=font1, bg='black', fg='pink', wraplength=500)
    label1.pack()
    
    label2 = tk.Label(window, text=text2, font=font2, bg='black', fg='pink', anchor='e')
    label2.pack(side='right')
    
    # Set window opacity to 0.0 (completely transparent)
    window.attributes('-alpha', 0.0)

    # window settings
    window.wm_attributes("-topmost", True)
    window.wm_attributes("-transparentcolor", "black")
    window.overrideredirect(True)

     # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate the x and y coordinates to center the window
    x = int((screen_width / 2) - (window.winfo_reqwidth() / 2))- int(screen_width * 0.08)
    y = int((screen_height / 2) - (window.winfo_reqheight() / 2))
    
    # Set the window position
    window.geometry(f'+{x}+{y}')
    
    # Define a function to change the opacity over time
    def fade_in():
        opacity = window.attributes('-alpha')
        if opacity < 1.0:
            opacity += fade
            window.attributes('-alpha', opacity)
            window.after(10, fade_in)
    
    # Schedule the fade-in effect after a brief delay
    window.after(500, fade_in)
    
    # Schedule the window to close after 5 seconds
    window.after(time, window.destroy)
    
    window.mainloop()

