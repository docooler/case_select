#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# code by elaiyan (Laiyuan yang)
import wx
import os
import testcases

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
		menuSave = filemenu.Append(wx.ID_SAVE, "S&ave", "save file")
		
		# Creating the menubar.
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		self.SetMenuBar(menuBar)

		# Events.
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		self.Bind(wx.EVT_MENU, self.OnSave, menuSave)

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
  		
  		self.control = wx.TextCtrl (self.panel, -1, value="please input testcases.xml", size=(980,400), style=wx.TE_MULTILINE)
  		wx.StaticText(self.panel, -1, label="filer condition", pos=(250,400))
  		wx.StaticText(self.panel, -1, label="hardware", pos=(25,425))
  		self.choice = wx.Choice(self.panel,-1, (0,450), size=(120,20))
  		wx.StaticText(self.panel, -1, label="number", pos=(300,425))
  		self.numLabel = wx.StaticText(self.panel, -1, label="", pos=(300,425))

  		filterBtn = wx.Button(self.panel, -1, "Filter Start", pos=(600, 425))
  		self.Bind(wx.EVT_BUTTON, self.OnFilterStart, filterBtn)
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
			f.close()
			self.tcs = testcases.TestCases(os.path.join(self.dirname, self.filename))
			pdt = self.tcs.getAllProductType()
			for x in sorted(pdt.keys()):
				self.choice.Append(x)		

		dlg.Destroy()
	def OnSave(self, e):
		if self.dirname == None:
			self.dirname = os.getcwd()
		dlg = wx.FileDialog(self, "please choice save file", self.dirname, "", "*.txt", wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			filename = dlg.GetFilename()
			dirname = dlg.GetDirectory()
			self.control.SaveFile(os.path.join(dirname, filename))
			
		

	def OnAbout(self, e):
		dlg = wx.MessageDialog(self, "code by elaiyan", "List case from hardware", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()
	
	def OnExit(self, e):
		self.Close(True)
	def OnFilterStart(self, e):
		index = self.choice.GetSelection()
		if index == wx.NOT_FOUND:
			dlg = wx.MessageDialog(self, "code by elaiyan", "please select hardware", wx.OK)
			dlg.ShowModal()
			dlg.Destroy()
		pdt = self.choice.GetString(index)
		tcs = self.tcs
		content = tcs.filterByProductType(pdt)
		# print content
		display = ""
		for x in content:
			x += "\n"
			display += x.decode('utf8')

		self.control.SetValue(display)
		num = tcs.getAllProductType()[pdt]
		disNum = str(num).decode('utf8')
		self.numLabel.Label(disNum)



def parse_xml(fd):
	return
def main():
	app = wx.App(False)
	edit = wxEdit(None, 'terass list case')
	app.MainLoop()
if __name__ == '__main__':
	main()
		
