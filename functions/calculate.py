from colorama import Fore

def calculate(dealer_card, player_cards):
    
    print(Fore.CYAN + "Thinking..." + Fore.RESET)
    
    basic_strategy = [
        # Dealer's Upcard: 2, 3, 4, 5, 6, 7, 8, 9, 10, A
        ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],  # 8 or less
        ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],  # 9
        ["D", "D", "D", "D", "D", "H", "H", "H", "H", "H"],  # 10
        ["D", "D", "D", "D", "D", "H", "H", "H", "H", "H"],  # 11
        ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],  # 12
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # 13-16
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # 17 or more
    ]
    
    #! Card Values
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
    
    #! Get value from cards
    for card in dealer_card: 
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
        
    
    
    
    