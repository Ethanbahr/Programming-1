import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ScrollBar
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(376, 77)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(245, 31)
		self._textBox1.TabIndex = 0
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.ScrollBar
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(376, 114)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(245, 31)
		self._textBox2.TabIndex = 1
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(195, 77)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(122, 31)
		self._label1.TabIndex = 2
		self._label1.Text = "Inputs"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(195, 287)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(122, 31)
		self._label3.TabIndex = 4
		self._label3.Text = "Average"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(195, 239)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(122, 31)
		self._label4.TabIndex = 5
		self._label4.Text = "Sum"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(376, 239)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(245, 31)
		self._label5.TabIndex = 6
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(376, 287)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(245, 31)
		self._label6.TabIndex = 7
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(195, 339)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(137, 57)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(351, 339)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(137, 57)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(517, 339)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(137, 57)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.SystemColors.ScrollBar
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(376, 151)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(245, 31)
		self._textBox3.TabIndex = 11
		self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.SystemColors.ScrollBar
		self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(376, 188)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(245, 31)
		self._textBox4.TabIndex = 12
		self._textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.Highlight
		self.ClientSize = System.Drawing.Size(960, 442)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		sum = int(self._textBox1.Text) + int(self._textBox2.Text) + int(self._textBox3.Text) + int(self._textBox4.Text)
		avg = sum / 4.0
		self._label5.Text = str(sum)
		self._label6.Text = str(avg)
		
		# + - * / % 	** pow	// divide & round down
		#int (Integer): Whole number, positive or negative
		# float (Floating-Point Number): any number w/ a decimal
		# str (String): a string of text

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()