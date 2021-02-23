import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.dic = kwargs        # Lines 6-11 take the dictionary that kwargs make and convert to two lists. The first one, contents, is able to change. The second one, balls, stays the same as it was once it was created.
        self.contents = []
        for k,v in self.dic.items():
            for x in range(v):
                self.contents.append(k)
        self.balls = copy.copy(self.contents)

    def draw(self, draw_times):
        if len(self.contents) < draw_times:  # Lines 15-30 are to make it where you can enter whatever amount of draw times and it'll still draw them.
            appe = draw_times - len(self.balls)
            if appe > len(self.balls):
                add = (appe // len(self.balls))
                for ad in range(add):
                    for db in self.balls:
                        self.contents.append(db)
                    self.balls += self.balls
                appe = draw_times - len(self.balls)
                ap = random.sample(self.balls, abs(appe))
                for a in ap:
                    self.contents.append(a)
            else:
                ap = random.sample(self.balls, abs(appe))
                for a in ap:
                    self.contents.append(a)
        v = random.sample(self.contents, draw_times) # Line 31-38 is giving you the balls to be drawn at random and removing them from the hat, or if hat is empty replacing them into the hat. 
        self.content_drew = v
        for d in self.content_drew:
            self.contents.remove(d)
        if len(self.contents) == 0:
            for db in self.balls:
                self.contents.append(db)
        return self.content_drew

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    favorable = 0
    failed = 0
    exper = num_experiments
    while num_experiments > 0:    # Lines 45-51 are breaking down the balls drawn from list format to the dictionary format.
        ha = hat.draw(num_balls_drawn)
        actual = {}
        for h in ha:
            if h in actual:
                actual[h] += 1
            else:
                actual[h] = 1
# Lines 53-64 are going through each item of the expected and comparing checking if the actual has the them in it. If it has all of the expected in it favorable variable above gets added by 1.
        z = 0  
        exp_balls = 0
        for act in expected_balls: 
            exp_balls += expected_balls[act]
            try:
                if expected_balls[act] <= actual[act]:
                    z += 1
            except:
                failed += 1

        if z >= len(expected_balls):
            favorable += 1
        num_experiments -= 1
# These last two lines give you the probability of the expected balls with number of balls drawn and number of experiments. 
    percent_per_num_experiments = favorable/exper
    return percent_per_num_experiments
