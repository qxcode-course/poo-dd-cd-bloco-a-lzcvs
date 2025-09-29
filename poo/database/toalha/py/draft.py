class Towel:
    def __init__(self, color: str, size: str): #constructor
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def getMaxWetness(self) -> int :
        if self.size == 'P':
            return 10
        if self.size == 'M':
            return 20
        if self.size == 'G':
            return 30
        return 0
    
    def wringOut(self) -> None:
        self.wetness = 0
    
    def dry(self, amount: int) -> None: #self objeto
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print('toalha encharcada')
            self.wetness = self.getMaxWetness()
    
    def isDry(self) -> bool:
        return self.wetness == 0
    
    def show(self) -> None:
        print(self)
    
    def __str__(self) -> str:
        return f"cor: {self.color} tamanho: {self.size} umidade: {self.wetness}"
def main():
    toalha = Towel(' ', ' ')
    while True:
        line: str = input()
        args: list[str] = line.split(' ') # [0, 1, 2]
        if args[0] == 'end':
            break
        elif args[0] == 'new':
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == 'show':
            print(toalha)
        elif args[0] == 'dry':
            amount: int = int(args[1])
            toalha.dry(amount)
        else:
            print('comando invalido')
main()