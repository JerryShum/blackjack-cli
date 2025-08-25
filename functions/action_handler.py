from colorama import Fore

def action_handler(action):
    action_map = {
        "H": Fore.MAGENTA + "Hit",
        "S": Fore.MAGENTA +"Stand",
        "D": Fore.MAGENTA +"Double Down",
        "G": Fore.MAGENTA +"Double Down",
        "W": Fore.MAGENTA +"Blackjack",
        "L" : Fore.MAGENTA +"Lose"
    }
    
    if action not in action_map:
        return f"ERROR: Invalid action: {action}"
    
    if action == "W":
        return Fore.GREEN + f"🎉 Congratulations! You hit a BlackJack! Enjoy your earnings."
    elif action == "L":
        return Fore.RED + f"😭 You lost. Better luck next time!"
    
    return Fore.GREEN + f"🤓 According to our calculations, I think you should: {action_map[action]}" + Fore.RESET