import time


class TrafficLight:
    __color = ""

    def running(self):
        __color = "Red"
        print("Red")
        time.sleep(7)
        __color = "Yellow"
        print("Yellow")
        time.sleep(2)
        __color = "Green"
        print("Green")
        time.sleep(7)
        __color = "Yellow"
        print("Yellow")
        time.sleep(2)


a = TrafficLight()
a.running()
