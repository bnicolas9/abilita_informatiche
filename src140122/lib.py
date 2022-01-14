class Shape:
    def __init__(self, nome, base):
        self.name = nome
        self.base = base

    def area(self):
        from numpy import dot
        parallelogrammi = ["rombo", "quadrato", "rettangolo", "parallelogramma"]
        if self.name == "cerchio":
            from math import pi
            return self.base ** 2 * pi
        elif self.name in parallelogrammi:
            return dot(self.base[0], self.base[1])
        elif self.name == "triangolo":
            return dot(self.base[0], self.base[1]) * 0.5
        else:
            print("Non disponibile")

def div(a, b):
    return a / b