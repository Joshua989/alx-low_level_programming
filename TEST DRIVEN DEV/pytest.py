def test_add_positive_numbers():
    result = add_numbers(2, 3)
    assert result == 5

def test_add_negative_numbers():
    result = add_numbers(-2, -3)
    assert result == -5

def test_add_zero():
    result = add_numbers(10, 0)
    assert result == 10
