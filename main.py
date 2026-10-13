from focar import FoCar
import time

car = FoCar()

car.set_led("green")
car.forward(speed=60)
time.sleep(2.5)
car.stop()
time.sleep(1)

car.set_led("yellow")
car.turn_right(speed=70)
time.sleep(0.7)
car.forward(speed=50)
time.sleep(0.7)
car.stop()
time.sleep(0.5)

car.turn_left(speed=70)
time.sleep(1.0)
car.backward(speed=50)
time.sleep(1.0)
car.stop()
time.sleep(0.5)

car.turn_left(speed=70)
time.sleep(0.7)
car.stop()
time.sleep(1)

car.set_led("red")
car.forward(speed=60)
time.sleep(2.5)
car.stop()

car.set_led("off")
