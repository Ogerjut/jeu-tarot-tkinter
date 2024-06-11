###################################################################################################
##### // frame info : point att en cours (a revoir), cartes dans le chien (bout, roi, atout?)
##### si pas tour peut pas acceder textbox, clique sur chien retire aussi carte de new chien ??
##### jeu à 5 (appel roi), regle chien fin de game (classement, calcul points)
##### Revoir design des widgets ajouter des labels (joueur qui a pris en valeur, couleur demandée )
# trouver bug 
##################################################################################################

from customtkinter import *
from random import *

from game import Game
from player import Player
from cards import Card
from enchere import Enchere
from infobar import InfoBar

class AppGame:
    def __init__(self) -> None:
        self.root = CTk()
        self.root.title("Jeu de Tarot")
        self.root.minsize(640, 640)
        #self.window.iconbitmap("logo.ico")
        self.root.config(background="alice blue")
        self.game = Game()
        self.player = Player(None, None)
        self.cards = Card()
        self.enchere  = Enchere()
        self.game.setNbPlayers(self.root, self.startGame)
           
#------------EVENT CLICK---------------
    def startGame(self, button):
        button_text = button.cget("text")
        match button_text : 
            case "4 JOUEURS" : self.setPlayers(4)
            case "5 JOUEURS" : self.setPlayers(5)
         
    def onSegmentedButton(self, value):
        # print(f"{self.game.player_enchere.name} mise une {value}") input log
        self.current_player.a_mise = True
        self.enchere.setBet(value, self.current_player)
        self.enchereUpdate()
        
    def SkipButton(self):
        print(f"{self.current_player.name} passe")
        self.current_player.a_mise = True
        self.enchereUpdate()

    def onClickedCard(self, event):
        if self.enchere.isDone and not self.game.set_chien :
            self.onClickHandChien(event)
        
        if self.enchere.isDone and self.game.set_chien : 
            self.current_player.win_round = False
            card = self.getCard(event, self.current_player.text, self.current_player.hand)   
            if self.game.checkCard(card, self.current_player.hand) :
                self.playCard(card)
                self.pliIsdone()
                self.endRoundOrGame()        
                                
    def onClickedChien(self, event) :
        if len(self.cards.chien) != 0 :
            card = self.getCard(event, self.game.chien_text, self.cards.chien)
            self.transferCard(card, self.cards.chien, self.chien_player.hand)
            self.game.updateTextList(self.game.chien_text, self.cards.chien)
            self.chien_player.update()
            self.cards.sortCard(self.game.list_player)
            
    def onClickedNouveauChien(self, event):
        if len(self.cards.new_chien) != 0 :
            card = self.getCard(event, self.game.new_chien_text, self.cards.new_chien)
            self.transferCard(card,self.cards.new_chien , self.chien_player.hand)
            self.game.updateTextList(self.game.new_chien_text, self.cards.new_chien)
            self.cards.sortCard(self.game.list_player)
            self.chien_player.update()
     
    def onClickHandChien(self, event):
        max = 6 if self.game.nb_j == 4 else 3
        if len(self.cards.new_chien) < max :
            card = self.getCard(event, self.chien_player.text, self.chien_player.hand)
            self.transferCard(card, self.chien_player.hand, self.cards.new_chien)
            self.game.updateTextList(self.game.new_chien_text, self.cards.new_chien)
            self.chien_player.update()
            self.cards.sortCard(self.game.list_player)
        
    def okChien(self):
        max = 6 if self.game.nb_j == 4 else 3
        if len(self.cards.new_chien) == max and len(self.cards.chien) == 0 :
            self.enchere.isDone = False
            self.game.set_chien = True
            self.game.roundIsRunning = True
            self.game.nb_round_max = len(self.current_player.hand)
            self.info = InfoBar(self.root)
            self.game.chien_frame.after_cancel(self.id_chien)
            self.remove_widget(self.game.table)
            self.setInfo()
            self.game.frame(self.root)
            self.id_game = self.game.table.after(100, self.updateTimerGame)
        else : print("Constitue le chien !")
    
    def startNewGame(self):
        self.defaultGameParameters()
        self.remove_widget(self.root)
        self.game.setNbPlayers(self.root, self.startGame)
    
    def transferCard(self, card, source=list, destination=list):
        source.remove(card)
        destination.append(card)
             
