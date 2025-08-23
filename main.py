from functions.greeting import greeting
from functions.calculate import calculate
def main():
    
    #! Greeting CLI message
    greeting()
    
    #! While loop to keep the program running
    while True:
        
        #@ Take user input for dealer and player cards
        dealer_cards = input("Dealer Cards: ")
        player_cards = input("Player Cards: ")
        
        #! Call the calculate function
        calculate(dealer_cards, player_cards)
    
if __name__ == "__main__":
    main()
