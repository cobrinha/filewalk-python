import wx
import gui

class MainApp(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.panelMain = Panel_Main(self)
        self.panelScan = Panel_Scan(self)
        self.panelLargest = Panel_Largest(self)
        self.panelToolbar = PanelToolbar(self)  
        self.panelScan.Hide()
        self.panelLargest.Hide()
        self.panelMain.Show()
        
class Panel_Main(gui.panel_main):
    def __init__(self, parent):
        gui.panel_main.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Main options")
            #self.Hide()
            #self.parent.panelScan.Show()

class Panel_Scan(gui.panel_scan):
    def __init__(self, parent):
        gui.panel_scan.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Scan files")
            #self.parent.panelMain.Show()
            #self.Hide()

class Panel_Largest(gui.panel_largest):
    def __init__(self, parent):
        gui.panel_largest.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Largest files")
            #self.parent.panelLargest.Show()
            #self.Hide()

class PanelToolbar(gui.panel_toolbar):
    def __init__(self, parent):
        gui.panel_toolbar.__init__(self, parent)
        self.parent = parent

def main():
    app = wx.App()
    window = MainApp(None)
    window.SetTitle("Py File Search")    
    window.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
