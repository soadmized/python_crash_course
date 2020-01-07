from car import Car, ElectricCar
from user import User, Admin
from resto import Restaurant, IceCreamStand
import random

class Dog():

    """
    This class describes dog
    """

    def __init__(self, name: str, age):
        self.name = name
        self.age= age


    def sit(self):
        """
        This method makes dog sit
        :return: 0
        """
        print(self.name.title() + " is now sitting")
        return 0

    def roll_over(self):
        """
        this method makes dog roll over
        :return:
        """
        print(self.name.title() + " is now rolling over!")


if __name__ == "__main__":
    my_dog = Dog('joker', 1)
    print("My dog's name is {0} and it's {1} years old".format(my_dog.name.title(), my_dog.age))
    my_dog.sit()
    my_dog.roll_over()
    your_dog = Dog('jacklin', 1)
    print("Your dog's name is {0} and it's {1} years old".format(your_dog.name.title(), your_dog.age))
    your_dog.sit()
    your_dog.roll_over()

    print('-----------------------')
    mcdonalds = Restaurant("McDonalds", "fast food")
    mcdonalds.describe_resto()
    mcdonalds.open_resto()
    kfc = Restaurant("KFC", "fast food")
    kfc.describe_resto()
    bellagio = Restaurant("bellagio", "italian")
    bellagio.describe_resto()
    print(bellagio.number_served)
    bellagio.set_number_served(4)
    print(bellagio.number_served)
    bellagio.increment_number_served(6)
    print(bellagio.number_served)

    print("-------------------------")
    user_1 = User("Alex", "Z.", "soadmized")
    user_1.describe_user()
    user_1.greet_user()
    print(user_1.login_attempts)
    user_1.increment_login_attempts()
    user_1.increment_login_attempts()
    print(user_1.login_attempts)
    user_1.reset_login_attempts()
    print(user_1.login_attempts)

    print("------------------------")
    flavors = ['cherry', 'strawberry', 'orange', 'kiwi', 'coconut', 'blueberry']
    icecream = IceCreamStand("Gellatio", "ice cream", flavors)
    icecream.describe_icecream()

    print("------------------------")
    privs = ['add user', 'delete user', 'change password', 'restart server', 'add/delete dirs']
    admin = Admin('Alex', 'Z', 777, 'soadmized', privs)
    admin.privs.show_privilegies()
    admin.describe_user()

    print("------------------------")
    my_car = ElectricCar('Toyota', 'prius', 2008)
    my_car.battery.describe_battery()
    my_car.battery.get_range()
    my_car.battery.upgrade_battery()
    my_car.battery.describe_battery()
    my_car.battery.get_range()

    print("------------------------")



