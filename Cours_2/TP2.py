import Canard

# ... Les autres classes FlyBehavior, QuackBehavior, Duck et ses sous-classes ...

class Goose:
    def honk(self):
        print("Honk honk")

class GooseAdapter(Canard.Duck):
    def __init__(self, goose: Goose):
        super().__init__(name='Goose', flybehavior=Canard.Fly2Wings(), quackbehavior=None)
        self.goose = goose
    
    def quack(self):
        self.goose.honk()

class DuckSimulator:
    def simulate(self, duck: Canard.Duck):
        for _ in range(2):
            duck.fly()
        duck.quack()
        for _ in range(3):
            duck.fly()

class QuackCounter(Canard.QuackBehavior):
    _quacks_count = 0

    def __init__(self, behavior: Canard.QuackBehavior):
        self.decorated_quack = behavior
    
    def quack(self):
        self.decorated_quack.quack()
        QuackCounter._quacks_count += 1
    
    @staticmethod
    def get_quacks():
        return QuackCounter._quacks_count

class Quackologist:
    def update(self, duck: Canard.Duck):
        print(f"Quackologist: Duck {duck.name} just quacked.")

# Observer pattern classes
# ...

if __name__ == '__main__':
    simulator = DuckSimulator()
    quackologist = Quackologist()

    # Intégration de Goose avec GooseAdapter
    goose = Goose()
    goose_adapter = GooseAdapter(goose)
    goose_adapter.flybehavior = QuackCounter(goose_adapter.flybehavior)
    # Attaching observer
    # ...

    simulator.simulate(goose_adapter)
    
    print(f"Total quacks: {QuackCounter.get_quacks()}")
    # Total quacks would include both the Duck and the GooseAdapter quacks.


