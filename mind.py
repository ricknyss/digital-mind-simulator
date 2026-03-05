class DigitalMind:
    def __init__(self):
        self.energy = 70
        self.mood = 60
        self.stress = 30
        self.hunger = 40

    def status(self):
        print("\n--- Mind Status ---")
        print("Energy:", self.energy)
        print("Mood:", self.mood)
        print("Stress:", self.stress)
        print("Hunger:", self.hunger)

    def work(self):
        print("\nYou decided to work.")
        self.energy -= 20
        self.stress += 15
        self.mood -= 5

    def eat(self):
        print("\nYou decided to eat.")
        self.hunger -= 20
        self.energy += 10
        self.mood += 5

    def sleep(self):
        print("\nYou decided to sleep.")
        self.energy += 25
        self.stress -= 10

    def relax(self):
        print("\nYou decided to relax.")
        self.stress -= 15
        self.mood += 10