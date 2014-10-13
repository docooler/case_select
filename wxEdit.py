#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# code by elaiyan (Laiyuan yang)
import wx
import os

class wxEdit(wx.Frame):
	"""docstring for wxEdit"""
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(1000,600))
		
		self.CreateStatusBar()

		# Setting up the menu.
		filemenu = wx.Menu()
		menuOpen = filemenu.Append(wx.ID_OPEN, "O&pen", "open testcase.xml")
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "code by elaiyan")
		# filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT,  "E&xit", "Terminate the program")
		
		# Creating the menubar.
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		self.SetMenuBar(menuBar)

		# Events.
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

		# self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
  # 		self.buttons = []
  # 		for i in range(0, 6):
  # 		    self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
  # 		    self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)
  		
  # 		# Use some sizers to see layout options
  # 		self.sizer = wx.BoxSizer(wx.VERTICAL)
  # 		self.sizer.Add(self.control, 1, wx.EXPAND)
  # 		self.sizer.Add(self.sizer2, 0, wx.EXPAND)
  		
  # 		#Layout sizers
  # 		self.SetSizer(self.sizer)
  # 		self.SetAutoLayout(1)
  # 		self.sizer.Fit(self)
  		self.panel = wx.Panel(self, -1)
  		self.choice = wx.Choice(self.panel,-1, (0,400))


  		self.control = wx.TextCtrl (self.panel, -1, value="please input testcases.xml", size=(980,400), style=wx.TE_MULTILINE)
  		# self.listview.SetItem()

		self.Show(True)

	def OnOpen(self, e):
		self.dirname = ""
		dlg = wx.FileDialog(self, "Choose the testcase.xml", self.dirname, "", "testcases.xml", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.control.SetValue(f.read())
			parse_xml(f)
			f.close()



			for x in xrange(1,10):
				self.choice.Append(str(x))		
		dlg.Destroy()

	def OnAbout(self, e):
		dlg = wx.MessageDialog(self, "code by elaiyan", "List case from hardware", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()
	
	def OnExit(self, e):
		self.Close(True)


def parse_xml(fd):
	return
def main():
	app = wx.App(False)
	edit = wxEdit(None, 'terass list case')
	app.MainLoop()
if __name__ == '__main__':
	main()
		
