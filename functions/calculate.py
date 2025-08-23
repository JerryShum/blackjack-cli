from colorama import Fore

def calculate(dealer_cards, player_cards):
    
    print(Fore.CYAN + "Thinking..." + Fore.RESET)
    
    #! Dictionary of card values
    card_values = {
        'A': 11,
        'K': 10,
        'Q': 10,
        'J': 10,
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }
    
    #! Initialize total values
    total_dealer = 0
    total_player = 0
    
    #! Get value from cards
    for card in dealer_cards:
        total_dealer += card_values[card.upper()]
    for card in player_cards:
        total_player += card_values[card.upper()]
    
    #! Print totals
    print(Fore.CYAN + "Dealer Total: " + Fore.RESET, total_dealer)
    print(Fore.CYAN + "Player Total: " + Fore.RESET, total_player)
    
    #! Check for blackjack
    if total_dealer == 21 and total_player == 21:
        print(Fore.GREEN + "Blackjack! You win!" + Fore.RESET)
    elif total_dealer == 21 and total_player != 21:
        print(Fore.RED + "Dealer has blackjack. You lose." + Fore.RESET)
        
    
    
    
    