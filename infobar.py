from customtkinter import *

class InfoBar:
    def __init__(self, master) :
        self.frame = CTkFrame(master, width=230, height=60, corner_radius=2, fg_color="azure3", border_width=1)
        self.frame.grid(row = 0, column = 0, ipady=50)
        self.frame.pack_propagate(False)
        
        self.label = CTkLabel(master=self.frame, text="Infos Partie :", font=("Arial Bold", 13), justify="left")
        self.label.place(relx = 0.5, rely = 0.15, anchor="center")   
        self.label.pack_propagate(False)
        
        self.label1 = self.labelInfo(0.25, 0.4)
        self.label2 = self.labelInfo(0.75, 0.40)
        self.label3 = self.labelInfo(0.5, 0.6)
        
    def labelInfo(self, relx, rely):
        info_label = CTkLabel(master=self.frame, text="", font=("Arial Bold", 13), justify="left")
        info_label.place(relx=relx, rely=rely, anchor="center")   
        info_label.pack_propagate(False)
        return info_label
            