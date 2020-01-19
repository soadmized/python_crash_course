class Restaurant():

    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_resto(self):
        print("This is {0} restaurant. It has a {1} cuisine.".format(self.restaurant_name.title(), self.cuisine_type))
        return 0


    def open_resto(self):
        print("{} is open!!".format(self.restaurant_name.title()))
        return 0


    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("Mistake!")


    def increment_number_served(self, number):
        if number >= self.number_served:
            self.number_served += number
        else:
            print("Mistake!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)

    def describe_icecream(self):
        print("There are {} flavors!".format(self.flavors))
