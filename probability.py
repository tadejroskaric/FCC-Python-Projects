import random

class Hat:
    def __init__(self, **kwargs):
        self.values = kwargs
        self.drawn = []
        self.contents = []

        # Making an array of keys (for example [red, red, yellow, yellow, yellow])
        for key, value in self.values.items():
            i = 0
            while value > i:
                i += 1
                self.contents.append(key)
        self.contents_original = self.contents.copy()

    def draw(self, balls):
        # Number of balls exceeding available quantity
        if balls > len(self.contents):
            return self.contents

        # Drawing an array of balls from hat
        i = 0
        self.drawn = []
        self.contents = self.contents_original.copy()
        while balls > i:
            index = random.randint(0, len(self.contents) - 1)
            self.drawn.append(self.contents[index])
            self.contents.pop(index)
            i += 1
        return self.drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # M is count of experiments with expected balls
    M = 0
    expected_balls_array = []

    # Making another array of keys
    for key, value in expected_balls.items():
        i = 0
        while value > i:
            i += 1
            expected_balls_array.append(key)

    # Conducting experiment
    i = 0
    while num_experiments > i:
        check = []
        for key, value in expected_balls.items():
            # Checking if drawn array is the same as expected array
            if hat.draw(num_balls_drawn).count(key) >= expected_balls_array.count(key):
                check.append(0)
            else:
                check.append(1)

        if sum(check) == 0:
            M += 1
        i += 1
    return M / num_experiments
