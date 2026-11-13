from pricing import shipping_cost


def test_free_shipping():
    assert shipping_cost(200) == 0


def test_medium_shipping():
    assert shipping_cost(150) == 15


def test_regular_shipping():
    assert shipping_cost(50) == 30
