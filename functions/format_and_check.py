from colorama import Fore

def format_and_check(cards, dealer):
    
    card_list = cards.replace(',', ' ').split()
    ## Make all cards uppercase
    card_list = [card.upper() for card in card_list]
    
    #@ Dealer should have only 1 card
    if dealer and len(card_list) != 1:
        print(Fore.RED + "Invalid input. Please enter a single card for the dealer, since they should only have 1 card showing.")
        return False
    
    #@ Player hand should have atleast 2 cards
    elif not dealer and len(card_list) < 2:
        print(Fore.RED + "Invalid input. Please enter all of your cards in the format 'A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2'. With either a space or a comma between each card.")
        return False
    
    #@ Handle
    
        
    for card in card_list:
        if card not in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
            print(Fore.RED + "Invalid input. Please enter cards in the format 'A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2'. With either a space or a comma between each card.")
            return False

    return card_list

