import pytest

from lab import *


@pytest.fixture
def sample_flowers():
    rose = Flower(20, "Medium", "Red", {"price": 200, "quantity": 10, "delivery_rate": 5})
    tulip = Flower(15, "Small", "Yellow", {"price": 300, "quantity": 20, "delivery_rate": 4})
    lily = Flower(25, "Large", "White", {"price": 400, "quantity": 30, "delivery_rate": 3})
    return rose, tulip, lily


@pytest.fixture
def flower_shop(sample_flowers):
    flower_shop = FlowerShop()
    for flower in sample_flowers:
        flower_shop.add_flower_to_shop(flower)
    return flower_shop


@pytest.fixture
def sample_bouquet(sample_flowers):
    bouquet = Bouquet()
    bouquet.add_flower_to_bouquet(sample_flowers[0], 3)
    bouquet.add_flower_to_bouquet(sample_flowers[1], 5)
    return bouquet


def test_flower_attributes():
    rose = Flower(20, "Medium", "Red", {"price": 400, "quantity": 30, "delivery_rate": 25})
    assert rose.get_height() == 20
    assert rose.get_size() == "Medium"
    assert rose.get_color() == "Red"
    assert rose.get_price() == 400
    assert rose.get_quantity() == 30
    assert rose.get_delivery_rate() == 25


def test_flower_shop_initialization():
    flower_shop = FlowerShop()
    assert len(flower_shop.list_of_flowers_in_shop) == 0


def test_add_flower_to_shop(flower_shop):
    assert len(flower_shop.list_of_flowers_in_shop) == 3


def test_delete_flower_to_shop(flower_shop, sample_flowers):
    flower_to_delete = sample_flowers[0]
    flower_shop.delete_flower_to_shop(flower_to_delete)
    assert flower_to_delete not in flower_shop.list_of_flowers_in_shop


def test_bouquet_total_price(sample_bouquet):
    assert sample_bouquet.get_total_price() == pytest.approx(2100, 0.01)


def test_top_most_expensive_flowers(flower_shop):
    sorted_flowers = flower_shop.top_most_expensive_flowers()

    assert sorted_flowers[0].get_price() == 400
    assert sorted_flowers[1].get_price() == 300
    assert sorted_flowers[2].get_price() == 200
