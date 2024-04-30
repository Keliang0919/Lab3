import Lab2.bmi as bmi

def test_bmi_under_weight(bmi):
    height_input = 1.73
    weight_input = 57
    calc_bmi = weight_input/(height_input*height_input)
    if calc_bmi < 18.5:
        assert (calc_bmi < 18.5)
        return


def test_bmi_normal__weight(bmi):
    height_input = 1.73
    weight_input = 57
    calc_bmi = weight_input/(height_input*height_input)
    if 18.5 < calc_bmi < 25.0:
        assert (18.5 < calc_bmi < 25)
        result1 = print("Normal Weight")
        return result1


def test_bmi_over_weight(bmi):
    height_input = 1.73
    weight_input = 57
    calc_bmi = weight_input/(height_input*height_input)
    if bmi > 25.0:
        assert (calc_bmi> 25.0)
        result2 = print("Overweight")
        return result2