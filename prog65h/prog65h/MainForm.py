import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Silver
		self._label1.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(31, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(286, 59)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter weird British numbers in old notation here:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkGray
		self._textBox1.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(100, 71)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(140, 33)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Silver
		self._label2.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(31, 118)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(286, 59)
		self._label2.TabIndex = 2
		self._label2.Text = "Weird British numbers in current notation:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkGray
		self._label3.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(100, 187)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(140, 32)
		self._label3.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DimGray
		self._button1.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 235)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(101, 52)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DimGray
		self._button2.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(119, 235)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 52)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DimGray
		self._button3.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(228, 235)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(101, 52)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gray
		self.ClientSize = System.Drawing.Size(342, 299)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog65h"
		self.ResumeLayout(False)
		self.PerformLayout()

	# To be completed
	def Button1Click(self, sender, e):
		on = str(self._textBox1.Text)
		
		cn = 0
		
		self._label3.Text = str(cn)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()