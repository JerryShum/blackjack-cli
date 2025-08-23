from colorama import Fore

def format_and_check(cards, dealer):
    
    card_list = cards.replace(',', ' ').split()
    
    if dealer and len(card_list) != 1:
        print(Fore.RED + "Invalid input. Please enter a single card for the dealer, since they should only have 1 card showing.")
        return False
    elif not dealer and len(card_list) < 2:
        print(Fore.RED + "Invalid input. Please enter all of your cards in the format 'A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2'. With either a space or a comma between each card.")
        return False
    
    for card in card_list:
        if card.upper() not in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
            print(Fore.RED + "Invalid input. Please enter cards in the format 'A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2'. With either a space or a comma between each card.")
            return False

    return card_list

