from colorama import Fore

def format_check(cards):
    card_list = cards.replace(',', ' ').split()
    
    for card in card_list:
        if card not in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
            print(Fore.RED + "Invalid input. Please enter cards in the format 'A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2'. With either a space or a comma between each card.")
            return False

    return True