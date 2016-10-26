#!/usr/bin/env python

import wx, os, time
import os.path, dircache
import threading
import natsort
from progress import thread_progress

#from utils import utils
from math import log


class file_tree:

    def __init__(self, parent, tree):
        # this is just setup boilerplate
        # our tree object, self.tree

        self.totalBytes = 0
        print tree
        self.tree = tree
        #sizer.Fit(parent)
        #sizer.SetSizeHints(parent)
        #parent.Layout()
        # register the self.onExpand function to be called


    def sizeof_fmt(self, num):
        unit_list = zip(['bytes', 'kB', 'MB', 'GB', 'TB', 'PB'], [0, 0, 1, 2, 2, 2])
        """Human friendly file size"""
        if num > 1:
            exponent = min(int(log(num, 1024)), len(unit_list) - 1)
            quotient = float(num) / 1024**exponent
            unit, num_decimals = unit_list[exponent]
            format_string = '{:.%sf} {}' % (num_decimals)
            return format_string.format(quotient, unit)
        if num == 0:
            return '0 bytes'
        if num == 1:
            return '1 byte'

    def get_dir_size(self, top):
        total_bytes = 0
        for root, dirs, files in os.walk(top, topdown=False):
            for name in files:
                filename = os.path.join(root, name)
                try:
                    total_bytes += os.path.getsize(filename)
                except:
                    total_bytes += 0
                    pass
                        
            for name in dirs:
                pass
                #print str(os.path.join(root, name))

        return str(total_bytes)        

           
    def onExpand(self, event):
        th_progress = thread_progress(1, "ThreadProgress", 1, "Aguarde, expandindo diretorio...")
        th_progress.start()
        
        # get the wxID of the entry to expand and check it's validity
        itemID = event.GetItem()
        if not itemID.IsOk():
            itemID = self.tree.GetSelection()
        
        # only build that tree if not previously expanded
        old_pydata = self.tree.GetPyData(itemID)
        if old_pydata[1] == False:
            # clean the subtree and rebuild it
            self.tree.DeleteChildren(itemID)
            self.extendTree(itemID)
            self.tree.SetPyData(itemID,(old_pydata[0], True))
        th_progress.exitFlag = 1            
           
    def buildTree(self, treectrl, rootdir):
        '''Add a new root element and then its children'''
        self.totalBytes = float(self.get_dir_size(rootdir))
        dirsize = self.sizeof_fmt(self.totalBytes)
        print dirsize
        self.rootID = treectrl.AddRoot(rootdir+"["+dirsize+"]")
        treectrl.SetPyData(self.rootID, (rootdir,1))

        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        self.fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        self.fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN,   wx.ART_OTHER, isz))
        self.fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        treectrl.SetImageList(il)
        self.il = il        
        
        treectrl.SetItemImage(self.rootID, self.fldridx, wx.TreeItemIcon_Normal)
        treectrl.SetItemImage(self.rootID, self.fldropenidx, wx.TreeItemIcon_Expanded)        
        self.extendTree(self.rootID)
        treectrl.Expand(self.rootID)
        
    def extendTree(self, parentID):
        #excludeDirs=["c:\\System Volume Information","/System Volume Information" ,"/Arquivos de Programas" ,"/Documents and Settings"]
        excludeDirs=[]
        
        # retrieve the associated absolute path of the parent
        parentDir = self.tree.GetPyData(parentID)[0]
        
        #subdirs = natsort.natsorted(dircache.listdir(parentDir))
        subdirs = dircache.listdir(parentDir)
        subdirs.sort()
            
        for child in subdirs:
            child_path = os.path.join(parentDir,child)
            if os.path.isdir(child_path) and not os.path.islink(child):
                if child_path in excludeDirs:
                    continue                
                # add the child to the parent
                dirsize = self.sizeof_fmt(float(self.get_dir_size(child_path)))
                childID = self.tree.AppendItem(parentID, child+"["+dirsize+"]")
                
                # associate the full child path with its tree entry
                self.tree.SetPyData(childID, (child_path, False))
                self.tree.SetItemImage(childID, self.fldridx, wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(childID, self.fldropenidx, wx.TreeItemIcon_Expanded)                
                
                newParent = child
                newParentID = childID
                newParentPath = child_path
                #newsubdirs = natsort.natsorted(dircache.listdir(newParentPath))
                try:
                    newsubdirs = dircache.listdir(newParentPath)
                    newsubdirs.sort()
                    for grandchild in newsubdirs:
                        grandchild_path = os.path.join(newParentPath,grandchild)
                        if os.path.isdir(grandchild_path) and not os.path.islink(grandchild_path):                        
                            grandchildID = self.tree.AppendItem(newParentID, grandchild)
                            self.tree.SetPyData(grandchildID, (grandchild_path,False))
                        else:
                            self.tree.AppendItem(newParentID, grandchild_path)
                except:
                    print "ACESSO NEGADO: "+newParentPath
                    pass
                    
                    
            else:
                filename = child_path.split("\\")[-1]
                try:
                    filesize = str(self.sizeof_fmt(os.path.getsize(child_path)))
                except:
                    filesize = str('[Erro lendo arquivo]')
                    pass
                childID = self.tree.AppendItem(parentID, filename+"["+filesize+"]")
                self.tree.SetItemImage(childID, self.fileidx, wx.TreeItemIcon_Normal)                                      


