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
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DodgerBlue
		self._button1.Location = System.Drawing.Point(12, 257)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(91, 43)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DodgerBlue
		self._button2.Location = System.Drawing.Point(109, 257)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(76, 43)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DodgerBlue
		self._button3.Location = System.Drawing.Point(191, 257)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(81, 43)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SkyBlue
		self._label3.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 15)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(55, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Input:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.DodgerBlue
		self._textBox1.Location = System.Drawing.Point(109, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(163, 29)
		self._textBox1.TabIndex = 7
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.DodgerBlue
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 20
		self._listBox1.Location = System.Drawing.Point(12, 47)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(260, 204)
		self._listBox1.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DodgerBlue
		self.ClientSize = System.Drawing.Size(284, 312)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		header = "Even Num:\tSum:"
		self._listBox1.Items.Add(header)
		sum = 0
		for num in range(2,(int(self._textBox1.Text)+2),2):
			sum 	+= num
			line 	= str(num) + "\t\t" + str(sum) 
			self._listBox1.Items.Add(line)
	
	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()