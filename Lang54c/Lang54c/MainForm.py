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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._button1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(268, 308)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(157, 74)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(293, 95)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(106, 30)
		self._label1.TabIndex = 1
		self._label1.Text = "label1"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(493, 95)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(209, 30)
		self._textBox1.TabIndex = 2
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._button2.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(431, 308)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(157, 74)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._button3.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(594, 308)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(157, 74)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(493, 131)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(209, 30)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(493, 167)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(209, 30)
		self._textBox3.TabIndex = 6
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(293, 236)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(106, 30)
		self._label3.TabIndex = 10
		self._label3.Text = "label3"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Font = System.Drawing.Font("Modern No. 20", 17.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(293, 271)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(106, 30)
		self._label4.TabIndex = 11
		self._label4.Text = "label4"
		# 
		# textBox4
		# 
		self._textBox4.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(493, 203)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(209, 30)
		self._textBox4.TabIndex = 12
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(493, 236)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(209, 30)
		self._label2.TabIndex = 13
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(493, 272)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(209, 30)
		self._label5.TabIndex = 14
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(947, 442)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang54c"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pi = 3.14159
		radius = float(self._textBox1.Text)
		area = pi * radius ** 2
		self._label2.Text = str(area)
		
		# To be continued !!!!!!!!!!!!!!!!!!!!!!
		
		# + - * / % 	** pow	// divide & round down
		#int (Integer): Whole number, positive or negative
		# float (Floating-Point Number): any number w/ a decimal
		# str (String): a string of text


	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label2.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()