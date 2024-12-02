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
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkBlue
		self._button1.Font = System.Drawing.Font("Kunstler Script", 21.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.SaddleBrown
		self._button1.Location = System.Drawing.Point(12, 66)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(110, 48)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LimeGreen
		self._label1.Font = System.Drawing.Font("Jokerman", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Red
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(110, 46)
		self._label1.TabIndex = 1
		self._label1.Text = "Input:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightPink
		self._textBox1.Font = System.Drawing.Font("Chiller", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(137, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(135, 20)
		self._textBox1.TabIndex = 2
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MintCream
		self._button2.Font = System.Drawing.Font("Matura MT Script Capitals", 24, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.SaddleBrown
		self._button2.Location = System.Drawing.Point(145, 101)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(110, 67)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Black
		self._button3.Font = System.Drawing.Font("Goudy Stout", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Indigo
		self._button3.Location = System.Drawing.Point(1, 120)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(138, 48)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Aquamarine
		self._label2.Font = System.Drawing.Font("Gigi", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Crimson
		self._label2.Location = System.Drawing.Point(128, 54)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(153, 46)
		self._label2.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Yellow
		self.ClientSize = System.Drawing.Size(284, 177)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		input 	  = self._textBox1.Text
		factorial = math.factorial(long(input))
		self._label2.Text = str(factorial)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()