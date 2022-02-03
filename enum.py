from enum import Enum
import random

class Light(Enum):
    RED = 1
    YELLOW = 2
    GREEN=3

print("let's play red light green light")


my_list=[]
for i in range (8):
    my_list.append(random.randint(1,3))
print(my_list)
for item in my_list:
    if item ==1:
        current_light = Light.RED
        print(current_light, "stop")
    elif item ==2:
        current_light = Light.YELLOW
        print(current_light, "be aware")
    elif item ==3:
        current_light = Light.GREEN
        print(current_light, "go")

