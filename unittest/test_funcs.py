# TODO: 사용자 모듈 import


# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
# def test_always():
#     a = "i'm a boy!"
#     assert "i'm a boy!" == a, "Remove me!"

# def test_my_first_testcase():
#     l = [1, 2, 3, 4]
#     assert l == [1, 2, 3, 4, 5]


from my_funcs import is_even, average, max_value, min_value


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True


def test_average():
    assert average([1, 2, 3, 4]) == 2.5
    assert average([10, 20]) == 15


def test_max_value():
    assert max_value([1, 2, 3, 4]) == 4
    assert max_value([-1, -2, -3]) == -1


def test_min_value():
    assert min_value([1, 2, 3, 4]) == 1
    assert min_value([-1, -2, -3]) == -3
