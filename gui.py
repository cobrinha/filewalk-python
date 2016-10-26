import wx, time
from datetime import datetime
from progress import thread_progress
import tree

class MainFrame ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.SetSizer( bSizer1 )
        self.Layout()
        #self.panelMain = panel_main(self)
        #self.panelScan = panel_scan(self)
        # self.panelTwo.Hide()
        self.Centre( wx.BOTH )
        self.toolbar = self.CreateToolBar(style=(wx.TB_HORZ_LAYOUT | wx.TB_TEXT))
        self.toolbar.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        #self.toolbar.SetBackgroundColour((100, 100, 100))
        image_file = 'images/bg_toolbar.png'
        #bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #self.bitmap1 = wx.StaticBitmap(parent.toolbar, -1, bmp1, (0, 0))
        tool_main_id = wx.NewId()
        tool_scan_id = wx.NewId()
        tool_maiores_id = wx.NewId()
        self.toolbar.SetToolBitmapSize((64,64))        
        tool_main = self.toolbar.AddLabelTool(tool_main_id, '', wx.Bitmap('images/bt_main.png'))
        tool_scan = self.toolbar.AddLabelTool(tool_scan_id, '', wx.Bitmap('images/bt_scan.png'))
        tool_maiores = self.toolbar.AddLabelTool(tool_maiores_id, '', wx.Bitmap('images/bt_maiores.png'))
        self.toolbar.AddSeparator()
        self.toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.showMain, tool_main)
        self.Bind(wx.EVT_TOOL, self.showScan, tool_scan)
        self.Bind(wx.EVT_TOOL, self.showMaiores, tool_maiores)

    def showMain(self, e):
        self.SetTitle("Home")
        self.panelScan.Hide()        
        self.panelLargest.Hide()        
        self.panelMain.Show()

    def showScan(self, e):
        self.SetTitle("Scan files")

        #choose root dir
        dlg = wx.DirDialog(self, "Choose a directory:")
        rootdir = 0
        if dlg.ShowModal() == wx.ID_OK:
            rootdir = dlg.GetPath()
            dlg.Destroy()

        # initialize the tree
        t = datetime.now()
        datet = t.strftime("%d/%m/%Y %H:%M:%S")
        print 'Datahora: '+datet

        start = time.time()
        th_progress = thread_progress(1, "ThreadProgress", 1, "Aguarde, esse processo pode levar algum tempo!")
        th_progress.start()
        panel_treectrl.file_tree.buildTree(panel_treectrl, rootdir+"\\")
        th_progress.exitFlag = 1
        end = time.time()
        print 'PRONTO! \n'
        print str(end - start) + ' s.\n'
        
        self.panelMain.Hide()
        self.panelLargest.Hide()        
        self.panelScan.Show()
        
        
    def showMaiores(self, e):
        self.SetTitle("Largest files")
        self.panelMain.Hide()
        self.panelScan.Hide()        
        self.panelLargest.Show()
        
    def __del__( self ):
        pass

class panel_main ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        '''self.m_button2 = wx.Button( self, wx.ID_ANY, u"panel 1 button", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )'''
        self.SetSizer( bSizer5 )
        #self.SetBackgroundColour((, 11, 11))
        self.Layout()
        # Connect Events
        #self.m_button2.Bind( wx.EVT_BUTTON, self.changeIntroPanel )
    def __del__( self ):
        pass
    # Virtual event handlers, overide them in your derived class
    def changeIntroPanel( self, event ):
        event.Skip()

class panel_treectrl ( wx.TreeCtrl ):
    def __init__( self, parent ):
        wx.TreeCtrl.__init__(self, parent, -1, style=wx.TR_HAS_BUTTONS|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER)
        self.file_tree = tree.file_tree(panel_scan, self)
        #print panel_treectrl.tree
        
        

class panel_scan ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        '''self.m_button2 = wx.Button( self, wx.ID_ANY, u"panel 2 button ", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )'''

        self.tree = panel_treectrl(self)

        bSizer5.Add(self.tree, 1, wx.EXPAND, 0)
        #file_tree = tree.file_tree(self.panelScan, self.panelScan.tree)
        #wx.EVT_TREE_ITEM_EXPANDING(self.tree, self.tree.GetId(), tree.file_tree.onExpand)                        
        
        self.SetBackgroundColour((200, 200, 200))        
        self.SetSizer( bSizer5 )
        self.Layout()
        # Connect Events
        #self.m_button2.Bind( wx.EVT_BUTTON, self.changeIntroPanel )

    def __del__( self ):
        pass
        # Virtual event handlers, overide them in your derived class
    def changeIntroPanel( self, event ):
        event.Skip()
          
class panel_largest ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        '''self.m_button2 = wx.Button( self, wx.ID_ANY, u"panel 2 button ", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )'''
        self.SetBackgroundColour((100, 100, 226))        
        self.SetSizer( bSizer5 )
        self.Layout()
        # Connect Events
        #self.m_button2.Bind( wx.EVT_BUTTON, self.changeIntroPanel )

    def __del__( self ):
        pass
        # Virtual event handlers, overide them in your derived class
    def changeIntroPanel( self, event ):
        event.Skip()
          
        
class panel_toolbar:    
    def __init__(self, parent):
        pass

      


