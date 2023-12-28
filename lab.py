"""lab5"""


class Flower:
    """
    class Flower
    """
    __height = None
    __size = None
    __color = None
    __details = {}

    def get_height(self):
        """
            The func returns height
            :return:
            """
        return self.__height

    def get_size(self):
        """
            The func returns size
            :return:
            """
        return self.__size

    def get_color(self):
        """
            The func returns color
            :return:
            """
        return self.__color

    def get_details(self):
        """
            The func returns details(price,quantity,delivery_rate)
            :return:
            """
        return self.__details

    def get_price(self):
        """
            The func returns price from details
            :return:
            """
        return self.__details["price"]

    def get_quantity(self):
        """
            The func returns quantity from details
            :return:
            """
        return self.__details["quantity"]

    def get_delivery_rate(self):
        """
            The func returns delivery_rate from details
            :return:
            """
        return self.__details["delivery_rate"]

    def set_height(self, new_height):
        """
              The func sets new value for height
              :param new_height: new value for price
              :return:
              """
        self.__height = new_height

    def set_size(self, new_size):
        """
              The func sets new value for size
              :param new_size: new value for price
              :return:
              """
        self.__size = new_size

    def set_color(self, new_price):
        """
              The func sets new value for color
              :param new_price: new value for price
              :return:
              """
        self.__color = new_price

    def set_details(self, new_details):
        """
              The func sets new value for details(price,quantity,delivery_rate)
              :param new_details: new value for price
              :return:
              """
        self.__details = new_details

    def __init__(self, height, size, color, details):
        """
               Class constructor
               :param height: height of flower
               :param size: size of flower that we have
               :param color: flower color
               :param details: dictionary containing price,delivery_rate and quantity of flower
               """
        self.__height = height
        self.__size = size
        self.__color = color
        self.__details = details

    def __str__(self):
        """
                The func returns object in str format
                :return:
                """
        return (f"Flower: | Height:{self.get_height()}"
                f" Price:{self.get_price()} Quantity:{self.get_quantity()}|")


class FlowerShop:
    """
        class FlowerShop
        """

    def __init__(self):
        """
                      Class constructor
                      """
        self.list_of_flowers_in_shop = []

    def add_flower_to_shop(self, flower_from_flower_shop):
        """add flower to shop"""
        self.list_of_flowers_in_shop.append(flower_from_flower_shop)

    def top_most_expensive_flowers(self):
        """print top most expensive flowers in shop"""
        sorted_list = sorted(self.list_of_flowers_in_shop,
                             key=lambda flower_from_flower_shop:
                             flower_from_flower_shop.get_price(), reverse=True)
        return sorted_list

    def delete_flower_to_shop(self, flower_from_flower_shop):
        """delete flower from shop"""
        if flower_from_flower_shop in self.list_of_flowers_in_shop:
            self.list_of_flowers_in_shop.remove(flower_from_flower_shop)

    def __str__(self):
        """
                        The func returns object in str format
                        :return:
                        """
        return "\n".join(str(flower_from_flower_shop)
                         for flower_from_flower_shop in self.list_of_flowers_in_shop)


class Bouquet:
    """
            class FlowerShop
            """

    def __init__(self):
        """
                             Class constructor
                             """
        self.flowers = []

    def add_flower_to_bouquet(self, flower_from_flower_shop, quantity):
        """add flower to bouquet"""
        for _ in range(quantity):
            self.flowers.append(flower_from_flower_shop)

    def get_total_price(self):
        """print total price flowers in bouquet"""
        return sum(flower.get_price() for flower in self.flowers)

    def __str__(self):
        """
                              The func returns object in str format
                              :return:
                              """
        return f"Bouquet - Total Price: {self.get_total_price()}"


if __name__ == "__main__":
    rose = Flower(20, "Medium", "Red", {"price": 200, "quantity": 10, "delivery_rate": 5})
    tulip = Flower(15, "Small", "Yellow", {"price": 400, "quantity": 20, "delivery_rate": 2})
    lily = Flower(25, "Large", "White", {"price": 500, "quantity": 30, "delivery_rate": 1})

    flower_shop = FlowerShop()
    flower_shop.add_flower_to_shop(rose)
    flower_shop.add_flower_to_shop(tulip)
    flower_shop.add_flower_to_shop(lily)

    print("Flower Shop Inventory:")
    print(flower_shop)

    bouquet = Bouquet()
    bouquet.add_flower_to_bouquet(rose, 3)
    bouquet.add_flower_to_bouquet(tulip, 5)

    print(f"Bouquet Details: {bouquet}")

    top_expensive_flowers = flower_shop.top_most_expensive_flowers()
    print("Top Most Expensive Flowers in the Shop:")
    for i, flower in enumerate(top_expensive_flowers, start=1):
        print(f"{i}. {flower}")
