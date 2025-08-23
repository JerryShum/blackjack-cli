from colorama import Fore

from functions.greeting import greeting
from functions.calculate import calculate
from functions.format_and_check import format_and_check
def main():
    
    #! Greeting CLI message
    greeting()
    
    #! While loop to keep the program running
    while True:
        
        #@ Take user input for dealer and player cards
        dealer_cards = input(Fore.CYAN + "Dealer Cards: " + Fore.RESET)
        formatted_dealer = format_and_check(dealer_cards)
        if not formatted_dealer:
            continue
        
        
        player_cards = input(Fore.CYAN + "Player Cards: " + Fore.RESET)
        formatted_player = format_and_check(player_cards)
        if not formatted_player:
            continue
        
        #! Call the calculate function
        calculate(formatted_dealer, formatted_player)
    
if __name__ == "__main__":
    main()
