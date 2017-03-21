import webbrowser as wb
import time


# def main():
#     while True:
#         print("DateTime " + time.strftime("%c"))
#         time.sleep(1) # delays for 1 seconds

# if __name__ == '__main__':
#     main()


time.sleep(10) # delays for 10 seconds
# time.sleep(60) # delays for 1 minute
# time.sleep(3600) # delays for 1 hour

new = 2

url = "https://www.youtube.com/watch?v=lRpxecLkUHQ"
wb.open(url,new=new)
