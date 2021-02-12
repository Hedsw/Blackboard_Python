
'''
In Blackboard Pattern, Several specialized sub-systems which is Knowledge Sources
Store the Knowledge data to build a possibly partial solution.
In this way, the sub-systems wrok together to provide solution

The Solution is the sume of parts 

We referenced https://en.wikipedia.org/wiki/Blackboard_system
'''

import abc
import random

class BlackBoardPattern(object):

    def __init__(self):
        self.experts = []
        self.common_state = {
            'problems': 0,
            'contributions': [],
            'progress': 0   # percentage, if 100 -> task is finished
        }

    def add_expert(self, expert):
        self.experts.append(expert)

class Controller(object):

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def loop_run(self):
        while self.blackboard.common_state['progress'] < 100:
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


class PersonA(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return True

    def contribute(self):
        self.blackboard.common_state['problems'] += random.randint(1, 10)
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(1, 2)


class PersonB(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return random.randint(0, 1)

    def contribute(self):
        self.blackboard.common_state['problems'] += random.randint(10, 20)
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(10, 30)

class PersonC(AbstractExpert):
    @property
    def is_eager_to_contribute(self):
        return True if self.blackboard.common_state['problems'] > 100 else False

    def contribute(self):
        self.blackboard.common_state['problems'] += random.randint(1, 2)
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(10, 100)


if __name__ == '__main__':
    blackboard = BlackBoardPattern()

    blackboard.add_expert(PersonB(blackboard))
    blackboard.add_expert(PersonA(blackboard))


    c = Controller(blackboard)
    contributions = c.loop_run()

    from pprint import pprint
    pprint(contributions)
    
