import random


class Hat:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        counter = 0
        for v in [*self.kwargs.values()]:
            for k in range(int(v)):
                vals = [*self.kwargs.keys()]
                self.contents.append(vals[counter])
            counter += 1
        self.fixed_content = self.contents[:]

    def draw(self, num_balls_drawn):
        balls_drawn = []
        if num_balls_drawn > len(self.contents):
            return self.contents
        else:
            for i in range(num_balls_drawn):
                ball = random.randint(0, len(self.contents)-1)
                balls_drawn.append(self.contents.pop(ball))
            return balls_drawn

    def refill(self):
        self.contents = self.fixed_content[:]

def experiment(hat, expected_balls, num_balls_drawn=5, num_experiments=1000):
    M = 0
    c = [*[[i]*expected_balls[i] for i in [*expected_balls]]]
    ex_b = []
    experiment_counter = 0
    for i in c:
        ex_b += i
    if len(ex_b) > num_balls_drawn:
        return 0.0
    for n in range(num_experiments):
        balls = hat.draw(num_balls_drawn)
        check_balls = []
        for k,v in expected_balls.items():
            if balls.count(k) >= v:
                check_balls.append(True)
            else:
                check_balls.append(False)
        if all(check_balls):
            M += 1
        experiment_counter += 1
        hat.refill()
    probability = M/num_experiments
    print(experiment_counter)
    return probability



a = Hat(orange=5, blue=4)
print(experiment(a, expected_balls={'blue':3, 'orange':1}, num_balls_drawn=4, num_experiments=3000))
