import wx
class DrawingPanel(wx.Panel):
    def __init__(self, parent):
        super(DrawingPanel, self).__init__(parent)

        # inicializar variáveis
        self.drawing = False
        self.last_pos = None
        self.lines = []

        # definir eventos de mouse
        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_mouse_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_motion)

        # definir eventos de pintura
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_mouse_down(self, event):
        self.drawing = True
        self.last_pos = event.GetPosition()

    def on_mouse_up(self, event):
        self.drawing = False
        self.last_pos = None

    def on_mouse_motion(self, event):
        if self.drawing:
            new_pos = event.GetPosition()
            line = (self.last_pos, new_pos)
            self.lines.append(line)
            self.last_pos = new_pos
            self.Refresh()

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        for line in self.lines:
            dc.DrawLine(*line)

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, size=(800, 600))

        # criar um painel
        self.panel = wx.Panel(self)

        # criar um painel de desenho
        self.drawing_panel = DrawingPanel(self.panel)

        # adicionar o painel de desenho ao painel principal
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.drawing_panel, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)

        self.Show(True)

app = wx.App()
frame = MainWindow(None, 'Desenho')
app.MainLoop()
