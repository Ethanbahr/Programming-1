﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.Control
		self._label1.Font = System.Drawing.Font("Poor Richard", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.MenuHighlight
		self._label1.Location = System.Drawing.Point(268, 41)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(451, 239)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.MenuHighlight
		self._button1.Location = System.Drawing.Point(268, 298)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(113, 44)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.MenuHighlight
		self._button2.Location = System.Drawing.Point(439, 298)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(113, 44)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.MenuHighlight
		self._button3.Location = System.Drawing.Point(606, 298)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(113, 44)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.MenuHighlight
		self.ClientSize = System.Drawing.Size(956, 441)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Your Name GUI"
		self.ResumeLayout(False)



	def Button1Click(self, sender, e):
		self._label1.Text = "Ethan Bahr"

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()