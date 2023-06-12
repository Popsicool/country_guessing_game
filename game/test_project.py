from project import check_choice

def test_check_choice():
    '''
    test choice
    '''
    assert check_choice(1) == (1)
    assert check_choice(2) == (2)
    assert check_choice("q") == ("q")
    assert check_choice("Q") == ("Q")
    assert check_choice(12) == False
