import wx
import wx.grid
import wx.lib.scrolledpanel


#----------------------
#----------------------
#----------------------
#----------------------
class GridFrame(wx.Frame):
    def __init__(self, parent, data, rlabels = None, clabels = None):
        screenSize = wx.DisplaySize()
        wx.Frame.__init__(self, parent, -1, "Label")

        self.SetMinSize((1000, 400))
        self.SetSize((1000, 400))
        Sizer = wx.FlexGridSizer(rows = 2, cols = 1, hgap = 6, vgap = 6)
        Sizer.AddGrowableCol(0, 0)
        Sizer.AddGrowableRow(0, 10)
        Sizer.AddGrowableRow(1, 1)

        self.panel1 = GridPanel(self, data, rlabels, clabels)
        self.panel2 = TextEntryPanel(self)
        self.SetMinSize((400, 400))

        Sizer.Add(self.panel1, -1, wx.EXPAND | wx.GROW | wx.ALL, 0)
        Sizer.Add(self.panel2, -1, wx.EXPAND | wx.ALL, 0)
        self.SetSizer(Sizer)
        self.Show(True)

#----------------------
#----------------------
#----------------------
#----------------------
class TextEntryPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.shift_down = False
        Sizer = wx.FlexGridSizer(rows = 1, cols = 2, hgap = 6, vgap = 6)
        Sizer.AddGrowableRow(0, 0)
        Sizer.AddGrowableCol(0, 0)

        self.Text = wx.TextCtrl(
            self, wx.ID_ANY,"", style = wx.TE_MULTILINE)
        self.Text.SetFont(wx.Font(10, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        Sizer.Add(self.Text, -1, wx.EXPAND|wx.ALL, 4)
        self.Text.SetFocus()
        self.Text.Bind(wx.EVT_CHAR_HOOK, self.AddReturn)
        self.Text.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Text.Bind(wx.EVT_KEY_UP, self.OnKeyUp)

        AddBtn = wx.Button(self, wx.ID_ANY, "Add")
        Sizer.Add(AddBtn, -1, wx.ALIGN_CENTRE|wx.ALL, 4)
        AddBtn.Bind(wx.EVT_BUTTON, self.OnAdd)

        self.SetSizer(Sizer)
        self.Fit()

    def OnAdd(self, evt):
        self.Add()

    def Add(self):
        self.parent.panel1.grid.AddNote(self.Text.GetValue())
        self.Text.SetValue("")

    def AddReturn(self, evt):
        key_code = evt.GetKeyCode()
        #print("Entered = " + chr(key_code))
        # filter unicode characters
        if key_code == wx.WXK_NONE:
            pass
        elif key_code == wx.WXK_RETURN or key_code == 370:
            if self.shift_down == False:
                if self.Text.GetValue().strip() != "":
                    self.Add()
            else:
                evt.Skip()
        else:
            evt.Skip()                     
        return

    def OnKeyUp(self, evt):
        if evt.GetKeyCode() == wx.WXK_SHIFT:
            self.shift_down = False
        evt.Skip()

    def OnKeyDown(self, evt):
        if evt.GetKeyCode() == wx.WXK_SHIFT:
            self.shift_down = True
        evt.Skip()
        
#----------------------
#----------------------
#----------------------
#----------------------
class GridPanel(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, data, rlabels, clabels):
        wx.lib.scrolledpanel.ScrolledPanel.__init__(self, parent)
        self.SetupScrolling()
        
        Sizer = wx.BoxSizer(wx.VERTICAL)
        self.grid = SimpleGrid(self, data, rlabels, clabels)
        Sizer.Add(self.grid, -1, wx.EXPAND | wx.ALL, 0)
        
        self.SetSizer(Sizer)
        self.Bind(wx.EVT_SIZE, self.ChSize)
        self.Fit()

    def ChSize(self, evt):
        if self.GetSize()[0] > 40:
            self.grid.SetColSize(0, self.GetSize()[0]-40)
        
#----------------------
#----------------------
#----------------------
#----------------------
class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent, data, rlabels, clabels):
        wx.grid.Grid.__init__(self, parent, -1)
        self.data = data
        
        self.CreateGrid(len(data), 1)
        for col in range (0, 1):
            for row in range (0, len(data)):
                self.SetCellValue(row, col, data[row])
                self.AutoSizeRow(row, True)
                self.SetReadOnly(row, col, True)
            
        self.SetSelectionBackground("gray")             
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnDClick)

        self.HideRowLabels()
        self.HideColLabels()

    def OnDClick(self, evt):
        InfoFrame("Info frame Label", self.GetCellValue(evt.GetRow(), evt.GetCol()))

    def GetValues(self):
        temp = []
        for row in range (0, self.GetNumberRows()):
            temp.append([])
            for col in range (0, self.GetNumberCols()):
                temp[row].append(self.GetCellValue(row, col))
        return temp

    def AddNote(self, note):
        self.AppendRows(1, True)
        self.Scroll(1000, 1000)
        lastRow = self.GetNumberRows()-1
        self.SetCellValue(lastRow, 0, note)
        self.AutoSizeRow(lastRow, True)
        self.SetReadOnly(lastRow, 0, True)

#----------------------
#----------------------
#----------------------
#----------------------
class InfoFrame(wx.Frame):
    def __init__(self, label, data):
        screenSize = wx.DisplaySize()
        wx.Frame.__init__(self, None, -1, label)

        self.SetMinSize((600, 200))
        Sizer = wx.FlexGridSizer(rows = 1, cols = 1, hgap = 6, vgap = 6)
        Sizer.AddGrowableCol(0, 0)
        Sizer.AddGrowableRow(0, 0)
        panel = InfoPanel(self, data)
        Sizer.Add(panel, -1, wx.EXPAND | wx.ALL, 0)
        self.SetSizer(Sizer)      
        self.Fit()
        self.Show(True)

#----------------------
#----------------------
#----------------------
#----------------------
class InfoPanel(wx.Panel):
    def __init__(self, parent, data):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        Sizer = wx.FlexGridSizer(rows = 2, cols = 1, hgap = 6, vgap = 6)
        Sizer.AddGrowableRow(0, 0)
        Sizer.AddGrowableCol(0, 0)

        Text = wx.TextCtrl(self, wx.ID_ANY, data, style = wx.TE_MULTILINE | wx.TE_READONLY)
        Sizer.Add(Text, -1, wx.EXPAND|wx.ALL, 4)
        
        Ok = wx.Button(self, wx.ID_ANY, "ОК")
        Ok.Bind(wx.EVT_BUTTON, self.OnOk)
        Ok.SetSize((150, 40))
        Sizer.Add(Ok, -1, wx.ALIGN_CENTRE|wx.ALL, 4)

        self.SetSizer(Sizer)
        self.Fit()

    def OnOk(self, evt):
        self.parent.Destroy()
        
data = "author says: Hello guys, I'm from Russia!!!"
Data = [f"Number {i} mess {data}"*5 for i in range (0, 15)]
      
app = wx.App()
frame = GridFrame(None, Data)
app.MainLoop()
