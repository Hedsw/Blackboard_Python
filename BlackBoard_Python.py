
'''
BlackBoard <--> Controller <---> Knowledge Source (Cat, Dog)
Randomly add numbers on contributions and feeds. After that, check feeds is smaller than 5
If the feeds is smaller than 5, return contributions
We referenced https://en.wikipedia.org/wiki/Blackboard_system
'''

import abc
import random

class BlackBoardPattern(object):

    def __init__(self):
        self.animals = []
        self.common_state = {
            'contributions': [],
            'feeds': 0   # Randomly add numbers on feeds
        }

    def add_expert(self, expert):
        self.animals.append(expert)

class Controller(object):

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def loop_run(self):
        while self.blackboard.common_state['feeds'] < 100:
            for expert in self.blackboard.animals:
                if expert.randomly_contri:
                    expert.contribute()
        
        return self.blackboard.common_state['contributions']

class Erroerchecker(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, blackboard):
        self.blackboard = blackboard

    @abc.abstractproperty
    def randomly_contri(self):
        raise ErroerShooting('Error_ Implementation')

    @abc.abstractmethod
    def contribute(self):
        raise ErroerShooting('Error_ Implementation')


class Cat(Erroerchecker):
    @property
    def randomly_contri(self):
        return random.randint(0, 1)

    def contribute(self):
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['feeds'] += random.randint(1, 11)


class Dog(Erroerchecker):
    @property
    def randomly_contri(self):
        return random.randint(0, 1)

    def contribute(self):
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['feeds'] += random.randint(1, 11)


if __name__ == '__main__':
    blackboard = BlackBoardPattern()

    blackboard.add_expert(Cat(blackboard))
    blackboard.add_expert(Dog(blackboard))

    c = Controller(blackboard)
    returnvalue = c.loop_run()

    from pprint import pprint
    pprint(blackboard.common_state['contributions'])
    

