import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumSpringGreen
		self._button1.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.MintCream
		self._button1.Location = System.Drawing.Point(3, 228)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(138, 51)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MediumSpringGreen
		self._button2.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.MintCream
		self._button2.Location = System.Drawing.Point(147, 228)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 51)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MediumSpringGreen
		self._button3.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.MintCream
		self._button3.Location = System.Drawing.Point(270, 228)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(121, 51)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.MintCream
		self._textBox1.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(156, 23)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(235, 30)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.MintCream
		self._textBox2.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(156, 96)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(235, 30)
		self._textBox2.TabIndex = 4
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label1.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(3, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(147, 44)
		self._label1.TabIndex = 5
		self._label1.Text = "Enter total price:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label2.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(3, 74)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(147, 72)
		self._label2.TabIndex = 6
		self._label2.Text = "Enter amount paid:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label3.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(3, 164)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(147, 44)
		self._label3.TabIndex = 7
		self._label3.Text = "Change due:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightGray
		self._label4.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(156, 171)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(235, 30)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumSeaGreen
		self.ClientSize = System.Drawing.Size(427, 303)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog58t"
		self.ResumeLayout(False)
		self.PerformLayout()
		

	def Button1Click(self, sender, e):
		pass
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
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()