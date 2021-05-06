class Car:
    def __init__(self, value1, value2):
        self.color = value1
        self.speed = self.speed = value2

    def upSpeed(self, value):
        self.speed += value
        self.speed = self.speedCheck(self.speed)

    def downSpeed(self, value):
        self.speed -= value
        self.speed = self.speedCheck(self.speed)

    def speedCheck(self, speed):
        if speed < 0:
            return 0
        elif speed > 300:
            return 300
        else:
            return speed


class Sedan(Car):
    seat = 5

    def getSeat(self):
        return self.seat


class Truck(Car):
    seat = 2

    def getSeat(self):
        return self.seat


myCar1 = Sedan("RED", 20)

myCar2 = Truck("BLUE", 90)

myCar3 = Car("YELLOW", 0)

myCar1.upSpeed(30)
print(
    "자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다. 좌석수 : %d"
    % (myCar1.color, myCar1.speed, myCar1.seat)
)

myCar2.downSpeed(60)
print(
    "자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다. 좌석수 : %d"
    % (myCar2.color, myCar2.speed, myCar2.seat)
)

myCar3.downSpeed(10)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar3.color, myCar3.speed))
