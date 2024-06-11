from customtkinter import *
import time
class Timer:
    def __init__(self, master):
        self.time_frame = CTkFrame(master, border_width=3, bg_color='wheat2', width =100)
        self.time_frame.grid(row = 0, column = 2)
        
        self.label_time = CTkLabel(self.time_frame, height=1, width=15, bg_color='wheat1')
        self.label_time.pack(side=LEFT, pady=5)
        self.label_time.pack_propagate(False)
        
        self.label_time_game = CTkLabel(self.time_frame, height=1, width=15, bg_color='wheat1')
        self.label_time_game.pack(side=LEFT,pady=5)
        self.label_time_game.pack_propagate(False)
        
        self.label_cycle_game = CTkLabel(self.time_frame, height=1, width=15, bg_color='wheat1')
        self.label_cycle_game.pack(side=LEFT, pady=5)
        self.label_cycle_game.pack_propagate(False)
        
        self.start_time = time.time()