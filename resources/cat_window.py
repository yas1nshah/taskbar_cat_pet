import tkinter
from resources.cat_class import CatCharacter 


#called when Mouse Hovers
def hovering_mouse(event):
    if catobj.animation_state== "dancing":
        update_position()    # hovering over the cat recalls the function making it faster (i wanted it to run away form mouse)       
    else:
        # print("Cat not Dancing")
        pass

def kill_cat(e):
    print("killing Cat")
    if e.keysym == "Escape":
        catWindow.destroy()


    # making cat object as label
def make_cat():
    global catobj
    catobj = CatCharacter(catWindow)
    catobj.pack()

# binding cat to Hover Event
def bind_cat():
    catWindow.bind("<Motion>", hovering_mouse)
    catWindow.bind("<Key>", kill_cat)


#creating main cat Window
def create_window():
    global catWindow, screen_height, screen_width, cat_height, cat_width, x, y
    catWindow = tkinter.Tk()
    print("Cat is initialized")


    # cat window settings
    catWindow.wm_attributes("-topmost", True)
    catWindow.wm_attributes("-transparentcolor", "black")
    catWindow.overrideredirect(True)

    # screen Resoluion
    screen_width = catWindow.winfo_screenwidth()
    screen_height =catWindow.winfo_screenheight()
    print(f"Your current screen resolution is {screen_height}x{screen_width}")

    #cat resolution in pixels (same as image resolutions)
    cat_width= 100 
    cat_height= 100

    #cat position
    x= screen_width - cat_width
    if screen_height < 1080:
        y= screen_height - cat_height -35 # window start-menu is about 50 px
    else:
        y= screen_height - cat_height -50

    catWindow.geometry(f"{cat_width}x{cat_height}+{x}+{y}")
    

    make_cat()
    bind_cat()
    call_mainloop()

# to call main cat window
def call_mainloop():
    catWindow.mainloop()

# cat position logic
def update_position():
    # print("updating")
    global x, screen_width
    # runs left if cat is on right side of window
    if x > int(screen_width * 0.8): # checks cat window x is larger than 80% of screen size
        catobj.running_direc = "left" # updates direction
        # print(f"runing {catobj.running_direc}")
        run_left()
       
    # runs right if cat is on left side of window
    elif x <(int(screen_width * 0.1)):# checks cat window x is smaller than 10% of screen size
        catobj.running_direc = "right" # updates direction
        catobj.runing = True
        # print(f"run {catobj.running_direc}")
        run_right()
        
# for running left
def run_left():
     global x, y, cat_width, cat_height, screen_width, catWindow
   
     if x > int(screen_width *0.01): # cat window stops at 5% of screen width
       if x == int(screen_width *0.01 + 1):       
            catobj.runing = False # updates running status
       else:
            x -= 1   
            catWindow.geometry(f"{cat_width}x{cat_height}+{x}+{y}") # updates cat window position
            catWindow.after(100, run_left)
            catobj.runing = True # updates running status
            

# for running right
def run_right():    
     global x, y, cat_width, cat_height, screen_width
     if x < int(screen_width * 0.9): # cat window stops at 95% of screen width
        if x == int(screen_width * 0.9) - 1:       
            catobj.runing = False       # updates running status
        elif catobj.runing:
            x += 1   
            catWindow.geometry(f"{cat_width}x{cat_height}+{x}+{y}") # updates cat window position
            catWindow.after(100, run_right)
            catobj.runing = True # updates running status