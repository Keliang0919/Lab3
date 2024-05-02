import Lab2.bmi as bmi

def test_bmi_under_weight(bmi):
    assert bmi.calc_bmi(height = 1.79, weight = 57) == -1
    return -1


def test_bmi_normal__weight(bmi):
    assert bmi.calc_bmi(height = 1.79, weight = 67) == 0
    return 0


def test_bmi_over_weight(bmi):
    assert bmi.calc_bmi(height = 1.79, weight = 87) == 1
    return 1