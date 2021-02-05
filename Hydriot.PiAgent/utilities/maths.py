import random

class Math(object):
    def random_number(self, lower_bound, upper_bound):
        random_value = random.randint(lower_bound, upper_bound)

        return random_value