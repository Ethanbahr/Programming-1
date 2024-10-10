import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(55, 334)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(143, 46)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.Info
		self._textBox1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(155, 114)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(243, 36)
		self._textBox1.TabIndex = 5
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(204, 334)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 46)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(311, 334)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(86, 46)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.Info
		self._textBox2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(155, 156)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(243, 36)
		self._textBox2.TabIndex = 9
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.SystemColors.Info
		self._textBox3.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(154, 198)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(243, 36)
		self._textBox3.TabIndex = 10
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MintCream
		self._label1.Font = System.Drawing.Font("Palatino Linotype", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(219, 76)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 35)
		self._label1.TabIndex = 11
		self._label1.Text = "Inputs"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MintCream
		self._label2.Font = System.Drawing.Font("Palatino Linotype", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(119, 256)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(125, 35)
		self._label2.TabIndex = 12
		self._label2.Text = "Outputs"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MintCream
		self._label3.Font = System.Drawing.Font("Palatino Linotype", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 67)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(125, 167)
		self._label3.TabIndex = 13
		self._label3.Text = "Put a number in each of the three textboxes."
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Font = System.Drawing.Font("Palatino Linotype", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(255, 237)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(143, 35)
		self._label5.TabIndex = 15
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label6.Font = System.Drawing.Font("Palatino Linotype", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(254, 283)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(143, 35)
		self._label6.TabIndex = 16
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SeaGreen
		self.ClientSize = System.Drawing.Size(437, 430)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "lang58b"
		self.ResumeLayout(False)
		self.PerformLayout()
		


	def Button1Click(self, sender, e):
		a = int(self._textBox1.Text)
		nega = a - a - a
		b = int(self._textBox2.Text)
		negb = b - b - b
		c = int(self._textBox3.Text)
		negc = c - c - c
		x = 0 #To be added
		root = negb + (b [- 4 * a * c]) / 2 * a
		rootII = pass
		rootIII = pass
		self._label5.Text = rootII
		self._label6.Text = rootIII
		# + 
		# - 
		# * 
		# / 
		# % 	
		# ** pow (Exponent)
		# // (divide & round down)
		# .sqrt (Square root)
		#int (Integer): Whole number, positive or negative
		# float (Floating-Point Number): any number w/ a decimal
		# str (String): a string of text


	def Button2Click(self, sender, e):
		self._label5.Text = ""
		self._label6.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()