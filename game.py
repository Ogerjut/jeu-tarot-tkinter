from customtkinter import *

class Game:
    def __init__(self):
        self.set_chien = False
        self.roundIsRunning = False
        self.nb_j = int
        self.nb_round = 1
        self.nb_round_max = int
        self.nb_game = 1
        self.nb_game_max = 2
        self.list_player = []
        self.pli = {}
        self.current_color = str
        self.color_choosen = False
        self.last_value_atout = []
        self.pliIsDone = False
        self.isOver = False
        self.rank = {}
        self.show_rank = False
    
    def setNbPlayers(self, root, method):
        self.set_game = CTkFrame(root, width=400, height=400,bg_color='transparent', fg_color= "Slategray3", corner_radius=35, border_width=6, background_corner_colors=("Slategray2", "Slategray2", "Slategray2", "Slategray2"), border_color="Slategray2")
        self.set_game.place(relx = 0.5, rely = 0.5, anchor="center")
        
        self.button_4p = CTkButton(self.set_game,height=100, width=200, text="4 JOUEURS",  command=lambda : method(self.button_4p), font=('Arial Bold', 25), text_color="black", fg_color="rosy brown", border_width=1, border_color="indian red")
        self.button_4p.place(relx = 0.5, rely = 0.3, anchor="center")
        
        self.button_5p = CTkButton(self.set_game,height=100, width=200, text="5 JOUEURS",  command=lambda : method(self.button_5p), font=('Arial Bold', 25), text_color="black", fg_color="rosy brown", border_width=1, border_color="indian red")
        self.button_5p.place(relx = 0.5, rely = 0.7, anchor="center")
        
    def frame(self, root):
        self.table = CTkFrame(root, width=400, height=300, corner_radius=60, fg_color="green", border_width=10,  border_color="brown", background_corner_colors=["white", "white", "white", "white"])
        self.table.grid(row = 1, column =1)
        
        if self.roundIsRunning :
            print("Manche en cours")
            self.table_pli = CTkTextbox(self.table, height=90, width=90, fg_color='green', activate_scrollbars=False, border_width=2)
            self.table_pli.pack(side=RIGHT)
            self.table_pli.pack_propagate(False)
            self.table_pli.configure(state=DISABLED)
            self.table_pli.place(relx = 0.5, rely=0.5, anchor="center")
            
            self.pli_label = CTkLabel(self.table, text=f"Manche en cours", bg_color="lightgreen", corner_radius=10)
            self.pli_label.place(relx = 0.5, rely=0.75, anchor="center")
            self.pli_label.pack_propagate(False)
            
            self.timer = CTkProgressBar(self.table, width= 100, height=10, corner_radius= 15, fg_color="red" )
            self.timer.place(relx = 0.5, rely = 0.25, anchor = "center")
            self.timer.pack_propagate(False)
            self.timer.set(0)
            
            # else : 
            # if self.isOver : self.frameGameOver()  
            # if not self.set_chien and not self.roundIsRunning : self.frameChien()
    
    def frameGameOver(self, method=None):
        self.g_o_frame = CTkFrame(self.table, width=260, height=260, corner_radius=2, fg_color="azure3", border_width=1)
        self.g_o_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.g_o_frame.pack_propagate(False)
        
        self.g_o_label = CTkLabel(master=self.g_o_frame, text="Classement :", font=("Arial Bold", 13), justify="left")
        self.g_o_label.place(relx=0.5, rely=0.1, anchor="center")
        self.g_o_label.pack_propagate(False)
        
        self.g_o_text = CTkTextbox(self.g_o_frame, height=150, width=200, activate_scrollbars=False, border_width=2)
        self.g_o_text.pack(side=RIGHT)
        self.g_o_text.pack_propagate(False)
        self.g_o_text.configure(state=DISABLED)
        self.g_o_text.place(relx = 0.5, rely=0.5, anchor="center")
        
        print(self.isOver)
        if self.isOver and not self.show_rank : 
            self.button_g_o = CTkButton(self.g_o_frame, text="Retour au menu principal", command=method)
            self.button_g_o.place(relx = 0.5, rely = 0.9, anchor="center") 
        else :
            self.end_round_timer = CTkProgressBar(self.g_o_frame, width= 100, height=10, corner_radius= 15, fg_color="red" )
            self.end_round_timer.place(relx = 0.5, rely = 0.9, anchor = "center")
            self.end_round_timer.pack_propagate(False)
            self.end_round_timer.set(0)
        
        
    def frameChien(self, methode=None, method2=None, method3=None):
        self.chien_frame = CTkFrame(self.table, width=250, height=250, corner_radius=2, fg_color="azure3", border_width=1)
        self.chien_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.chien_frame.pack_propagate(False)
        
        self.chien_label = CTkLabel(master=self.chien_frame, text="Constituer le chien", font=("Arial Bold", 13), justify="left")
        self.chien_label.place(relx=0.5, rely=0.1, anchor="center")
        self.chien_label.pack_propagate(False)
        
        self.chien_label1 = CTkLabel(master=self.chien_frame, text="Chien", font=("Arial Bold", 13), justify="left")
        self.chien_label1.place(relx=0.25, rely=0.3, anchor="center")
        self.chien_label1.pack_propagate(False)
        self.chien_label2 = CTkLabel(master=self.chien_frame, text="Nouveau chien", font=("Arial Bold", 13), justify="left")
        self.chien_label2.place(relx=0.75, rely=0.3, anchor="center")
        self.chien_label2.pack_propagate(False)
        
        self.chien_text = CTkTextbox(self.chien_frame, height=110, width=85, activate_scrollbars=False, border_width=2)
        self.chien_text.pack(side=RIGHT)
        self.chien_text.pack_propagate(False)
        self.chien_text.configure(state=DISABLED)
        self.chien_text.place(relx = 0.25, rely=0.55, anchor="center")
        self.chien_text.bind("<Double-1>", methode)
        
        self.new_chien_text = CTkTextbox(self.chien_frame, height=110, width=85, activate_scrollbars=False, border_width=2)
        self.new_chien_text.pack(side=RIGHT)
        self.new_chien_text.pack_propagate(False)
        self.new_chien_text.configure(state=DISABLED)
        self.new_chien_text.place(relx = 0.75, rely=0.55, anchor="center") 
        self.chien_text.bind("<Double-1>", method2)

        self.button_chien = CTkButton(self.chien_frame, text="Valider nouveau chien", command=method3)
        self.button_chien.place(relx = 0.5, rely = 0.85, anchor="center")
        
        self.chien_timer = CTkProgressBar(self.chien_frame, width= 100, height=10, corner_radius= 15, fg_color="red" )
        self.chien_timer.place(relx = 0.5, rely = 0.2, anchor = "center")
        self.chien_timer.pack_propagate(False)
        self.chien_timer.set(0)
    
    def changePlayer(self, current_player):
        if self.list_player.index(current_player) < len(self.list_player)-1 :
            current_player  = self.list_player[self.list_player.index(current_player)+1]
            self.pli_label.configure(text= f"Au tour de {current_player.name}")
            return current_player   
        else : 
            self.pliIsDone = True
            self.pli_winner()
            self.defineFirst()
            # renvoie nouveau round card
    def activateChien(self, methodchien, methodnewchien):
        self.chien_text.bind("<Double-1>", methodchien)
        self.new_chien_text.bind("<Double-1>", methodnewchien)
            
    def update(self, text, dic):
            text.configure(state = NORMAL)
            text.delete(1.0, END)
            for val in dic :
                text.insert(END, f"{dic[val].valeur} {self.pli[val].couleur}\n")
            text.configure(state=DISABLED)
        
    def updateRank(self):
        self.g_o_text.configure(state = NORMAL)
        self.g_o_text.delete(1.0, END)
        sorted_dict = dict(sorted(self.rank.items(), key=lambda item: item[1], reverse=True))
        for key, val in sorted_dict.items() :
            self.g_o_text.insert(END, f"{key.name} : {val} points \n")
        self.g_o_text.configure(state=DISABLED)
        # afficher en premier plus grand score
        
        
    def updateTextList(self, text, list):
        text.configure(state = NORMAL)
        text.delete(1.0, END)
        for card in list :
            text.insert(END, f"{card.valeur} {card.couleur}\n")
        text.configure(state=DISABLED) 
    
    def checkCard(self, card, hand):
        self.possible_cards = []
        if not self.color_choosen : 
            self.current_color = card.couleur
            self.color_choosen = True
            self.possible_cards = [card for card in hand]
        else :  
            if self.current_color == "Atout" and card.valeur !=0 :
                max_atout = max(self.last_value_atout)
                self.possible_cards = [card for card in hand if card.couleur == self.current_color and card.valeur > max_atout]
                if len(self.possible_cards) == 0 : 
                    self.possible_cards = [card for card in hand if card.couleur == self.current_color]
                if len(self.possible_cards) == 0 : 
                    self.possible_cards = [card for card in hand]
                    
            else : 
                self.possible_cards = [card for card in hand if card.couleur == self.current_color]
                if len(self.possible_cards) == 0 and len(self.last_value_atout) == 0:
                    self.possible_cards = [card for card in hand if card.couleur == "Atout"]
                if len(self.last_value_atout) != 0 and len(self.possible_cards) == 0 :
                    max_atout = max(self.last_value_atout) 
                    self.possible_cards = [card for card in hand if card.valeur > max_atout and card.couleur == "Atout"]
                if len(self.possible_cards) == 0 :
                    self.possible_cards = [card for card in hand if card.couleur == "Atout"]
                if len(self.possible_cards) == 0 : 
                    self.possible_cards = [card for card in hand]
                    
        if self.possible_cards.__contains__(card) or card.valeur == 0 :
            if card.couleur == "Atout" and card.valeur != 0 :
                self.last_value_atout.append(card.valeur)
            return True
            # for card in self.hand :
            #     if card.couleur == "Atout" :
            #         print(f"il reste au {self.name} les atouts : {card.valeur}")
        
        
    def pli_winner(self):
        card_to_compare = []
        for player in self.pli :
            if self.pli[player].couleur == self.current_color :
                card_to_compare.append(self.pli[player].valeur)
            
            if self.pli[player].couleur == "Atout" and self.pli[player].valeur != 0 : 
                card_to_compare.clear()
                self.current_color = "Atout"
                card_to_compare.append(self.pli[player].valeur)
        
        best_card = max(card_to_compare)
        
        for key, value in self.pli.items() : 
            if value.valeur == best_card :
                key.win_round = True
                print(f"{key.name} a gagné le pli")
                key.plis_gagnés.append(self.pli[player])
                if key.a_pris :
                    score = self.compute(key)
                    print(f"{key.name} a marqué : {score}")
                    
                return key   
    
    def defineFirst(self):
        for num, player in enumerate(self.list_player) : 
            if player.first_to_play == True :
                player.first_to_play = False
            if player.win_round == True :
                player.first_to_play = True
                index = num    
        self.list_player = self.list_player[index:] + self.list_player[:index] 
    
    def computePointsGame(self):
        # revoir exactement comptage des points !!!
        for player in self.list_player : 
            player.score_game += player.score_manche
            highest = player.score_game 
            #ligne bizarre ?
            if highest < player.score_game :
                highest = player.score_game
            print(f"{player.name} a marqué : {player.score_game} durant la partie")
        
        if self.nb_game == self.nb_game_max  :
            for player in self.list_player :
                if player.score_game == highest : 
                    player.winner_game = True
                    
    def computePointsRound(self, chien):
        print("Compte points")
        for player in self.list_player :
            if player.a_pris == True and player.bonus == 1 or 2 or 4 :
                for card in chien :
                    player.plis_gagnés.append(card)
                print("chien ajouté aux plis")
            score, nb_bout = self.computePoints(player)
            print(f"{player.name} a marqué : {score} (bouts:{nb_bout})")
            self.rank[player] = score
            player.plis_gagnés.clear()
            if player.a_pris == True :
                match nb_bout :
                    case 0: player.contrat = 56
                    case 1: player.contrat = 51
                    case 2: player.contrat = 41
                    case 3: player.contrat = 36
                if player.contrat == player.score_manche :
                    print(f"{player.name} a juste win")
                elif player.contrat < player.score_manche :
                    print(f"{player.name} a win")
                else : print(f"{player.name} avait un contrat de {player.contrat} mais a chuté")
            
                
    def computePoints(self, player):
        player.nb_bout = 0
        for card in player.plis_gagnés :
            if card.couleur == "Atout":
                if card.valeur == 1 or card.valeur == 21 or card.valeur == 0 :
                    player.nb_bout +=1
                    pts = 4.5
                else : pts = 0.5
            else : 
                match card.valeur :
                    case 14 |13 | 12 | 11 : 
                        pts = card.valeur - 9.5
                    case _: 
                        pts = 0.5
                
            player.score_manche+=pts
        return player.score_manche, player.nb_bout
    
    def compute(self, player):            
        for player, card in self.pli.items():
            if card.couleur == "Atout":
                if card.valeur == 1 or card.valeur == 21 or card.valeur == 0 :
                    pts = 4.5
                else : pts = 0.5
            else : 
                match card.valeur :
                    case 14 |13 | 12 | 11 : 
                        pts = card.valeur - 9.5
                    case _: 
                        pts = 0.5
                
            player.score_plis+=pts
        return player.score_plis

    