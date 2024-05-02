import price_info as price

def test_total_cost_shopping():
    total_cost = 46.75
    assert (price.total_cost_shopping() == 46.75)



def test_cost_of_fruit():
    cost_of_fruits = 12
    fruit = 'apple'
    assert (price.cost_of_fruits(fruit, 10) == 1.2)

