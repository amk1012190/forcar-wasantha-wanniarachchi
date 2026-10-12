from focar import FoCar
import time

car = FoCar()

# --- TASK 1: Forward 1 meter ---
print("Task 1: Going forward 1m")
car.set_led("green")
car.forward(speed=60)
time.sleep(2.5)  # Lab එකේදී 1m යන්න ඕන වෙලාව බලලා මේක වෙනස් කරගන්න
car.stop()
time.sleep(1)

# --- TASK 2: Three-point turn ---
print("Task 2: Three-point turn")
car.set_led("yellow")

# 1st: Turn right and forward
car.turn_right(speed=70)
time.sleep(0.7)
car.forward(speed=50)
time.sleep(0.7)
car.stop()
time.sleep(0.5)

# 2nd: Turn left and backward
car.turn_left(speed=70)
time.sleep(1.0)
car.backward(speed=50)
time.sleep(1.0)
car.stop()
time.sleep(0.5)

# 3rd: Turn left to face back
car.turn_left(speed=70)
time.sleep(0.7)
car.stop()
time.sleep(1)

# --- TASK 3: Return to start ---
print("Task 3: Returning")
car.set_led("red")
car.forward(speed=60)
time.sleep(2.5)
car.stop()

car.set_led("off")
print("Completed: 1m forward, 3-point turn, return")
