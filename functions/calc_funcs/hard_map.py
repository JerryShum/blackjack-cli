def hard_map(total_player, total_dealer):
    #! Basic Strategy
    # S = Stand
    # H = Hit
    # D = Double Down otherwise Hit
    # G = Double Down otherwise Stand
        
    
    #@ Strategy for hard hands (no aces)
    hard_hands_strategy_chart = [
        # Dealer up cards
        # 2,   3,   4,   5,   6,   7,   8,   9,   10,  A
        ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],  # Hard 20
        ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],  # Hard 19
        ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],  # Hard 18
        ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"],  # Hard 17
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # Hard 16
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # Hard 15
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # Hard 14
        ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],  # Hard 13
        ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],  # Hard 12
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],  # Hard 11
        ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],  # Hard 10
        ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],  # Hard 9
        ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],  # Hard 8
    ]
    
    hard_total_map = {
        # total_player -> chart index
        20: 0,
        19: 1,
        18: 2,
        17: 3,
        16: 4,
        15: 5,
        14: 6,
        13: 7,
        12: 8,
        11: 9,
        10: 10,
        9: 11,
        8: 12
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
    
      
    
    if total_player <=8:
        chart_index = hard_total_map[8]
    else:
        chart_index = hard_total_map[total_player]

    dealer_index = dealer_map[total_dealer]
    
    
    return hard_hands_strategy_chart[chart_index][dealer_index]