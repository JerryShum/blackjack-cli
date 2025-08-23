from colorama import Fore

from functions.greeting import greeting
from functions.calculate import calculate
from functions.format_check import format_check
def main():
    
    #! Greeting CLI message
    greeting()
    
    #! While loop to keep the program running
    while True:
        
        #@ Take user input for dealer and player cards
        dealer_cards = input(Fore.CYAN + "Dealer Cards: " + Fore.RESET)
        if not format_check( dealer_cards):
            continue
        
        
        player_cards = input(Fore.CYAN + "Player Cards: " + Fore.RESET)
        if not format_check(player_cards):
            continue
        
        #! Call the calculate function
        calculate(dealer_cards, player_cards)
    
if __name__ == "__main__":
    main()
