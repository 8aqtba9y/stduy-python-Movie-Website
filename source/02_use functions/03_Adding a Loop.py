import webbrowser as wb
import time

url = "https://www.youtube.com/watch?v=lRpxecLkUHQ"

break_count = 0
total_count = 3

print "This Program started on " +time.ctime() # Current time
# def loop():
while break_count < total_count:
    time.sleep(10) # delays for 10 seconds
    wb.open(url)
    break_count = break_count + 1

# if __name__ == '__main__':
#     loop()
# UnboundLocalError: local variable 'break_count' referenced before assignment
