from functions.calc_funcs.hard_map import hard_map

def test_hard_map_stand():
    # Player total, Dealer total
    assert hard_map(17,1) == "S"
    assert hard_map(18,1) == "S"
    assert hard_map(20,2) == "S"
    assert hard_map(14,2) == "S"
    assert hard_map(14,3) == "S"
    assert hard_map(17,3) == "S"
    assert hard_map(20, 10) == "S"
    assert hard_map(12,4) == "S"
    assert hard_map(13,6) == "S"
    assert hard_map(15,4) == "S"
    
def test_hard_map_hit():
    # Player total, Dealer total
    assert hard_map(8,1) == "H"
    assert hard_map(8,10) == "H"
    assert hard_map(12,9) == "H"
    assert hard_map(12,10) == "H"
    assert hard_map(13,1) == "H"
    assert hard_map(13,10) == "H"
    assert hard_map(14,10) == "H"
    assert hard_map(15,10) == "H"
    assert hard_map(16,1) == "H"
    assert hard_map(12,9) == "H"
    
def test_hard_map_double():
    # Player total, Dealer total
    assert hard_map(9,3) == "D"
    assert hard_map(9,4) == "D"
    assert hard_map(9,5) == "D"
    assert hard_map(9,6) == "D"
    assert hard_map(10,2) == "D"
    assert hard_map(10,3) == "D"
    assert hard_map(10,4) == "D"
    assert hard_map(10,5) == "D"
    assert hard_map(10,6) == "D"
    assert hard_map(10,7) == "D"
    
    
    