import time
import threading
from ultralytics.yolo.v8.detect.predict import result_show

defaultGreen = {0: 20, 1: 20, 2: 20, 3: 20}
defaultRed = 150
defaultYellow = 5
signals = []
noOfSignals = 4
currentGreen = 0   # Indicates which signal is green currently
nextGreen = (currentGreen+1) % noOfSignals
currentYellow = 0   # Indicates whether yellow signal is on or off
speeds = 2  # 2km/h average speeds of vehicles taken from reference paper "tomtom"

class TrafficSignal:
    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green
        self.signalText = ""

def initialize():
    ts1 = TrafficSignal(0, defaultYellow, defaultGreen[0])
    signals.append(ts1)
    ts2 = TrafficSignal(ts1.yellow+ts1.green, defaultYellow, defaultGreen[1])
    signals.append(ts2)
    ts3 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[2])
    signals.append(ts3)
    ts4 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[3])
    signals.append(ts4)
    repeat()


def repeat():
    global currentGreen, currentYellow, nextGreen
    while (signals[currentGreen].green > 0):
        updateValues()
        time.sleep(1)
    currentYellow = 1

    while (signals[currentGreen].yellow > 0):
        updateValues()
        time.sleep(1)
    currentYellow = 0

    signals[currentGreen].green = defaultGreen[currentGreen]
    signals[currentGreen].yellow = defaultYellow
    signals[currentGreen].red = defaultRed

    currentGreen = nextGreen
    nextGreen = (currentGreen + 1) % noOfSignals
    signals[currentGreen].green = result_show
    signals[nextGreen].red = signals[currentGreen].yellow + signals[currentGreen].green
    repeat()

def updateValues():
    for i in range(0, noOfSignals):
        if(i==currentGreen):
            if(currentYellow==0):
                signals[i].green-=1
            else:
                signals[i].yellow-=1
        else:
            signals[i].red-=1


class Main:
    thread1 = threading.Thread(name="initialization", target=initialize, args=())
    thread1.daemon = True
    thread1.start()

    black = (0, 0, 0)
    white = (255, 255, 255)
    screenWidth = 1400
    screenHeight = 800
    screenSize = (screenWidth, screenHeight)

    while True:
       for i in range(0, noOfSignals):
            if (i == currentGreen):
                if (currentYellow == 1):
                    signals[i].signalText = signals[i].yellow
                else:
                    signals[i].signalText = signals[i].green
            else:
                if (signals[i].red <= 10):
                    signals[i].signalText = signals[i].red
                else:
                    signals[i].signalText = "---"

Main()