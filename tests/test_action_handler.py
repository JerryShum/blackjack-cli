from colorama import Fore
from functions.action_handler import action_handler

def test_action_handler_H():
    # Test action handler with value of H (hit)
    assert action_handler("H") == Fore.GREEN + f"🤓 According to our calculations, I think you should: " + Fore.MAGENTA + "Hit" + Fore.RESET
    
def test_action_handler_S():
    # Test action handler with value of S (stand)
    assert action_handler("S") == Fore.GREEN + f"🤓 According to our calculations, I think you should: " + Fore.MAGENTA + "Stand" + Fore.RESET
    
def test_action_handler_D():
    # Test action handler with value of D (double down)
    assert action_handler("D") == Fore.GREEN + f"🤓 According to our calculations, I think you should: " + Fore.MAGENTA + "Double Down if allowed, otherwise Hit" + Fore.RESET
    
def test_action_handler_G():
    # Test action handler with value of G (double down)
    assert action_handler("G") == Fore.GREEN + f"🤓 According to our calculations, I think you should: " + Fore.MAGENTA + "Double Down if allowed, otherwise Stand" + Fore.RESET
    
def test_action_handler_W():
    # Test action handler with value of W (win)
    assert action_handler("W") == Fore.GREEN + f"🎉 Congratulations! You hit a BlackJack! Enjoy your earnings."
    
def test_action_handler_L():
    # Test action handler with value of L (lose)
    assert action_handler("L") == Fore.RED + f"😭 You lost. Better luck next time!"
    

    