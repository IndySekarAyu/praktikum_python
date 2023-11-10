class Human:
    def __init__(self, name, position, speed):
        self._name = name
        self._position = position
       
    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def movement(self, direction):
        if direction == "L":
            self._position -= self._speed
        elif direction == "R":
            self._position += self._speed

    def attack(self, target):
        target.set_health(target.get_health() - self._power)

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def get_armor(self):
        return self._armor

    def set_armor(self, armor):
        self._armor = armor

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed
        
class Hero(Human):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)


class Warrior(Hero):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self.set_armor(45)
        self._power = 32
        target.set_health(target.get_health() - self._power)


class Assassin(Hero):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self.set_speed(7)
        self._power = 42
        target.set_health(target.get_health() - self._power)


class Support(Hero):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._health = 500
        self._armor = 8
        self._speed = 4
                            
    def special(self, target):
        self.set_speed(6)
        target.set_health(target.get_health() + 150)

warrior = Warrior("Warrior", 0, 3)
assassin = Assassin("Assassin", 0, 3)
support = Support("Support", 0, 3)

warrior.special(warrior)
assassin.special(assassin)
support.special(support)

print(f"{warrior.get_name()}'s health after special: {warrior.get_health()}")
print(f"{assassin.get_name()}'s health after special: {assassin.get_health()}")
print(f"{support.get_name()}'s health after special: {support.get_health()}")

