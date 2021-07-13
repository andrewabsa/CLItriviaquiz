import time
def countdowntimer():
    cd = 60
    while cd:
     mins = cd // 60
     secs = cd % 60 
     timer = '{:02d}:{:02d}'.format(mins, secs)
     print(timer, end="\r")
     time.sleep(1)
     cd-=1
