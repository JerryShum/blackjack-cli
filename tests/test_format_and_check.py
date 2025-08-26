from functions.format_and_check import format_and_check

def test_format_and_check_player():
    assert format_and_check("A", False) == False
    assert format_and_check("5", False) == False
    assert format_and_check("A K", False) == ["A", "K"]
    assert format_and_check("A 2", False) == ["A", "2"]
    assert format_and_check("A 2 3", False) == ["A", "2", "3"]
    assert format_and_check("A, 2 3 4 5 6 7 8 9 10", False) == ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    assert format_and_check("A 2 3, 4 5 6 7 8 9 10, J", False) == ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J"]
    assert format_and_check("A, 2 3, 4 ,5 6, 7 ,8 9 10 J Q", False) == ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q"]
    assert format_and_check("A 2 3 4 5 6, 7 8 9, 10 J Q K", False) == ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    assert format_and_check("J, K", False) == ["J", "K"]
    

def test_format_and_check_dealer():
    assert format_and_check("A", True) == ["A"]
    assert format_and_check("5", True) == ["5"]
    assert format_and_check("10", True) == ["10"]
    assert format_and_check("A K", True) == False
    assert format_and_check("A 2", True) == False
    assert format_and_check("A 2 3", True) == False
    assert format_and_check("A, 2", True) == False
    assert format_and_check("A, 2 3", True) == False
    assert format_and_check("A, 2, 3", True) == False
    assert format_and_check("A, 2, 3, 4", True) == False
    
    
