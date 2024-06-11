from random import * 

class Card:
    def __init__(self, valeur = None, couleur=None, est_atout=False):
        self.valeur = valeur
        self.couleur = couleur
        self.est_atout = est_atout
        self.chien = []
        self.new_chien = []
        self.couleurs = ["Pique", "Carreaux", "Coeur", "Trèfle"]
        self.valeurs =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.valeurs_atout =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    
    def create_deck(self): 
        self.paquet = []
        for couleur in self.couleurs:
            for valeur in self.valeurs :
                self.paquet.append(Card(valeur, couleur, False))    
        # Ajoutez les cartes d'atout, 0 sera l'excuse
        for i in self.valeurs_atout:
            self.paquet.append(Card(i, "Atout", True))
        shuffle(self.paquet)
        # for num, card in enumerate(self.paquet):
        #     print(f"{self.paquet[num].valeur} {self.paquet[num].couleur}")
        print("paquet créé et cartes mélangées")
    
    def deal_cards (self, nb_player, list_player):# distribuer les cartes en fonction nombre de joueur (15 à 5 + 3 chien, 18+6chien à 4)    
        shuffle(self.paquet)
        if nb_player == 4 :
            for num, player in enumerate(list_player): 
                player.hand = self.paquet[18*num:18*(num+1)]
                print(f"cartes distribuées à {player.name} ")
            self.chien = self.paquet[72:78]
                
        elif nb_player == 5 :
            for num, player in enumerate(list_player): 
                player.hand = self.paquet[15*num:15*(num+1)]
                
                print(f"cartes distribuées à {player.name} ")
            self.chien = self.paquet[76:78]    

    def sortCard(self, list_player):
        for player in list_player :
            self.couleurs.append("Atout")
            player.hand.sort(reverse = True, key=self.card_sort_key)
            self.couleurs.remove("Atout")   
                
    def card_sort_key(self, card):
        color_index = self.couleurs.index(card.couleur)
        if card.couleur == "Atout" :
            value_index = self.valeurs_atout.index(card.valeur)
        else : value_index = self.valeurs.index(card.valeur)
        return (color_index, value_index)     
                
                
            
            
                        
        