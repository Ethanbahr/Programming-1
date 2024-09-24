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
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.HighlightText
		self._label1.Font = System.Drawing.Font("Monotype Corsiva", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label1.Location = System.Drawing.Point(103, 46)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(781, 265)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.HighlightText
		self._button1.Font = System.Drawing.Font("Monotype Corsiva", 20.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button1.Location = System.Drawing.Point(231, 337)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(129, 53)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.HighlightText
		self._button2.Font = System.Drawing.Font("Monotype Corsiva", 20.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button2.Location = System.Drawing.Point(420, 337)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(129, 53)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.HighlightText
		self._button3.Font = System.Drawing.Font("Monotype Corsiva", 20.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button3.Location = System.Drawing.Point(591, 337)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(129, 53)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(955, 442)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Favorite Club GUI"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Minecraft Club"

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()