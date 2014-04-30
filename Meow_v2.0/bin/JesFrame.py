#Boa:Frame:Frame4

import wx
import wx.richtext
import wx.lib.filebrowsebutton
import os
def create(parent):
    return Frame4(parent)

[wxID_FRAME4, wxID_FRAME4BITMAPBUTTON1, wxID_FRAME4BITMAPBUTTON2, 
 wxID_FRAME4BUTTON1, wxID_FRAME4BUTTON2, wxID_FRAME4BUTTON3, 
 wxID_FRAME4CHECKBOX1, wxID_FRAME4CHECKBOX2, wxID_FRAME4CHECKBOX3, 
 wxID_FRAME4DIRBROWSEBUTTON1, wxID_FRAME4FILEBROWSEBUTTON1, 
 wxID_FRAME4NOTEBOOK1, wxID_FRAME4RICHTEXTCTRL1, wxID_FRAME4STATICTEXT1, 
 wxID_FRAME4STATICTEXT2, wxID_FRAME4STATICTEXT3, wxID_FRAME4STATICTEXT4, 
 wxID_FRAME4STATICTEXT5, wxID_FRAME4TEXTCTRL1, wxID_FRAME4TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(20)]

class Frame4(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME4, name='', parent=prnt,
              pos=wx.Point(322, 112), size=wx.Size(785, 583),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Meow Rec-Sim v2.0')
        self.SetClientSize(wx.Size(769, 545))
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.SetIcon(wx.Icon(u'C:/Meow_v2.0/resources/Shwz-Disney-Winnie-the-pooh.ico',
              wx.BITMAP_TYPE_ICO))

        self.notebook1 = wx.Notebook(id=wxID_FRAME4NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(769, 545), style=0)

        self.fileBrowseButton1 = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Browse',
              dialogTitle='Choose a file', fileMask='*.*',
              id=wxID_FRAME4FILEBROWSEBUTTON1, initialValue='',
              labelText=u'Choose dataset', parent=self.notebook1,
              pos=wx.Point(56, 16), size=wx.Size(640, 56), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.fileBrowseButton1.Show(False)

        self.checkBox1 = wx.CheckBox(id=wxID_FRAME4CHECKBOX1,
              label=u'User Based', name='checkBox1', parent=self.notebook1,
              pos=wx.Point(288, 160), size=wx.Size(86, 24), style=0)
        self.checkBox1.SetValue(False)
        self.checkBox1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.checkBox1.Show(False)
        self.checkBox1.Enable(True)
        self.checkBox1.Bind(wx.EVT_CHECKBOX, self.OnCheckBox1Checkbox,
              id=wxID_FRAME4CHECKBOX1)

        self.checkBox2 = wx.CheckBox(id=wxID_FRAME4CHECKBOX2,
              label=u'Item Based', name='checkBox2', parent=self.notebook1,
              pos=wx.Point(288, 200), size=wx.Size(96, 24), style=0)
        self.checkBox2.SetValue(False)
        self.checkBox2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.checkBox2.Show(False)
        self.checkBox2.Bind(wx.EVT_CHECKBOX, self.OnCheckBox2Checkbox,
              id=wxID_FRAME4CHECKBOX2)

        self.staticText1 = wx.StaticText(id=wxID_FRAME4STATICTEXT1,
              label=u'Choose type of recommender', name='staticText1',
              parent=self.notebook1, pos=wx.Point(256, 112), size=wx.Size(169,
              16), style=0)
        self.staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.staticText1.Show(False)

        self.checkBox3 = wx.CheckBox(id=wxID_FRAME4CHECKBOX3, label=u'Hybrid',
              name='checkBox3', parent=self.notebook1, pos=wx.Point(288, 240),
              size=wx.Size(86, 24), style=0)
        self.checkBox3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.checkBox3.SetValue(False)
        self.checkBox3.Show(False)
        self.checkBox3.Bind(wx.EVT_CHECKBOX, self.OnCheckBox3Checkbox,
              id=wxID_FRAME4CHECKBOX3)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME4TEXTCTRL1, name='textCtrl1',
              parent=self.notebook1, pos=wx.Point(184, 304), size=wx.Size(384,
              29), style=0, value=u'Enter dataset Size')
        self.textCtrl1.Show(False)

        self.dirBrowseButton1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_FRAME4DIRBROWSEBUTTON1,
              labelText=u'Select  directory for output:', newDirectory=False,
              parent=self.notebook1, pos=wx.Point(40, 400), size=wx.Size(680,
              48), startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton1.Show(False)

        self.button1 = wx.Button(id=wxID_FRAME4BUTTON1, label=u'Click Me',
              name='button1', parent=self.notebook1, pos=wx.Point(272, 472),
              size=wx.Size(160, 32), style=0)
        self.button1.Show(False)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME4BUTTON1)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME4TEXTCTRL2, name='textCtrl2',
              parent=self.notebook1, pos=wx.Point(176, 368), size=wx.Size(392,
              21), style=0, value=u'Enter User Id')
        self.textCtrl2.Show(False)

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME4BITMAPBUTTON1, name='bitmapButton1',
              parent=self.notebook1, pos=wx.Point(248, 96), size=wx.Size(208,
              88), style=wx.BU_AUTODRAW)
        self.bitmapButton1.SetBitmapLabel(wx.Bitmap(u'C:/Meow_v2.0/resources/extractht_g.png',
              wx.BITMAP_TYPE_PNG))
        self.bitmapButton1.Bind(wx.EVT_BUTTON, self.OnBitmapButton1Button,
              id=wxID_FRAME4BITMAPBUTTON1)

        self.bitmapButton2 = wx.BitmapButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME4BITMAPBUTTON2, name='bitmapButton2',
              parent=self.notebook1, pos=wx.Point(240, 280), size=wx.Size(216,
              88), style=wx.BU_AUTODRAW)
        self.bitmapButton2.SetBitmapLabel(wx.Bitmap(u'C:/Meow_v2.0/resources/extractht_h.png',
              wx.BITMAP_TYPE_PNG))
        self.bitmapButton2.Bind(wx.EVT_BUTTON, self.OnBitmapButton2Button,
              id=wxID_FRAME4BITMAPBUTTON2)

        self.button2 = wx.Button(id=wxID_FRAME4BUTTON2, label=u'Simulate',
              name='button2', parent=self.notebook1, pos=wx.Point(288, 464),
              size=wx.Size(152, 32), style=0)
        self.button2.Show(False)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME4BUTTON2)

        self.staticText2 = wx.StaticText(id=wxID_FRAME4STATICTEXT2,
              label=u'Missing Ratings ', name='staticText2',
              parent=self.notebook1, pos=wx.Point(280, 64), size=wx.Size(114,
              19), style=0)
        self.staticText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.staticText2.Show(False)

        self.staticText3 = wx.StaticText(id=wxID_FRAME4STATICTEXT3,
              label=u'Top Recommendations', name='staticText3',
              parent=self.notebook1, pos=wx.Point(248, 72), size=wx.Size(192,
              23), style=0)
        self.staticText3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.staticText3.Show(False)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME4RICHTEXTCTRL1,
              parent=self.notebook1, pos=wx.Point(56, 112), size=wx.Size(672,
              344), style=wx.richtext.RE_MULTILINE, value='richTextCtrl1')
        self.richTextCtrl1.Show(False)

        self.button3 = wx.Button(id=wxID_FRAME4BUTTON3, label=u'Done',
              name='button3', parent=self.notebook1, pos=wx.Point(296, 472),
              size=wx.Size(120, 31), style=0)
        self.button3.Show(False)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME4BUTTON3)

        self.staticText4 = wx.StaticText(id=wxID_FRAME4STATICTEXT4,
              label=u'Made By :', name='staticText4', parent=self.notebook1,
              pos=wx.Point(608, 384), size=wx.Size(68, 18), style=0)
        self.staticText4.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.staticText5 = wx.StaticText(id=wxID_FRAME4STATICTEXT5,
              label=u'Saransh Sharma \nAnupriya Gagneja \n', name='staticText5',
              parent=self.notebook1, pos=wx.Point(560, 408), size=wx.Size(132,
              57), style=0)
        self.staticText5.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnCheckBox2Checkbox(self, event):
        a=self.checkBox2.GetValue()
        if a == True:
            self.checkBox1.Enable(False)
            self.checkBox3.Enable(False)
        else:
            self.checkBox1.Enable(True)
            self.checkBox3.Enable(True)

    def OnBitmapButton1Button(self, event):
        self.fileBrowseButton1.Show(True)
        self.checkBox1.Show(True)
        self.checkBox2.Show(True)
        self.checkBox3.Show(True)
        self.staticText1.Show(True)
        self.textCtrl1.Show(True)
        self.button1.Show(True)
        self.bitmapButton2.Show(False)
        self.bitmapButton1.Show(False)
        self.dirBrowseButton1.Show(True)
        self.staticText5.Show(False)
        self.staticText4.Show(False)
       
       
        
        
    def OnBitmapButton2Button(self, event):
        self.fileBrowseButton1.Show(True)
        self.checkBox1.Show(True)
        self.checkBox2.Show(True)
        self.checkBox3.Show(True)
        self.staticText1.Show(True)
        self.textCtrl1.Show(True)
        self.textCtrl2.Show(True)
        self.button2.Show(True)
        self.bitmapButton2.Show(False)
        self.bitmapButton1.Show(False)
        self.dirBrowseButton1.Show(True)
        self.staticText5.Show(False)
        self.staticText4.Show(False)
       

    def OnButton1Button(self, event):
        self.fileBrowseButton1.Show(False)
        self.checkBox1.Show(False)
        self.checkBox2.Show(False)
        self.checkBox3.Show(False)
        self.staticText1.Show(False)
        self.textCtrl1.Show(False)
        self.textCtrl2.Show(False)
        self.button1.Show(False)
        self.staticText2.Show(True)
        self.richTextCtrl1.Show(True)
        self.button3.Show(True)
        self.dirBrowseButton1.Show(False)
        pathd=self.fileBrowseButton1.GetValue()
        c1=self.checkBox1.GetValue()
        c2=self.checkBox2.GetValue()
        c3=self.checkBox3.GetValue()
        size=self.textCtrl1.GetValue()
        patho=self.dirBrowseButton1.GetValue()
        if c1 == True:
            path=r'C:\Meow_v2.0\bin\UserJester.py'+' '+pathd+' '+size+' '+patho+' '+'-1'
            os.system(path)
            outp=patho+'\pear_out.txt'
            fp=open(outp,'r')
            buf=fp.read()
            self.richTextCtrl1.SetValue(buf)
            
        if c2 == True:
            path=r'C:\Meow_v2.0\bin\CosSimJester.py'+' '+pathd+' '+size+' '+patho+' '+'-1'
            os.system(path)
            outp=patho+'\cos_out.txt'
            fp=open(outp,'r')
            buf=fp.read()
            self.richTextCtrl1.SetValue(buf)
            
        if c3 == True:
            path=r'C:\Meow_v2.0\bin\HybridJester.py'+' '+pathd+' '+size+' '+patho+' '+'-1'
            os.system(path)
            outp=patho+'\hybrid_out.txt'
            fp=open(outp,'r')
            buf=fp.read()
            self.richTextCtrl1.SetValue(buf)
        

    def OnButton2Button(self, event):
        self.fileBrowseButton1.Show(False)
        self.checkBox1.Show(False)
        self.checkBox2.Show(False)
        self.checkBox3.Show(False)
        self.staticText1.Show(False)
        self.textCtrl1.Show(False)
        self.button2.Show(False)
        self.staticText3.Show(True)
        self.textCtrl2.Show(False)
        self.richTextCtrl1.Show(True)
        self.dirBrowseButton1.Show(False)
        self.button3.Show(True)
        pathd=self.fileBrowseButton1.GetValue()
        c1=self.checkBox1.GetValue()
        c2=self.checkBox2.GetValue()
        c3=self.checkBox3.GetValue()
        size=self.textCtrl1.GetValue()
        patho=self.dirBrowseButton1.GetValue()
        id=self.textCtrl2.GetValue()
        if c1 == True:
            path=r'C:\Meow_v2.0\bin\UserJester.py'+' '+pathd+' '+size+' '+patho+' '+str(id)
            os.system(path)
            outp=patho+'\user_pear_out.txt'
            fp=open(outp,'r')
            buf=fp.read()
            self.richTextCtrl1.SetValue(buf)
            

        if c2 == True:
            path=r'C:\Meow_v2.0\bin\CosSimJester.py'+' '+pathd+' '+size+' '+patho+' '+str(id)
            os.system(path)
            outp=patho+'\user_cos_out.txt'
            fp=open(outp,'r')
            buf=fp.read()
            self.richTextCtrl1.SetValue(buf)
        
        if c3 == True:
            path=r'C:\Meow_v2.0\bin\HybridJester.py'+' '+pathd+' '+size+' '+patho+' '+str(id)
            os.system(path)
            outp=patho+'\user_hybrid_out.txt'
            fp=open(outp,'r')
            buf=fp.read()
            self.richTextCtrl1.SetValue(buf)
        
            
        

    def OnButton3Button(self, event):
        self.richTextCtrl1.Show(False)
        self.staticText3.Show(False)
        self.bitmapButton2.Show(True)
        self.bitmapButton1.Show(True)
        self.button3.Show(False)
        self.staticText2.Show(False)
        self.staticText5.Show(True)
        self.staticText4.Show(True)
       
    def OnCheckBox1Checkbox(self, event):
        a=self.checkBox1.GetValue()
        if a == True:
            self.checkBox2.Enable(False)
            self.checkBox3.Enable(False)
        else:
            self.checkBox2.Enable(True)
            self.checkBox3.Enable(True)

    def OnCheckBox3Checkbox(self, event):
        a=self.checkBox3.GetValue()
        if a == True:
            self.checkBox1.Enable(False)
            self.checkBox2.Enable(False)
        else:
            self.checkBox1.Enable(True)
            self.checkBox2.Enable(True)

    def OnBitmapButton3Button(self, event):
        event.Skip()

    def OnBitmapButton4Button(self, event):
        event.Skip()
