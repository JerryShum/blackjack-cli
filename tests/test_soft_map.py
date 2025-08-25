from functions.calc_funcs.soft_map import soft_map

def test_soft_map_stand():
    # Player total, Dealer total
    assert soft_map(20,1) == "S"
    assert soft_map(20,2) == "S"
    assert soft_map(20,3) == "S"
    assert soft_map(20,4) == "S"
    assert soft_map(20,5) == "S"
    assert soft_map(20,6) == "S"
    assert soft_map(20,7) == "S"
    assert soft_map(20,8) == "S"
    assert soft_map(20,9) == "S"
    assert soft_map(20,10) == "S"
    
