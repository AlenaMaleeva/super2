class Horse:
    def __init__(self):
        self.x_distance = 0 # пройденный путь.
        self.sound = 'Frrr' #звук, который издаёт лошадь
        super().__init__()
    def run(self, dx):
        self.x_distance += dx

class Eagle: # класс описывающий орла
    def __init__(self):
        self.y_distance = 0 # высота полёта
        self.sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл
    def fly(self, dy):
        self.y_distance += dy

class Pegasus (Horse, Eagle):# класс описывающий пегаса
    def move(self, dx, dy): #где dx и dy изменения дистанции
        self.run(dx)
        self.fly(dy)
    def get_pos(self):
       return (self.x_distance, self.y_distance)
    def voice (self):
        print(self.sound)
p1 = Pegasus()
print(p1.get_pos())

p1.move(10, 15)
print(p1.get_pos())

p1.move(-5, 20)
print(p1.get_pos())

p1.voice()






