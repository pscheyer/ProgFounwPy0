import time
import webbrowser

totalbreaks = 3
breakcount = 0

print("This program started on "+time.ctime())
while(breakcount < totalbreaks):
    time.sleep(10.0)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print breakcount
    breakcount = breakcount + 1
