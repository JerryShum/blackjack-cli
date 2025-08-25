from colorama import Fore

from functions.greeting import greeting
from functions.calculate import calculate
from functions.format_and_check import format_and_check
from functions.action_handler import action_handler
def main():
    
    #! Greeting CLI message
    greeting()
    
    #! While loop to keep the program running
    while True:
        
        #@ Take user input for dealer and player cards
        dealer_card = input(Fore.CYAN + "Dealer Card (The card that the dealer shows): " + Fore.RESET)
        formatted_dealer = format_and_check(dealer_card, dealer=True)
        if not formatted_dealer:
            continue
        
        
        player_cards = input(Fore.CYAN + "Player Cards (The cards that the player has): " + Fore.RESET)
        formatted_player = format_and_check(player_cards, dealer=False)
        if not formatted_player:
            continue
        

        #@ Secondary loop for calculating and hitting cycle
        while True:
            #! Call the calculate function
            action = calculate(formatted_dealer, formatted_player)
            print(Fore.YELLOW + "-------------------------------------------------------------------------")
            print(action_handler(action))
            
            if action == "H":
                print(Fore.YELLOW + "-------------------------------------------------------------------------")
                wants_hit_again = input(Fore.GREEN + "🤔 Since we suggested you to hit again, Would you like to input your new card? (y/n): " + Fore.RESET)
                if wants_hit_again.lower() == "y":
                    #@ Player wants to hit -> take new card 
                    
                    print(Fore.YELLOW + "-------------------------------------------------------------------------")
                    new_player_card = input(Fore.CYAN + "New card that you just got from hitting :" + Fore.RESET)
                    
                    ## Append the new card to the player's hand
                    
                    formatted_player.append(new_player_card)
                    reformat_string = ",".join(formatted_player)
                    reformat_player_hand = format_and_check(reformat_string, dealer=False)
                    if not reformat_player_hand:
                        continue
                    
                    ## Set the "player_cards" variable to the new player hand
                    formatted_player = reformat_player_hand
                    
                elif wants_hit_again.lower()=="n":
                    #@ Player does not want to hit again -> break and end the game/round
                    break
                else:
                    #@ Invalid input -> reprompt
                    print(Fore.YELLOW + "-------------------------------------------------------------------------")
                    print(Fore.RED + "Invalid input. Please type 'y' or 'n'." + Fore.RESET)
                    continue
            elif action == "L":
                break
            else:
                print(Fore.YELLOW + "-------------------------------------------------------------------------")
                print(Fore.GREEN + "🤓🙏 Good luck on your hand! Thanks for using this tool." + Fore.RESET)
                break
        
        
        #! Ask the user if they want to play again
        print(Fore.YELLOW + "-------------------------------------------------------------------------")
        wants_to_play_again = input(Fore.GREEN + "🤔 Would you like to start a new round? (y/n): " + Fore.RESET)
        
        if wants_to_play_again.lower() == "y":
            print(Fore.YELLOW + "-------------------------------------------------------------------------")
            continue
        
        elif wants_to_play_again.lower() == "n":
            print(Fore.YELLOW + "-------------------------------------------------------------------------")
            print(Fore.GREEN + "😁 Thank you for your time and for using this tool. Have a great day!" + Fore.RESET)   
            break;
                
    
if __name__ == "__main__":
    main()
