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
		self._label3 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button1.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ControlText
		self._button1.Location = System.Drawing.Point(12, 162)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(126, 40)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button2.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(144, 162)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(86, 40)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button3.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(238, 162)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(85, 40)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Khaki
		self._label1.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 27)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(131, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Speed limit:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Khaki
		self._label3.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 78)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(158, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Vehicle Speed:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LemonChiffon
		self._label6.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(158, 122)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(165, 23)
		self._label6.TabIndex = 8
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Khaki
		self._label5.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 122)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(131, 23)
		self._label5.TabIndex = 9
		self._label5.Text = "Fine:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LemonChiffon
		self._textBox1.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(158, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(165, 30)
		self._textBox1.TabIndex = 10
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LemonChiffon
		self._textBox2.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(158, 71)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(165, 30)
		self._textBox2.TabIndex = 11
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Khaki
		self.ClientSize = System.Drawing.Size(335, 217)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog82a"
		self.ResumeLayout(False)
		self.PerformLayout()

# To be continued

	def Button1Click(self, sender, e):
		slmt = str(self._textBox1.Text)
		vspd = str(self._textBox2.Text)
		oslmt = vspd - slmt
		fine = (oslmt * 5) + 20.00
		# find error !!!!
		self._label6.Text = int(fine)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()