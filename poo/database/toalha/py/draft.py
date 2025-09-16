class Towel:
    def __init__(self):
        self.color = 'red'
        self.size  = 'P'
        self.wetness = 0
    def __str__ (self):
        return f'color: {self.color}, size: {self.size}'

toalha = Towel()
print(Towel())
print(toalha.color)
print(toalha.size)
print(toalha.wetness)