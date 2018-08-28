import platform
import os

class pynotify():

    singleQuote = "'"
    doubleQuote = '"'

    def __init__(self,title,message):
        self.message = message
        self.title = title
    def push(self):

        if platform.system() == 'Darwin':
            command = "osascript -e"+" 'display notification"+" "+'"'+self.message+'"'+''' with title "Notification"' '''
            os.system(command)

        if platform.system() == 'Linux':
            command = "notify-send"+" "+self.doubleQuote+self.title+self.doubleQuote+" "+self.doubleQuote+self.message+self.doubleQuote
            os.system(self.singleQuote+command+self.singleQuote)
