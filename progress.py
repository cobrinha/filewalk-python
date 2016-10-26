import wx
import threading

exitFlag = 0

class thread_progress (threading.Thread):
    def __init__(self, threadID, name, counter, msg):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.msg = msg
        self.exitFlag = 0
        
    def run(self):
        print "Starting " + self.name
        max = 99
        dlg = wx.ProgressDialog("FileWalker 0.1v",self.msg, style = wx.PD_CAN_ABORT| wx.PD_APP_MODAL| wx.PD_ELAPSED_TIME| wx.PD_REMAINING_TIME)
        keepGoing = True
        count = 0
        while self.exitFlag < 1:
            count += 0.5
            wx.MilliSleep(20)
            if count == max:
                count = 0
                
            dlg.Update(count)                
                             
        dlg.Destroy()
        print "Exiting " + self.name


class thread_progress2 (threading.Thread):
    def __init__(self, threadID, name, counter, msg):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.msg = msg
        self.exitFlag = 0
        
    def run(self):
        print "Starting " + self.name
        max = 99
        dlg = wx.ProgressDialog("pySpaceLiberator 0.1v",self.msg, style = wx.PD_CAN_ABORT| wx.PD_APP_MODAL| wx.PD_ELAPSED_TIME| wx.PD_REMAINING_TIME)
        keepGoing = True
        count = 0
        while self.exitFlag < 1:
            count += 0.5
            wx.MilliSleep(20)
            if count == max:
                count = 0
                
            dlg.Update(count)                
                             
        dlg.Destroy()
        print "Exiting " + self.name        
