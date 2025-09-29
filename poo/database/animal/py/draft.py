class Animal:
    def __init__ (self, specie: str, age: int, sound: str):
        self.specie: str = specie
        self.age: int = 0
        self.sound: str = sound

    def __str__ (self) -> str:
        return f'{self.specie}:{self.age}:{self.sound}'
    
    def show(self) -> None:
        print(self)

    def ageby(self,increment: int) -> None:
        self.age += increment
        if self.age >= 4:
            print(f"warning: {self.specie} morreu")
            self.age = 4
            
    def noise(self) -> str:
        if self.age == 0:
            return '---'
        if self.age == 4:
            return 'RIP'
        else:
            return self.sound

def main():
    animal = Animal(' ', ' ', ' ')
    
    while True:
        line: str = input()
        args: list[str] = line.split(' ')
        
        if args[0] == 'end':
            print('$end')
            break
        elif args[0] == 'init':
            specie = args[1]
            age = args[2]
            sound = args[2]
            animal = Animal(specie, age, sound)
            print(f'$init {specie} {sound}')
        elif args[0] == 'show':
            print('$show')
            print(animal)
        elif args[0] == 'grow':
            print(f'$' + line)
            increment:int = int(args[1])
            animal.ageby(increment)
        elif args[0] == 'noise':
            print('$noise')
            print(animal.noise())
            
main()