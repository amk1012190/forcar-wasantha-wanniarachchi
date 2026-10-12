# focar.py - FoCar control library
import time

class FoCar:
    def forward(self, speed=50):
        print(f"Moving forward at {speed}%")
        
    def backward(self, speed=50):
        print(f"Moving backward at {speed}%")
        
    def turn_right(self, speed=50):
        print(f"Turning right at {speed}%")
        
    def turn_left(self, speed=50):
        print(f"Turning left at {speed}%")
        
    def stop(self):
        print("Stopping")
        
    def set_led(self, color):
        print(f"LED set to {color}")
