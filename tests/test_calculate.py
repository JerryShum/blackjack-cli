from functions.calculate import calculate

def test_calculate_hard_8():
    assert calculate(["A"], ["5", "3"]) == "H"

def test_calculate_soft_18():
    assert calculate(["A"], ["A", "7"]) == "H"

def test_calculate_hard_21():
    assert calculate(["J"], ["10", "9"]) == "S"

def test_calculate_soft_19():
    assert calculate(["A"], ["A", "8"]) == "S"

def test_calculate_hard_20():
    assert calculate(["10"], ["10", "10"]) == "S"

def test_calculate_hard_20_3():
    assert calculate(["8"], ["10", "5", "5"]) == "S"
    
def test_calculate_ace():
    assert calculate(["A"], ["A", "5", "A"]) == "H"
    
def test_calculate_two_hand_blackjack():
    assert calculate(["A"], ["10", "A"]) == "W"
    
def test_calculate_blackjack():
    assert calculate(["A"], ["10", "5", "6"]) == "W"

def test_calculate_lose():
    assert calculate(["A"], ["10", "5", "4", "10"]) == "L"