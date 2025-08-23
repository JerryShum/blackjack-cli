from colorama import Fore, Style, init, Back
import pyfiglet

def greeting():
    # Initialize Colorama
    init(autoreset=True)

    #! Use figlet to create ASCII art for the welcome message
    welcome_art = pyfiglet.figlet_format("BLACKJACK CLI", font="slant")
    
    #@ Print the ASCII art in red
    print(Fore.RED + welcome_art)
    print(Fore.YELLOW + "-------------------------------------------------------------------------")

    # Accept user input
    print(Fore.GREEN + "This is BLACKJACK CLI. A simple CLI application that tells you the best action to take in a blackjack game. \nIt works by analyzing the cards in your hand and the dealer's hand. It will tell you if you should hit, stand, or double down. " )
    print(Fore.YELLOW + "-------------------------------------------------------------------------")
    print(Fore.GREEN + "In the future, I plan to expand upon this project using computer vision to analyze the cards either through a camera or through your screen. But for now, you have to input your cards manually.")
    print(Fore.YELLOW + "-------------------------------------------------------------------------")
    print(Fore.GREEN + "Let's get started! Type 'start' to begin." + Style.RESET_ALL)
    
    user_input = input("-> ")
    
    if user_input == "start":
        print(Fore.YELLOW + "-------------------------------------------------------------------------")
        print(Fore.GREEN + "Great! Let's begin.")
        print(Fore.YELLOW + "-------------------------------------------------------------------------")
    else:
        print(Fore.RED + "Invalid input. Please type 'start' to begin.")
        greeting()
    
    
    
    
    
    
    