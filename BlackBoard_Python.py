
'''
In Blackboard Pattern, Several specialized sub-systems which is Knowledge Sources
Store the Knowledge data to build a possibly partial solution.
In this way, the sub-systems work together to provide solution

Randomly add numbers on contributions and progress. After that, check progress is smaller than 5
If the progress is smaller than 5, return contributions

We referenced https://en.wikipedia.org/wiki/Blackboard_system
'''

import abc
import random

class BlackBoardPattern(object):

    def __init__(self):
        self.experts = []
        self.common_state = {
            'contributions': [],
            'progress': 0   # Randomly add numbers on Progress
        }

    def add_expert(self, expert):
        self.experts.append(expert)

class Controller(object):

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def loop_run(self):
        while self.blackboard.common_state['progress'] < 5:
            for expert in self.blackboard.experts:
                if expert.is_eager_to_contribute:
                    expert.contribute()
        
        return self.blackboard.common_state['contributions']

class AbstractExpert(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, blackboard):
        self.blackboard = blackboard

    @abc.abstractproperty
    def is_eager_to_contribute(self):
        raise NotImplementedError('Error_ Implementation')

    @abc.abstractmethod
    def contribute(self):
        raise NotImplementedError('Error_ Implementation')


class Cat(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return True

    def contribute(self):
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(1, 10)


class Dog(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return random.randint(0, 1)

    def contribute(self):
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(10, 30)


if __name__ == '__main__':
    blackboard = BlackBoardPattern()

    blackboard.add_expert(Cat(blackboard))
    blackboard.add_expert(Dog(blackboard))


    c = Controller(blackboard)
    contributions = c.loop_run()

    from pprint import pprint
    pprint(blackboard.common_state['contributions'])
    
