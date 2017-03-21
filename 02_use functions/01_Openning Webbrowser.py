"""
For documentation of the webbrowser module,
see http://docs.python.org/library/webbrowser.html
"""
import webbrowser as wb
new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
url = "https://www.youtube.com/watch?v=lRpxecLkUHQ"
wb.open(url,new=new)

# open an HTML file on my own (Windows) computer
# url = "file://C:\Users\****\****\****.html"
# wb.open(url,new=new)
