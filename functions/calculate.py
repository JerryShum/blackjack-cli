from colorama import Fore
from functions.calc_funcs.soft_map import soft_map
from functions.calc_funcs.hard_map import hard_map

def calculate(dealer_card, player_cards):
    
    print(Fore.YELLOW + "-------------------------------------------------------------------------")
    print(Fore.CYAN + "Thinking..." + Fore.RESET)
    

    #! Card Values
    # Ace starts as 1 so that we don't have to do -10 each time we see an ace in the future 
    card_values = {
        "A": 1, 
        "K": 10,
        "Q": 10,
        "J": 10,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }
    
    #! Initialize total values
    total_dealer = 0
    total_player = 0
    total_soft = None
    
    
    #! Get value from cards
    for card in dealer_card: 
        total_dealer += card_values[card.upper()]
    for card in player_cards:
        total_player += card_values[card.upper()]
    
    print(Fore.MAGENTA + "DEALER TOTAL: ", total_dealer, Fore.RESET)        
    print(Fore.MAGENTA + "PLAYER TOTAL: ", total_player, Fore.RESET)    
    
    #! If player busts, return L
    if total_player > 21:
        #@ If player total is over 21, they lose the game
        return "L"
    
    # ---
    
    #@ Detect if player has an ace (soft hand handling)
    player_has_ace = "A" in player_cards
        
    #! Check for blackjack (multiple cards)
    #@ Checks for blackjack with ace = 1
    if total_player == 21:
        return ("W")
    
            
    ## Calculate soft hand
    if player_has_ace:
        # soft total = total_player + 10 if total_player is less than 21 else its just the same as total_player
        # also handles edge cases of 2+ aces (only adds +10 once)
        total_soft = total_player + 10 if total_player + 10 <= 21 else None

        
        #@ Checks for blackjack with ace = 11
        if total_soft == 21:
            return ("W")
        
        
    #! Map soft total 
    if total_soft and total_soft >= 13:
        action = soft_map(total_soft, total_dealer)
        return action
    elif total_soft and total_soft <= 12:
        #@ If soft total is less than 13, map to hard total
        action = hard_map(total_soft, total_dealer)
        return action
    else:
        #@ If no soft total, map to hard total
        action = hard_map(total_player, total_dealer)
        return action

    
    
    
    