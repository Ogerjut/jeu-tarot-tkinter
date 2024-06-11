from customtkinter import *

class Player:
    def __init__(self, name,  pos) :
        self.name = name
        self.pos = pos
        self.hand = []
        self.a_mise = False
        self.a_pris = False
        self.first_to_play = False
        self.win_round = False
        self.plis_gagnés = []
        self.nb_bout = 0 
        self.bonus = 1
        self.score_manche = 0
        self.score_game = 0
        self.winner_game = False
        self.score_plis = 0
    
    def frame(self, root, method):
        self.frame_player = CTkFrame(root, width=150, height=150, corner_radius=2, fg_color="azure", border_width=1)
        self.frame_player.grid(row = self.pos[0], column = self.pos[1])
        
        self.label = CTkLabel(master=self.frame_player, width= 100, text=self.name, font=("Arial Bold", 12),corner_radius=10, justify="left", fg_color='azure2')
        self.label.pack()
        self.label.pack_propagate(False)
        
        self.text = CTkTextbox(self.frame_player, fg_color="azure", border_color="black", border_width=1)
        self.text.pack(side=RIGHT)
        self.text.pack_propagate(False)
        self.text.configure(state=DISABLED)
        # text a afficher et methode a appler en cas de double clic sur text
        self.text.bind("<Double-1>", method)
        
    def update(self):
        self.text.configure(state = NORMAL)
        self.text.delete(1.0, END)
        for card in self.hand :
            self.text.insert(END, f"{card.valeur} {card.couleur}\n")
        self.text.configure(state=DISABLED)

    def labelAPris(self, mise):
        self.label.configure(text = f"{self.name} a pris une {mise}", fg_color='azure3')
        