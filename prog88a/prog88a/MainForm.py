import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
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
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSalmon
		self._label1.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(101, 32)
		self._label1.TabIndex = 0
		self._label1.Text = "Num1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSalmon
		self._label2.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(101, 32)
		self._label2.TabIndex = 1
		self._label2.Text = "Num2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSalmon
		self._label3.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 122)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(101, 32)
		self._label3.TabIndex = 2
		self._label3.Text = "Sum:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSalmon
		self._label4.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 164)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(129, 32)
		self._label4.TabIndex = 3
		self._label4.Text = "Difference:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSalmon
		self._label5.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 202)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(101, 32)
		self._label5.TabIndex = 4
		self._label5.Text = "Product:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightSalmon
		self._label6.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 240)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(101, 32)
		self._label6.TabIndex = 5
		self._label6.Text = "Average:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightSalmon
		self._label7.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(12, 280)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(101, 32)
		self._label7.TabIndex = 6
		self._label7.Text = "Distance:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.LightSalmon
		self._label8.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(12, 320)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(101, 32)
		self._label8.TabIndex = 7
		self._label8.Text = "Max:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.LightSalmon
		self._label9.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(12, 362)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(101, 32)
		self._label9.TabIndex = 8
		self._label9.Text = "Min:"
		self._label9.Click += self.Label9Click
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.PeachPuff
		self._label10.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(147, 122)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(176, 32)
		self._label10.TabIndex = 9
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.PeachPuff
		self._label11.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(147, 164)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(176, 32)
		self._label11.TabIndex = 10
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.PeachPuff
		self._label12.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(147, 202)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(176, 32)
		self._label12.TabIndex = 11
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.PeachPuff
		self._label13.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(147, 240)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(176, 32)
		self._label13.TabIndex = 12
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.PeachPuff
		self._label14.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(147, 280)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(176, 32)
		self._label14.TabIndex = 13
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.PeachPuff
		self._label15.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(147, 320)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(176, 32)
		self._label15.TabIndex = 14
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.PeachPuff
		self._label16.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(147, 362)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(176, 32)
		self._label16.TabIndex = 15
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSalmon
		self._button1.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 397)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(115, 45)
		self._button1.TabIndex = 16
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSalmon
		self._button2.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(147, 397)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(115, 45)
		self._button2.TabIndex = 17
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSalmon
		self._button3.Font = System.Drawing.Font("Nirmala Text", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(278, 397)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(115, 45)
		self._button3.TabIndex = 18
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Linen
		self._textBox1.Font = System.Drawing.Font("Nirmala Text", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(147, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(176, 37)
		self._textBox1.TabIndex = 19
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Linen
		self._textBox2.Font = System.Drawing.Font("Nirmala Text", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(147, 52)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(176, 37)
		self._textBox2.TabIndex = 20
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Silver
		self.ClientSize = System.Drawing.Size(430, 445)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
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
		self.Name = "MainForm"
		self.Text = "prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e): # Calculate
		num1. = int(self._textBox1.Text)
		num2. = int(self._textBox2.Text)
		Sum = num1 + num2
		Dif = num1 - num2
		Prod = num1 / num2
		Avg = Sum / 2
		Abs = abs(Dif)
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
			#Min = num2
		else
			Max = num2
			
		if Max == num1
			Min = num2
		else
			Min = num1
		
		# TODO: put the rest of the nums in labels and finish clear btn
		self._label10.text = str(Sum)
		self._label11.text = str(Dif)
		self._label12.text = str(Prod)
		self._label13.text = str(Avg)
		self._label14.text = str(Abs)
		self._label15.text = str(Max)
		self._label16.Text = str(Min)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._textBox5.Text = ""
		self._textBox6.Text = ""
		self._textBox7.Text = ""
		self._textBox8.Text = ""
		self._textBox9.Text = ""
		self._textBox10.Text = ""
		self._textBox11.Text = ""
		self._textBox12.Text = ""
		self._textBox13.Text = ""
		self._textBox14.Text = ""
		self._textBox15.Text = ""
		self._textBox16.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()