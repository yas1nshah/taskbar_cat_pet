import datetime
import tkinter as tk
from PIL import Image, ImageTk
import random

from resources.message_box import MessageBox 
import images
import quotes

# Creating a tkinter label class for the cat 
# it handles all the animation and most of the logic
class CatCharacter(tk.Label):
    def __init__(self, master= None, **kwargs):
        super().__init__(master, **kwargs)
        
        # animation sequences
        self.idle_sequence = []
        self.sleep_sequence = []
        self.start_sleep_sequence= []
        self.end_sleep_sequence= []
        self.dance_sequence= []
        self.walk_left_sequence= []
        self.walk_right_sequence = []

        # habits include all the things the cat does
        self.habits = [self.start_idle, self.start_sleep, self.dance]
        
        # making variables for the cat
        self.current_image = None           # manages current image 
        self.current_index = 0              # manages current index for the image in list
        self.after_func = None              # manages the function which is called after the funtions (basically plays animations)
        self.seconds = 0                    # manages time
        self.animation_state = None         # tells which animation is happening at the moment
        self.runing = False                 # manages if the cat is running or not
        self.running_direc = None           # tells the direction of running

        # calling some initial functions
        self.load_images()
        self.start_idle()
        self.timeSec()
        
        # # time variables for quotes
        # self.current_time = None
        # self.is2Hours = False
        # self.counter_qoute = 0
    
    # check and verify 2 hours
    # def check2Hours(self):
    #     self.current_time = datetime.datetime.now()

    #     # print(self.current_time.second)
    #     if self.current_time.hour % 2 == 0 and self.current_time.second == 0:  
    #         self.is2Hours = True
    #         # print(self.is2Hours)
            
    #     else:
    #         self.is2Hours = False
    #         # print(self.is2Hours)
        
    # selects one random habit to do for the cat
    def habit_now(self):
        habit = random.choice(self.habits)
        # print(str(habit))
        self.seconds= 0
        self.current_index = 0
        return habit()   # calls the fuction from the habit selected
        
    # manages the time in seconds  
    def timeSec(self):
        self.seconds += 1 
        # print(self.seconds)   
        self.after(1000, self.timeSec)
    
    
    # loading all the animation photos to the lists
    def load_images(self):
            # idle
            for i in range(0,2):
                image = Image.open(f"images\\idle\\{i}.png")
                self.idle_sequence.append(ImageTk.PhotoImage(image))
            
            # start Sleep
            for i in range(0,3):
                 image= Image.open(f"images\\start_sleep\\{i}.png")
                 self.start_sleep_sequence.append(ImageTk.PhotoImage(image))
                 
            
            # sleep
            for i in range(0,4):
                 image= Image.open(f"images\\sleep\\{i}.png")
                 self.sleep_sequence.append(ImageTk.PhotoImage(image))

            # end Sleep
            for i in range(0,3):
                 image= Image.open(f"images\\end_sleep\\{i}.png")
                 self.end_sleep_sequence.append(ImageTk.PhotoImage(image))

            # dance 
            for i in range(0,7):
                 image= Image.open(f"images\\dance\\{i}.png")
                 self.dance_sequence.append(ImageTk.PhotoImage(image))
                 
            # walk left
            for i in range(0,3):
                 image= Image.open(f"images\\walk_left\\{i}.png")
                 self.walk_left_sequence.append(ImageTk.PhotoImage(image))
            
            # walk right
            for i in range(0,3):
                 image= Image.open(f"images\\walk_right\\{i}.png")
                 self.walk_right_sequence.append(ImageTk.PhotoImage(image))


    #------------------------------------------------------------------------------------------------------
    # Handling all the animation functions here

    # idle animation
    def start_idle(self):
        #  self.check2Hours()
        #  if self.is2Hours:
        #     # print("yes 2 hrs")
        #     if self.counter_qoute == 0:
        #         self.after(1000, self.makeCatSay)
        #         self.counter_qoute += 1
        #  else:
        #     # print("no 2 hrs")
        #     pass
            
         self.animation_state = "idle" # setting the animation state
         if self.seconds > 10:
             self.after_func = self.after(300, self.habit_now) # calling random habit
             self.counter = 0
             
         else:     
            self.current_index = (self.current_index +1) % len(self.idle_sequence)
            self.current_image = self.idle_sequence[self.current_index]
            self.configure(image= self.current_image, bg = "black")         
            self.after_func = self.after(300, self.start_idle)
    
    # starting sleep animation (sleep 1)
    def start_sleep(self):        
        if self.current_index == 2:
            self.after_func = self.after(400, self.sleeping) # calling sleep 2
            self.current_index = 0
        else:
            self.current_index = (self.current_index +1) % len(self.start_sleep_sequence)
            # print(self.current_index)
            self.current_image = self.start_sleep_sequence[self.current_index]
            self.configure(image= self.current_image, bg = "black")
            self.after_func = self.after(400, self.start_sleep)

    # sleep animation (sleep 2)
    def sleeping(self):
        self.animation_state = "sleeping" # setting the animation state
        if self.seconds > 25:
             self.after_func = self.after(300, self.end_sleep) # calling sleep 3
        else: 
            self.current_index = (self.current_index +1) % len(self.sleep_sequence)
            self.current_image = self.sleep_sequence[self.current_index]
            self.configure(image= self.current_image, bg = "black")
                
            self.after_func = self.after(400, self.sleeping)

    # ending sleep animation (sleep 3)
    def end_sleep(self):
        if self.current_index == 2:
            #  print("idle start")
             self.after_func = self.after(400, self.start_idle) # calling idle state
             self.seconds = 0
             self.current_index = 0
        else:
            self.current_index = (self.current_index +1) % len(self.end_sleep_sequence)
            # print(self.current_index)
            self.current_image = self.end_sleep_sequence[self.current_index]
            self.configure(image= self.current_image, bg = "black")
            self.after_func = self.after(400, self.end_sleep)

    # dance animation
    def dance(self):
        if self.seconds > 5:
             self.after_func = self.after(300, self.habit_now) # calling random habit
        else:

            self.animation_state = "dancing" # setting the animation state
            if self.runing: 
                if self.running_direc == "left":    # for left walk
                    self.after_func = self.after(100, self.walkLeft)
                elif self.running_direc == "right":    # for right walk
                    self.after_func = self.after(100, self.walkRight)

            else:
                self.current_index = (self.current_index +1) % len(self.dance_sequence)
                
                self.current_image = self.dance_sequence[self.current_index]
                self.configure(image= self.current_image, bg = "black")
                self.after_func = self.after(100, self.dance)

    # walk left animation
    def walkLeft(self):
        if not self.runing:
             self.after_func = self.after(100, self.dance) # calling dance funtion when cat reaches end of screen
        else:
            self.current_index = (self.current_index +1) % len(self.walk_left_sequence)
            
            self.current_image = self.walk_left_sequence[self.current_index]
            self.configure(image= self.current_image, bg = "black")
            self.after_func = self.after(200, self.walkLeft)
    
    # walk right function
    def walkRight(self):
        if not self.runing:
             self.after_func = self.after(100, self.dance)  # calling dance funtion when cat reaches end of screen
        else:
            self.current_index = (self.current_index +1) % len(self.walk_right_sequence)
            
            self.current_image = self.walk_right_sequence[self.current_index]
            self.configure(image= self.current_image, bg = "black")
            self.after_func = self.after(200, self.walkRight)
        
    
    # Uncomment this function to make cat say cute AI-Written Quotes to You!
    def makeCatSay(self):
        print("said")
        self.counter_qoute = 0
        with open('quotes\\quotes.txt', 'r') as file:
            # move the file pointer to the start of the third line
            for i in range(random.randrange(0,315)):  # the index is zero-based, so this moves to the third line
                file.readline()
            # read the third line
            self.line = file.readline()
            
            MessageBox(text1=self.line, text2= "~ catoo", time= 15000  )
            print("done")
