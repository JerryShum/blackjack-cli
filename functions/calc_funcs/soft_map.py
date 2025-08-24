def soft_map(total_soft, total_dealer):
    
    #! Basic Strategy
    # S = Stand
    # H = Hit
    # D = Double Down otherwise Hit
    # G = Double Down otherwise Stand
        
    
    #@ Strategy for soft hands (aces counted as 1 or 11)
    soft_hands_strategy_chart = [
        # Dealer up cards
        # 2,   3,   4,   5,   6,   7,   8,   9,   10,  A
        ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # A,9 / 20
        ['S', 'S', 'S', 'S', 'G', 'S', 'S', 'S', 'S', 'S'],  # A,8 / 19
        ['G', 'G', 'G', 'G', 'G', 'S', 'S', 'H', 'H', 'H'],  # A,7 / 18
        ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # A,6 / 17
        ['H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # A,5 / 16
        ['H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # A,4 / 15
        ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # A,3 / 14
        ['H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # A,2 / 13
    ]
    
    soft_total_map = {
        # total_soft -> chart index
        20: 0,
        19: 1,
        18: 2,
        17: 3,
        16: 4,
        15: 5,
        14: 6,
        13: 7
    }
    
    dealer_map = {
        1: 10,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
    }
    
    
    chart_index = soft_total_map[total_soft]
    dealer_index = dealer_map[total_dealer]
    
    return soft_hands_strategy_chart[chart_index][dealer_index]