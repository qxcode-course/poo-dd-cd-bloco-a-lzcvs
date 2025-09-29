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
        if self.wetness >= self.getMaxWetness():
            print('toalha encharcada')
            self.wetness = self.getMaxWetness()
    def isDry(self) -> bool:
        if self.wetness == 0:
            print('sim')
        else:
            print('nao')
    def show(self) -> None:
        print(self)
    
    def __str__(self) -> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"
def main():
    toalha = Towel(' ', ' ')
    while True:
        line: str = input()
        args: list[str] = line.split(' ') # [0, 1, 2]
        print(f'$' + line)
        if args[0] == 'end':
            break
        elif args[0] == 'criar':
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == 'mostrar':
            print(toalha)
        elif args[0] == 'enxugar':
            amount: int = int(args[1])
            toalha.dry(amount)
        elif args[0] == 'seca':
            toalha.isDry()
        elif args[0] == 'torcer':
            toalha.wringOut()
        else:
            print('comando invalido')
main()