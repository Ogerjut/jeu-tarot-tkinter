from customtkinter import *

class Enchere:
    def __init__(self):
        # self.player_enchere = self.list_player[0]
        self.isDone = False
        self.mises = {"prise":1, "garde":2, "garde sans":3, "garde contre":4}
        self.list_disable_option = []
        self.actual_bet = 0
        self.bet = {}
    
    def frame(self, table, player, method, methodskip):
        print("enchères")
        # self.remove_widget(self.table)
        self.enchere_frame = CTkFrame(table, width=300, height=300, corner_radius=2, fg_color="azure3", border_width=1)
        self.enchere_frame.pack()
        self.enchere_frame.pack_propagate(False)
        
        self.enchere_label = CTkLabel(master=self.enchere_frame, text=f"Enchères du {player.name}", font=("Arial Bold", 16), justify="left")
        self.enchere_label.place(relx = 0.5, rely= 0.2, anchor = "center")
        
        self.enchere_button = CTkSegmentedButton(self.enchere_frame, values=list(self.mises.keys()), command=method)
        self.enchere_button.place(relx = 0.5, rely= 0.6, anchor = "center")
        
        for button in self.enchere_button._buttons_dict.values():
            if button.cget("text") in self.list_disable_option :
                button.configure(state="disabled", fg_color="gray", text_color="darkgray")
            else : button.configure(state="normal", fg_color="azure1", text_color="blue")
        self.skip_button = CTkButton(master=self.enchere_frame, text="Passer", width=100, command = methodskip)
        self.skip_button.place(relx=0.5, rely = 0.80, anchor = "center")
        
        # progress bar pour temps (si timer out, passer)
        self.timer = CTkProgressBar(self.enchere_frame, width= 100, height=10, corner_radius= 15, fg_color="red" )
        self.timer.place(relx = 0.5, rely = 0.4, anchor = "center")
        self.timer.pack_propagate(False)
        self.timer.set(0)
    
    def setBet(self, mise, player):
        match mise : 
            case "prise" : bet = 1
            case "garde" : bet = 2
            case "garde sans" : bet = 3
            case "garde contre" : bet = 4   
        self.bet[player]= bet
        # self.player_enchere.a_misé = True       
        if bet > self.actual_bet : 
            self.actual_bet = bet
        if self.actual_bet == 4 :
            self.endEnchère(player, mise)
        print(f"{player.name} a misé une {mise}")
        
    def endEnchère(self, player, mise):
        player.first_to_play = True
        player.a_pris = True
        self.isDone = True
        self.mise = mise
        self.actual_bet = 0
        self.bet = {}
        print(f"{player.name} a pris une {mise}")
        match mise :
            case "garde": player.bonus = 2 
            case "garde sans" : player.bonus = 4 
            case "garde contre" :player.bonus = 6
           
            
       
