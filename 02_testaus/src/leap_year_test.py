from leap_year import is_leap_year


def test_year_2004_is_leap_year():
    assert is_leap_year(2004) == True


def test_year_2008_is_leap_year():
    assert is_leap_year(2008) == True


def test_year_2020_is_leap_year():
    assert is_leap_year(2020) == True


def test_year_1999_is_not_leap():
    assert is_leap_year(1999) == False


def test_year_2021_is_not_leap():
    assert is_leap_year(2021) == False


def test_years_divisible_by_100_are_not_leap():
    assert not is_leap_year(2100)
    assert not is_leap_year(2200)


def test_years_divisible_by_400_are_leap_year():
    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True
