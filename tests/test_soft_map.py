from functions.calc_funcs.soft_map import soft_map

def test_soft_map_stand():
    # Player total, Dealer total
    assert soft_map(20,1) == "S"
    assert soft_map(19,2) == "S"
    assert soft_map(20,3) == "S"
    assert soft_map(19,4) == "S"
    assert soft_map(19,5) == "S"
    assert soft_map(20,6) == "S"
    assert soft_map(18,7) == "S"
    assert soft_map(18,8) == "S"
    assert soft_map(19,9) == "S"
    assert soft_map(20,10) == "S"
    
def test_soft_map_hit():
    # Player total, Dealer total
    assert soft_map(17,1) == "H"
    assert soft_map(14,2) == "H"
    assert soft_map(15,3) == "H"
    assert soft_map(14,4) == "H"
    assert soft_map(17,7) == "H"
    assert soft_map(15,8) == "H"
    assert soft_map(16,9) == "H"
    assert soft_map(17,10) == "H"
    assert soft_map(16,2) == "H"
    assert soft_map(13,1) == "H"
    
def test_soft_map_double_hit():
    # Player total, Dealer total
    assert soft_map(13,5) == "D"
    assert soft_map(14,6) == "D"
    assert soft_map(13,6) == "D"
    assert soft_map(15,4) == "D"
    assert soft_map(16,4) == "D"
    
def test_soft_map_double_stand():
    # Player total, Dealer total
    assert soft_map(18,2) == "G"
    assert soft_map(18,3) == "G"
    assert soft_map(18,4) == "G"
    assert soft_map(18,5) == "G"
    assert soft_map(19,6) == "G"
    
    
