class Calculadora:
    def __init__(self, battery_max:int):
        self.display = 0
        self.battery:float = 0
        self.battery_max = battery_max

    def show(self):
        print(self)

    def charge(self, value: int) -> None:
        self.battery += value
        if self.battery > self.battery_max:
            self.battery = self.battery_max
    def sum(self, a: int, b: int) -> int:
        if self.battery == 0:
            print('fail: bateria insuficiente')
            return 
        self.display = (a + b)
        self.battery -= 1
    def div(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            print('fail: divisao por zero')
            self.battery -= 1
            return
        if self.battery == 0:
            print('fail: bateria insuficiente')
            return
        self.display = a / b
        self.battery -= 1
    def __str__(self) -> str:
        display_value = float(self.display)
        return (f'display = {display_value:.2f}, battery = {self.battery}')
def main():
    while True:
        line: str = input()
        args = line.split(' ')
        print(f'$' + line)
        if args[0] == 'end':
            break
        elif args[0] == 'init':
            battery = int(args[1])
            ca = Calculadora(battery)
        elif args[0] == 'show':
            print(ca)
        elif args[0] == 'charge':
            value:int = int(args[1])
            ca.charge(value)
        elif args[0] == 'sum':
            a = int(args[1])
            b = int(args[2])
            ca.sum(a, b)
        elif args[0] == 'div':
            a = int(args[1])
            b = int(args[2])
            ca.div(a, b)
main()