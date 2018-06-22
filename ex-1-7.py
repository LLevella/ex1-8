class FarmAnimal:
    def __init__(self, weight, growth, n_legs, cover, color, move_mode, speech, gender=""):
        self.weight = weight
        self.growth = growth
        self.n_legs = n_legs
        self.cover = cover
        self.color = color
        self.move_mode = move_mode
        self.speech = speech
        self.gender = gender.lower()

    def get_color(self):
        return self.color

    def get_weight(self):
        return self.weight

    def get_growth(self):
        return self.growth

    def get_n_legs(self):
        return self.n_legs

    def get_cover(self):
        return self.cover

    def get_move_mode(self):
        return self.move_mode

    def how_i_speake(self):
        return self.speech


class FarmBird(FarmAnimal):
    has_wings = True  # подрезаны ли крылья
    can_fly = True
    can_swim = True

    def __init__(self, has_wings, can_fly, can_swim, weight, growth, n_legs, cover, color, move_mode, speech, gender):
        super().__init__(weight, growth, n_legs, cover, color, move_mode, speech, gender)
        self.has_wings = has_wings
        self.can_fly = can_fly
        self.can_swim = can_swim
        self.speech = speech

    def to_fly(self):
        if self.can_fly and self.has_wings:
            print("I'm flying")
        elif self.has_wings:
            print("I don't know how to fly")
        elif self.can_fly:
            print("My wings are hamstring")
        else:
            print("I can't")

    def to_swim(self):
        if self.can_swim:
            print("I'm swiming")
        else:
            print("I can't")

    def lay_an_egg(self):
        if self.gender == "ж":
            return 1
        return 0


class FarmMammal(FarmAnimal):
    has_horn = True
    give_milk = True
    need_to_graze = True

    def __init__(self, has_horn, give_milk,  need_to_graze, weight, growth, cover, color, speech, gender):
        super().__init__(weight, growth, 4, cover, color, ["ходит", "бегает"], speech, gender)
        self.has_horn = has_horn
        self.give_milk = give_milk
        self.need_to_graze = need_to_graze

    def butts(self):
        if self.has_horn:
            print("I cam butts")
        else:
            print("I haven't horns")

    def get_milk(self):
        if self.give_milk:
            return 1
        return 0

    def to_graze(self):
        if self.need_to_graze:
            print("I'm going to grase")
        else:
            print("I don't want to graze")


class Cows(FarmMammal):

    def __init__(self, weight, growth, color, gender):
        super().__init__(True, True, True, weight, growth, "шерсть", color, "Му", gender)

    def set_milk(self):
        if self.give_milk:
            self.v_milk = 16

    def get_milk(self):
        return self.v_milk

    def set_grass(self):
        if self.need_to_graze:
            self.v_grass = 45

    def get_grass(self):
        return self.v_grass


class Goat(FarmMammal):

    def __init__(self, weight, growth, color, gender, gives_wool):
        super().__init__(True, True, True, weight, growth, "шерсть", color, "Ме", gender)
        self.gives_wool = gives_wool

    def set_milk(self):
        if self.give_milk:
            self.v_milk = 6

    def get_milk(self):
        return self.v_milk

    def set_grass(self):
        if self.need_to_graze:
            self.v_grass = 7

    def get_grass(self):
        return self.v_grass

    def set_wool(self):
        if self.gives_wool:
            self.v_wool = 5

    def get_wool(self):
        return self.v_wool


class Sheep(FarmMammal):

    def __init__(self, has_horn, weight, growth, color, gender):
        super().__init__(has_horn, False,  True, weight, growth, "шерсть", color, "Бе", gender)

    def set_grass(self):
        if self.need_to_graze:
            self.v_grass = 10

    def get_grass(self):
        return self.v_grass

    def set_wool(self):
        if self.gives_wool:
            self.v_wool = 3

    def get_wool(self):
        return self.v_wool


class Pig(FarmMammal):

    def __init__(self, weight, growth, color, gender):
        super().__init__(False, False, False, weight, growth, "Шетина", color, "Хрю", gender)


class Duck(FarmBird):

    def __init__(self, has_wings, weight, growth, color, gender, gives_fluff):
        super().__init__(has_wings, True, True, weight, growth, 2, "Перья", color, ["Бегает", "Плавает", "Летает"],
                         "Кря", gender)
        self.gives_fluff = gives_fluff

    def set_egg(self):
        if self.gender == "ж":
            self.n_egg = 1
        else:
            self.n_egg = 0

    def get_egg(self):
        return self.n_egg

    def set_fluff(self):
        if self.gives_fluff:
            self.v_fluff = 0.12

    def get_fluff(self):
        return self.v_fluff


class Hen(FarmBird):

    def __init__(self, has_wings, weight, growth, color, gender):
        super().__init__(has_wings, False, True, weight, growth, 2, "Перья", color, ["Бегает"], "Ко", gender)

    def set_egg(self):
        if self.gender == "ж":
            self.n_egg = 1
        else:
            self.n_egg = 0

    def get_egg(self):
        return self.n_egg


class Goose(FarmBird):

    def __init__(self, has_wings, weight, growth, color, gender, gives_fluff):
        super().__init__(has_wings, True, True, weight, growth, 2, "Перья", color, ["Бегает", "Плавает", "Летает"],
                         "Га", gender)
        self.gives_fluff = gives_fluff

    def set_egg(self):
        if self.gender == "ж":
            self.n_egg = 1
        else:
            self.n_egg = 0

    def get_egg(self):
        return self.n_egg

    def set_fluff(self):
        if self.gives_fluff:
            self.v_fluff = 0.3

    def get_fluff(self):
        return self.v_fluff
