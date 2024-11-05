
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import wx


#=============================================
#=============================================
#=============================================
#=============================================
class NDlg(wx.Dialog):
    def __init__(self, label, prot = "ascii"):
        self.label = label
        self.prot = prot
        wx.Dialog.__init__(self, None, -1, label, size = (800, 280))
        labels = ["Строка", "Формат HEX"]
        posSText = [(10, 10), (10, 80)]
        for i in range (0, len(labels)):
            text = wx.StaticText(self, wx.ID_ANY, labels[i], pos = posSText[i])
            text.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        posText = [(10, 45), (10, 115)]
        self.Value = []
        for i in range(0, len(posText)):
            temp = wx.TextCtrl(self, wx.ID_ANY, "", pos = posText[i], size = (760, 30), style = wx.TE_CENTRE)
            temp.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
            self.Value.append(temp)
        OKButton = wx.Button(self, wx.ID_ANY, "Строка в HEX", pos = (10, 185), size = (370, 30))
        OKButton.SetDefault()
        OKButton.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        OKButton.Bind(wx.EVT_BUTTON, self.CodeToHEX)
        OTButton = wx.Button(self, wx.ID_ANY, "HEX в строку", pos = (400, 185), size = (370, 30))
        OTButton.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        OTButton.Bind(wx.EVT_BUTTON, self.CodeToSTR)
        return

    def CodeToHEX(self, evt):
        string = self.Value[0].GetValue()
        print("string = " + string)
        coded = string.encode(self.prot).hex()
        print("coded " + string  + " to " + coded)
        self.Value[1].SetValue(coded)

    def CodeToSTR(self, evt):
        Hex = self.Value[1].GetValue()
        print("hex = " + Hex)
        encoded = bytes.fromhex(Hex).decode(self.prot)
        print("encoded " + Hex  + " to " + encoded)
        self.Value[0].SetValue(encoded)



ex = wx.App()
dlg = NDlg("Code it NOW", prot = "utf-8")
dlg.ShowModal() 

ex.MainLoop()
