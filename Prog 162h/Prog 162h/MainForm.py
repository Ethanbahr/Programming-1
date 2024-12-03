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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Salmon
		self._button1.Font = System.Drawing.Font("Perpetua Titling MT", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(3, 174)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(150, 45)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Salmon
		self._button2.Font = System.Drawing.Font("Perpetua Titling MT", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(159, 174)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(94, 45)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Salmon
		self._button3.Font = System.Drawing.Font("Perpetua Titling MT", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(259, 174)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(99, 45)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Salmon
		self._label1.Font = System.Drawing.Font("Perpetua Titling MT", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(3, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(76, 25)
		self._label1.TabIndex = 3
		self._label1.Text = "Guests:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Salmon
		self._label2.Font = System.Drawing.Font("Perpetua Titling MT", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(3, 60)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(76, 25)
		self._label2.TabIndex = 4
		self._label2.Text = "Chairs:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Salmon
		self._label3.Font = System.Drawing.Font("Perpetua Titling MT", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(3, 98)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(141, 25)
		self._label3.TabIndex = 5
		self._label3.Text = "Permutations:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Salmon
		self._label4.Font = System.Drawing.Font("Perpetua Titling MT", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(3, 135)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(176, 25)
		self._label4.TabIndex = 6
		self._label4.Text = "Guests Standing:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightSalmon
		self._textBox1.Font = System.Drawing.Font("Perpetua Titling MT", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(222, 28)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(136, 26)
		self._textBox1.TabIndex = 7
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightSalmon
		self._textBox2.Font = System.Drawing.Font("Perpetua Titling MT", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(222, 60)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(136, 26)
		self._textBox2.TabIndex = 8
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Coral
		self._label5.Font = System.Drawing.Font("Perpetua Titling MT", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(222, 98)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(136, 25)
		self._label5.TabIndex = 9
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Coral
		self._label6.Font = System.Drawing.Font("Perpetua Titling MT", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(222, 135)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(136, 25)
		self._label6.TabIndex = 10
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Navy
		self.ClientSize = System.Drawing.Size(363, 231)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog 162h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		guests 		 = int(self._textBox1.Text)
		chairs 		 = int(self._textBox2.Text)
		permutations = guests
		standing 	 = guests - chairs
		for num in range(guests - 1, standing, -1):
			permutations *= num
		self._label6.Text = str(standing)
		self._label5.Text = str(permutations)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text 	= ""
		self._label6.Text 	= ""

	def Button3Click(self, sender, e):
		Application.Exit()