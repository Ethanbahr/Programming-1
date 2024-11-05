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
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 330)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(96, 49)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(108, 330)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(96, 49)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(210, 330)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(96, 49)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.White
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(294, 316)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightGray
		self.ClientSize = System.Drawing.Size(318, 391)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122b"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Hours:\t\tPay:"
		self.listBox1.items.add(header)
		for num in range(0,41):
			pay = num * 4
			line = str(num) + "\t\t" + str(int(pay))
			self.listBox1.items.add(line)
			

	def Button2Click(self, sender, e):
		self.listBox1.items.clear()

	def Button3Click(self, sender, e):
		Application.Exit()