# -----------FRAMES--------------------  
    def setPlayers(self, nb_joueur):
        self.game.nb_j = nb_joueur
        self.remove_widget(self.root)
        match nb_joueur :
            case 4 : pos_table = [(2,1),(1,2) ,(0,1), (1,0)]
            case 5 : pos_table = [(0,0),(2,0) ,(1,3), (3,3), (3,1)]
        for i in range(nb_joueur):
            self.game.list_player.append(Player(f"Joueur {i+1}", pos_table[i]))
            self.game.list_player[i].frame(self.root, lambda event: self.onClickedCard(event))
        self.game.frame(self.root)
        self.current_player = self.game.list_player[0]
        self.setCardsEnchere()
            
    def setCardsEnchere(self):
        self.cards.create_deck()
        self.cards.deal_cards(self.game.nb_j, self.game.list_player)
        self.cards.sortCard(self.game.list_player)
        for player in self.game.list_player :
            player.update()
            player.a_mise = False
        self.enchere.frame(self.game.table, self.current_player, self.onSegmentedButton, self.SkipButton)
        self.enchere.enchere_frame.after(1000, self.updateTimerEnchere)

    def setInfo(self):
        self.info.label1.configure(text=f"Manche {self.game.nb_game} / {self.game.nb_game_max}")
        self.info.label2.configure(text=f"Round {self.game.nb_round} / {self.game.nb_round_max}")
        for player in self.game.list_player:
            if player.a_pris :
                self.info.label3.configure(text=f"L'attaque ({player.name}) marque {player.score_plis} points")
#-------------------------------------
    def remove_widget(self, frame):
        # Remove widgets from the game box
        for widget in frame.winfo_children():
            widget.destroy()
#-------------CHECK & GET & AUTRES ------------------
    
    def checkEndEnchere(self):
        count = sum(1 for player in self.game.list_player if player.a_mise)
        if count == len(self.game.list_player):
            count = 0
            if self.enchere.actual_bet != 0 :
                print("fin enchere")
                value = max(self.enchere.bet.values())
                for key, val in self.enchere.bet.items():
                    if val == value :
                        for keym, valm in self.enchere.mises.items():
                            if val == valm: 
                                self.enchere.endEnchère(key, keym)    
            else :
                print("nouvelles enchères")
                self.game.list_player = self.game.list_player[1:4] + self.game.list_player[0:1]
                self.current_player = self.game.list_player[0]
                self.enchere.actual_bet = 0
                self.setCardsEnchere()
        else :
            if self.game.list_player.index(self.current_player) <= len(self.game.list_player) :
                self.current_player  = self.game.list_player[self.game.list_player.index(self.current_player)+1]      
    
    def getCard(self, event, text_widget, list):
        index = text_widget.index(f"@{event.x},{event.y}")
        line_start_index = f"{index.split('.')[0]}.0"
        card_str = text_widget.get(line_start_index, f"{line_start_index} lineend")
        for card in list :
            varstr = str(card.valeur) + str(" ") + str(card.couleur)
            if varstr == card_str :
                return card
     
    def playCard(self, card):            
        print(f" {self.current_player.name} a joué le {card.valeur} {card.couleur}")     
        self.game.pli[self.current_player] = card
        self.current_player.hand.remove(card) 
        self.game.timer.set(0)  
        self.game.update(self.game.table_pli, self.game.pli)
        self.current_player.update()
        self.current_player = self.game.changePlayer(self.current_player)
        self.updateTimerGame()
    
    def pliIsdone(self):
        if self.game.pliIsDone :
            print("ok")
            self.current_player = self.game.list_player[0]
            self.game.nb_round +=1
            self.game.color_choosen = False
            self.game.current_color = None
            self.game.last_value_atout.clear()
            self.game.pliIsDone = False
            if len(self.current_player.hand) == 0 and len(self.game.pli) == len(self.game.list_player) :
                self.game.isOver = True
            self.game.pli = {}
            self.setInfo()
            self.game.update(self.game.table_pli, self.game.pli)
            self.game.pli_label.configure(text=f"{self.current_player.name} va jouer")
            self.game.timer.set(0)
             
    def endRoundOrGame(self): 
        if self.game.isOver : 
            self.game.show_rank = True
            self.game.computePointsRound(self.cards.new_chien)
            # self.game.computePointsGame()
            self.game.table.after_cancel(self.id_game)
            print(self.game.nb_game_max, self.game.nb_game)
            if self.game.nb_game_max == self.game.nb_game :
                self.game.nb_game = 1
                for player in self.game.list_player :
                    if player.winner_game :               
                        print(f"{player.name} a gagné la partie avec un score de {player.score_game}")
                        player.winner_game = False
                    player.bonus = 1
                    player.score_game = 0
                self.game.frameGameOver(self.startNewGame)
                self.game.updateRank()
                self.game.isOver = False 
     
            else :
                print("Nouvelle manche")
                self.game.nb_game +=1
                self.remove_widget(self.game.table)
                self.game.frameGameOver(self.startNewGame)
                self.id_rank = self.game.g_o_frame.after(1000, self.updateTimerRank)
                self.game.updateRank() 
                self.defaultGameParameters()
                           
    def defineRandCard(self):
        self.possible_card = [card for card in self.current_player.hand if self.game.checkCard(card, self.current_player.hand )]
        if len(self.possible_card) != 0 : 
            nb = randint(0, len(self.possible_card)-1) 
            card = self.possible_card[nb]
            self.possible_card.clear()
            self.playCard(card)
            self.pliIsdone()
            self.endRoundOrGame()
    
    def defaultGameParameters(self):
        self.game.nb_round = 1
        self.enchere.actual_bet = 0
        self.game.set_chien = False
        self.game.roundIsRunning = False
        self.game.show_rank = False
        self.cards.chien.clear()
        self.enchere.list_disable_option.clear()
        self.cards.new_chien.clear()
        for player in self.game.list_player:
            player.a_mise = False
            if player.a_pris : 
                player.a_pris = False
                player.first_to_play = False
                # + autre chose ? 
                player.label.configure(text=player.name)
        self.game.rank = {}
        self.game.list_player.clear()
        print("paramètres jeu remis à 0")          
