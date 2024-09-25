import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label1.Font = System.Drawing.Font("Palatino Linotype", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.HighlightText
		self._label1.Location = System.Drawing.Point(107, 23)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(772, 286)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button1.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.HighlightText
		self._button1.Location = System.Drawing.Point(319, 312)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(96, 45)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button4.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.ForeColor = System.Drawing.SystemColors.HighlightText
		self._button4.Location = System.Drawing.Point(459, 312)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(96, 45)
		self._button4.TabIndex = 2
		self._button4.Text = "Clear"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button5.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.ForeColor = System.Drawing.SystemColors.HighlightText
		self._button5.Location = System.Drawing.Point(593, 312)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(96, 45)
		self._button5.TabIndex = 3
		self._button5.Text = "Exit"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.HighlightText
		self.ClientSize = System.Drawing.Size(959, 439)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Phone Numbers GUI"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Subway - 608-758-9410 \n Italian House - 608-754-2226 \n The Chocolate Shoppe - 608-563-4150 \n Auntie Anne's Pretzels - 847-903-4446 \n Culvers - 608-758-8916 \n Jimmy Johns - 608-314-9350"

	def Button4Click(self, sender, e):
		self._label1.Text = ""

	def Button5Click(self, sender, e):
		Application.Exit()