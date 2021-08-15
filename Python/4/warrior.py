# NOTE: not all tests have been passed (163 passed; 3 failed)

RANKS = [
    "Pushover",
    "Novice",
    "Fighter",
    "Warrior",
    "Veteran",
    "Sage",
    "Elite",
    "Conqueror",
    "Champion",
    "Master",
    "Greatest"
]


class Warrior:
    def __init__(self):
        self._experience = 100
        self.achievements = []

    def training(self, lst):
        ach, exp, lvl = lst
        if lvl > self.level:
            return "Not strong enough"

        self._experience += exp
        self.achievements.append(ach)
        return ach

    def battle(self, level):
        diff = level - self.level
        if not 0 < level <= 100:
            return "Invalid level"

        if diff >= 5 and level // 10 > self.level // 10:
            return "You've been defeated"

        if diff > 0:
            self._experience += 20 * diff * diff
            return "An intense fight"

        if diff > -2:
            self._experience += 5 if diff == -1 else 10
            return "A good fight"

        return "Easy fight"

    @property
    def level(self):
        return self._experience // 100

    @property
    def experience(self):
        return min(10000, self._experience)

    @property
    def rank(self):
        return RANKS[self._experience // 1000]


bruce_lee = Warrior()
assert bruce_lee.level         == 1
assert bruce_lee.experience    == 100
assert bruce_lee.rank          == "Pushover"
assert bruce_lee.achievements  == []
assert bruce_lee.training(["Defeated Chuck Norris", 9000, 1]) == "Defeated Chuck Norris"
assert bruce_lee.experience    == 9100
assert bruce_lee.level         == 91
assert bruce_lee.rank          == "Master"
assert bruce_lee.battle(90)    == "A good fight"
assert bruce_lee.experience    == 9105
assert bruce_lee.achievements  == ["Defeated Chuck Norris"]
