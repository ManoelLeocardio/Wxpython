import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, size=(800, 600))

        # criar um painel
        self.panel = wx.Panel(self)

        # criar uma caixa de texto para adicionar uma nova tarefa
        self.new_task_text = wx.TextCtrl(self.panel, size=(200, -1))
        self.add_task_button = wx.Button(self.panel, label='Adicionar')

        # criar uma lista de tarefas
        self.tasks_listbox = wx.ListBox(self.panel)

        # criar botões para editar e excluir tarefas
        self.edit_task_button = wx.Button(self.panel, label='Editar')
        self.delete_task_button = wx.Button(self.panel, label='Excluir')

        # adicionar elementos ao painel
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.new_task_text, 0, wx.ALL, 5)
        sizer.Add(self.add_task_button, 0, wx.ALL, 5)
        sizer.Add(self.tasks_listbox, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.edit_task_button, 0, wx.ALL, 5)
        sizer.Add(self.delete_task_button, 0, wx.ALL, 5)
        self.panel.SetSizer(sizer)

        # definir eventos para os botões
        self.add_task_button.Bind(wx.EVT_BUTTON, self.on_add_task)
        self.edit_task_button.Bind(wx.EVT_BUTTON, self.on_edit_task)
        self.delete_task_button.Bind(wx.EVT_BUTTON, self.on_delete_task)

        self.Show(True)

    def on_add_task(self, event):
        task = self.new_task_text.GetValue()
        self.tasks_listbox.Append(task)
        self.new_task_text.Clear()

    def on_edit_task(self, event):
        selected_task = self.tasks_listbox.GetStringSelection()
        if selected_task:
            dialog = wx.TextEntryDialog(self, 'Editar Tarefa', 'Editar Tarefa', selected_task)
            if dialog.ShowModal() == wx.ID_OK:
                new_task = dialog.GetValue()
                index = self.tasks_listbox.GetSelection()
                self.tasks_listbox.SetString(index, new_task)

    def on_delete_task(self, event):
        selected_task = self.tasks_listbox.GetStringSelection()
        if selected_task:
            index = self.tasks_listbox.GetSelection()
            self.tasks_listbox.Delete(index)

app = wx.App()
frame = MainWindow(None, 'Lista de Tarefas')
app.MainLoop()
