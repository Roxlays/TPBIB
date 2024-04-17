from abc import ABC, abstractmethod

class Duck(ABC):

    def __init__(self, name = 'undefined'):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def quack(self):
        pass

class RedKneck(Duck):

    def __init__(self, name):
        if name[0] == 'j':
            super().__init__(name)
        else:
            raise ValueError('Should start with j')

    def fly(self):
        print(f'{self.name} can fly')

    def quack(self):
        print('Red quack')

class GreenKneck(Duck):

    def __init__(self):
        super().__init__()
    
    def fly(self):
        print(f'{self.name} believe...')

    def quack(self):
        print('Quack Quack')

if __name__ == '__main__':
    greenDuck = GreenKneck()
    greenDuck.fly()
    greenDuck.quack()
    redDuck = RedKneck('jaffiduck')
    redDuck.fly()
    redDuck.quack()