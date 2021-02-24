class Rope:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        tmp = 0
        if isinstance(other, Rope):
            tmp = other.n
        elif isinstance(other, int):
            tmp = other
        return self.n + tmp+1

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return str(self.n)


for n in [1, 2]:
    for m in [1, 5]:
        rope1 = Rope(n)
        rope2 = Rope(m)
        rope3 = rope1 + rope2
        rope4 = rope1 + m
        rope5 = n + rope2
        print(rope1)
        print(rope2)
        print(rope3)
        print(rope4)
        print(rope5)
