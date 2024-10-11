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
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumSpringGreen
		self._button1.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.MintCream
		self._button1.Location = System.Drawing.Point(3, 382)
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
		self._button2.Location = System.Drawing.Point(147, 382)
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
		self._button3.Location = System.Drawing.Point(270, 382)
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
		self._label3.Size = System.Drawing.Size(147, 69)
		self._label3.TabIndex = 7
		self._label3.Text = "Change due (total):"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightGray
		self._label4.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(156, 183)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(235, 30)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label5.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(3, 247)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(119, 44)
		self._label5.TabIndex = 9
		self._label5.Text = "Dollars:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label6.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(3, 301)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(119, 44)
		self._label6.TabIndex = 10
		self._label6.Text = "Quarters:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label7.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(261, 247)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(94, 44)
		self._label7.TabIndex = 11
		self._label7.Text = "Dimes:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label8.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(261, 301)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(94, 44)
		self._label8.TabIndex = 12
		self._label8.Text = "Nickels:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label9.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(489, 247)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(147, 44)
		self._label9.TabIndex = 13
		self._label9.Text = "Pennies"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.LightGray
		self._label10.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.Black
		self._label10.Location = System.Drawing.Point(128, 254)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(115, 30)
		self._label10.TabIndex = 14
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.LightGray
		self._label11.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.Black
		self._label11.Location = System.Drawing.Point(128, 308)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(115, 30)
		self._label11.TabIndex = 15
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.LightGray
		self._label12.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.Color.Black
		self._label12.Location = System.Drawing.Point(361, 254)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(115, 30)
		self._label12.TabIndex = 16
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.LightGray
		self._label13.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.Black
		self._label13.Location = System.Drawing.Point(361, 308)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(115, 30)
		self._label13.TabIndex = 17
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.LightGray
		self._label14.Font = System.Drawing.Font("Perpetua Titling MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.Color.Black
		self._label14.Location = System.Drawing.Point(505, 301)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(115, 30)
		self._label14.TabIndex = 18
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumSeaGreen
		self.ClientSize = System.Drawing.Size(661, 436)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
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
		tp = float(self._textBox1.Text)
		ap = float(self._textBox2.Text)
		dlrs = 0
		qtrs = 0
		dimes = 0
		nckls = 0
		pns = 0
		cdt = ap - tp
		self._label4.Text = str(cdt)
		self._label10.Text = str(dlrs)
		self._label11.Text = str(qtrs)
		self._label12.Text = str(dimes)
		self._label13.Text = str(nckls)
		self._label14.Text = str(pns)
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
