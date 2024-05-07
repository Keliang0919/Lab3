import Lab2.bmi as bmi

def test_bmi_under_weight():
    height_input = 1.79
    weight_input = 47
    result = bmi.calculate_bmi(height_input, weight_input)
    expected_result = -1
    assert (result == expected_result)


def test_bmi_normal__weight():
    result = bmi.calculate_bmi(1.79, 60)
    expected_result = 0
    assert (result == expected_result)


def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.79, 97)
    expected_result = 1
    assert (result == expected_result)
