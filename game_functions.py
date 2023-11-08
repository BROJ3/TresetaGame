
from card import Card
from deck import Deck
from player import Player

def start_game():

    moj_spil = Deck()


    moj_spil.add_player() #adds player 1
    #moj_spil.add_player() #adds player 2
    hands = moj_spil.deal_cards(num_cards=5)

    for player in moj_spil.players:
        print(player.get_name())

    print("There are ", len(moj_spil.playing_deck_list)," cards left in the deck")

    return hands

# do I need to set hands as global variable