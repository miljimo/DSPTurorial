import wx;

class DataAnalyserWindow(wx.Frame):

    def __init__(self,parent,  **kwargs):
        super().__init__(parent , **kwargs);



if(__name__ =="__main__"):
  
    app = wx.App();

    frame  =  DataAnalyserWindow(None);

    frame.Show();

    app.MainLoop();
