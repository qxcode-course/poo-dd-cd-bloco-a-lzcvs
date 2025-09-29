class Carro:
    def __init__(self, psg: int , gas: int, km: int):
        self.psg = 0
        self.gas = 0
        self.km = 0
    def __str__(self) -> str:
        return(f'pass: {self.psg}, gas: {self.gas}, km: {self.km}')
    def enter(self) -> None:
        limite_de_pessoas = 2
        if self.psg == limite_de_pessoas:
            print('fail: limite de pessoas atingido')
        else:
            self.psg += 1
    def leave(self) -> None:
        if self.psg == 0:
            print('fail: nao ha ninguem no carro')
        else:
            self.psg -= 1
    def addfuel(self, increment:int) -> None:
        gas_max = 100
        self.gas += increment
        if self.gas > 100:
            self.gas = 100
    def drive(self, distance: int) -> None:
        
        if self.psg == 0:
            print('fail: nao ha ninguem no carro')
        elif self.gas == 0:
            print('fail: tanque vazio')
        elif distance > self.gas:
            print(f'fail: tanque vazio apos andar {self.gas} km')
            self.km += self.gas
            self.gas = 0
        else:
            self.km = distance
            self.gas = self.gas - distance
            
def main():
    carro = Carro(' ', ' ', ' ')

    while True:
        line: str = input()
        args: list[str] = line.split(' ')
        print(f'$' + line)
        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(carro)
        elif args[0] == 'enter':
            carro.enter()
        elif args[0] == 'leave':
            carro.leave()
        elif args[0] == 'fuel':
            increment:int = int(args[1])
            carro.addfuel(increment)
        elif args[0] == 'drive':
            distance: int = int(args[1])
            carro.drive(distance)
main()