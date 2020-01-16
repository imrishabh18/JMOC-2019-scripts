import time

def convertTime(sec):
    mins = sec/60
    secs = sec%60
    hours = mins/60
    mins = mins%60

    print("Time Lapsed : {0}:{1}:{2}".format(int(hours),int(mins),int(secs)))


input("Press Enter to start the StopWatch : ")
startTime = time.time()
input("Press Enter to stop : ")
endTime = time.time()
timeConsumed = endTime-startTime

convertTime(timeConsumed)