#-------------UPDATES-----------------
    def updateTimerEnchere(self):
        current_value = self.enchere.timer.get()
        self.enchere.timer.set(current_value + 0.04) 
        if current_value < 1:
            self.id_enchere = self.enchere.enchere_frame.after(500, self.updateTimerEnchere)  # Appel récursif toutes les 1000 ms
        else : 
            self.enchereUpdate()
            self.enchere.timer.set(0)
            
    def updateTimerGame(self):
        current_value = self.game.timer.get()
        self.game.timer.set(current_value + 1) 
        if current_value < 1:
            self.id_game = self.game.table.after(10, self.updateTimerGame)  # Appel récursif toutes les 1000 ms
        else : 
            self.defineRandCard()
    
    def updateTimerChien(self):
        current_value = self.game.chien_timer.get()
        self.game.chien_timer.set(current_value + 0.02) 
        if current_value < 1:
            self.id_chien = self.game.chien_frame.after(500, self.updateTimerChien)  # Appel récursif toutes les 1000 ms
        else : 
            print("chien fait au hasard")
            # passe au 1er tour
    
    def updateTimerRank(self):
        current_value = self.game.end_round_timer.get()
        self.game.end_round_timer.set(current_value + 0.1) 
        if current_value < 1:
            self.id_rank = self.game.g_o_frame.after(500, self.updateTimerRank)  # Appel récursif toutes les 1000 ms
        else :
            self.game.end_round_timer.set(0)
            self.game.g_o_frame.after_cancel(self.id_rank)
            self.game.show_rank = False
            self.game.isOver = False
            self.setCardsEnchere()
            
    def enchereUpdate(self):
        self.enchere.list_disable_option.clear()  
        for num, mise in enumerate(self.enchere.mises):
            if num < self.enchere.actual_bet :
                self.enchere.list_disable_option.append(mise)
        
        self.checkEndEnchere()
        self.remove_widget(self.game.table)
        if not self.enchere.isDone : 
            self.enchere.frame(self.game.table, self.current_player, self.onSegmentedButton, self.SkipButton)
            self.enchere.enchere_frame.after(100, self.updateTimerEnchere)
        else : 
            self.current_player = self.game.list_player[0]
            self.game.frame(self.root) 
            for player in self.game.list_player :
                player.a_mise = False
                if player.a_pris : 
                    player.labelAPris(self.enchere.mise)
                    self.chien_player = player           
            self.game.frameChien(self.onClickedChien, self.onClickedNouveauChien, self.okChien)
            self.id_chien = self.game.chien_frame.after(200, self.updateTimerChien)
            self.game.activateChien(self.onClickedChien, self.onClickedNouveauChien)
            self.game.updateTextList(self.game.chien_text, self.cards.chien)
            # self.updateTimerEnchere
            self.enchere.enchere_frame.after_cancel(self.id_enchere)
            
    def runApp(self) : 
        self.root.mainloop()
        
if __name__ == "__main__" :
    app = AppGame()
    app.runApp()