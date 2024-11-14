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
		self._button1.BackColor = System.Drawing.Color.Cornsilk
		self._button1.Font = System.Drawing.Font("Monotype Corsiva", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(73, 335)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(95, 49)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Cornsilk
		self._button2.Font = System.Drawing.Font("Monotype Corsiva", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(198, 335)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(95, 49)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Cornsilk
		self._button3.Font = System.Drawing.Font("Monotype Corsiva", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(320, 335)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(95, 49)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Cornsilk
		self._listBox1.Font = System.Drawing.Font("Monotype Corsiva", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 25
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(467, 304)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightGreen
		self.ClientSize = System.Drawing.Size(491, 396)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122i"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Number:" + "\t\t" + "Cube Root:" + "\t\t" + "Num Cubed:"
		self._listBox1.Items.Add(header)
		for num in range(-25,26):
			nc 		= num**3
			ncr  	= num
			if ncr <=0:
				ncr2 = -(abs(ncr)**(1.0/3))
			else:
				ncr2 = (abs(num)**(1.0/3))
			ncr2r = round((ncr2),5)
		#	if ncr2**3 is num:
		#		ncr2 = ncr2
		#	else:
		#		ncr2 = "error"
		#	^^ Error finder-er thingy or something idk^^
			line 	= str(num) + "\t\t" + str(ncr2r) + "\t\t" + str(nc)
			self._listBox1.Items.Add(line)
			# Fix !!!!

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()