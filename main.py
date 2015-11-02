#Importing the other files and links it via the ui
import frequency
import specinfo
import player
import sys
import bpm
import os
from pydub import AudioSegment
#import client
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
 
form_class = uic.loadUiType("pyqtgui.ui")[0]                 # Load the UI
 
class MyWindowClass(QtGui.QMainWindow, form_class):
    	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.comparison)   # Bind the event handlers
		#To browse files		
		self.pushButton_2.clicked.connect(self.search1)  
		self.pushButton_3.clicked.connect(self.search2)
		#Display spectral info on labels		
		self.rms.clicked.connect(self.fnrms)
		self.mfcc.clicked.connect(self.fnmfcc)
		self.chroma.clicked.connect(self.fnchroma)
		self.centroid.clicked.connect(self.fncentroid)						  
		#Compute frequency and amplitude		
		self.button1.clicked.connect(self.freqamp1)
		self.button2.clicked.connect(self.freqamp2)
		#compute beats per minute		
		self.bpm1.clicked.connect(self.beat1)
		self.bpm2.clicked.connect(self.beat2)
		#Mixer functionalites
		self.apply1.clicked.connect(self.cut1)
		self.apply2.clicked.connect(self.crossfade1)
		self.apply3.clicked.connect(self.cut2)
		self.apply4.clicked.connect(self.crossfade2)
		self.undo1.clicked.connect(self.fnundo1)
	   	self.undo2.clicked.connect(self.fnundo2)
		self.export_2.clicked.connect(self.exp)
		#Phonon player
		self.pushButton_4.clicked.connect(self.playfile1)
		self.pushButton_5.clicked.connect(self.playfile2)
		#flags
		self.rms,self.mfcc,self.chroma,self.centroid=0,0,0,0
		
				
	def search1(self):
		self.lineEdit.setText(QFileDialog.getOpenFileName())
		self.filepath1=self.lineEdit.text()
		
	def search2(self):
		self.lineEdit_2.setText(QFileDialog.getOpenFileName())
		self.filepath2=self.lineEdit_2.text()

	def comparison(self):
		self.filepath1=str(self.filepath1)
		self.filepath2=str(self.filepath2)
		self.song1 = AudioSegment.from_wav(self.filepath1)
		self.song2 = AudioSegment.from_wav(self.filepath2)

	def fnrms(self):
		if self.rms==0:
		 self.rms=specinfo.create('rms',self.filepath1,self.filepath2)
		 self.label_a.setScaledContents(True)
		 self.label_a.setPixmap(QPixmap("wave_rms1.png"))
		 self.label_b.setScaledContents(True)
		 self.label_b.setPixmap(QPixmap("wave_rms2.png"))
		elif self.rms==1:
		 self.label_a.setScaledContents(True)
		 self.label_a.setPixmap(QPixmap("wave_rms1.png"))
		 self.label_b.setScaledContents(True)
		 self.label_b.setPixmap(QPixmap("wave_rms2.png"))
	
	def fnmfcc(self):
	   if self.mfcc==0:
		self.mfcc=specinfo.create('mfcc',self.filepath1,self.filepath2)
		self.label_a.setScaledContents(True)
		self.label_a.setPixmap(QPixmap("wave_mfcc1.png"))
		self.label_b.setScaledContents(True)
		self.label_b.setPixmap(QPixmap("wave_mfcc2.png"))
	   elif self.mfcc==1:
		self.label_a.setScaledContents(True)
		self.label_a.setPixmap(QPixmap("wave_mfcc1.png"))
		self.label_b.setScaledContents(True)
		self.label_b.setPixmap(QPixmap("wave_mfcc2.png"))

	def fnchroma(self):
	  if self.chroma==0:
		self.chroma=specinfo.create('chroma',self.filepath1,self.filepath2)
		self.label_a.setScaledContents(True)
		self.label_a.setPixmap(QPixmap("wave_chroma1.png"))
		self.label_b.setScaledContents(True)
		self.label_b.setPixmap(QPixmap("wave_chroma2.png"))
	  elif self.chroma==1:
		self.label_a.setScaledContents(True)
		self.label_a.setPixmap(QPixmap("wave_chroma1.png"))
		self.label_b.setScaledContents(True)
		self.label_b.setPixmap(QPixmap("wave_chroma2.png"))

	def fncentroid(self):
	  if self.centroid==0:
		self.centroid=specinfo.create('centroid',self.filepath1,self.filepath2)
		self.label_a.setScaledContents(True)
		self.label_a.setPixmap(QPixmap("wave_centroid1.png"))
		self.label_b.setScaledContents(True)
		self.label_b.setPixmap(QPixmap("wave_centroid2.png"))
	  elif self.centroid==1:
		self.label_a.setScaledContents(True)
		self.label_a.setPixmap(QPixmap("wave_centroid1.png"))
		self.label_b.setScaledContents(True)
		self.label_b.setPixmap(QPixmap("wave_centroid2.png"))

	def freqamp1(self):
		flag=1
		frequency.freq(self.filepath1,flag)
		self.fnalabel1.setScaledContents(True)
		self.fnalabel1.setPixmap(QPixmap("freq&amp1.png"))

	def freqamp2(self):
		flag=2
		frequency.freq(self.filepath2,flag)
		self.fnalabel2.setScaledContents(True)
		self.fnalabel2.setPixmap(QPixmap("freq&amp2.png"))		

	def beat1(self):
		flag=1
		b=bpm.bperm(self.filepath1,3,flag)	
		self.bpmlabel1.setScaledContents(True)
		self.bpmlabel1.setPixmap(QPixmap("bpm1.png"))
		self.bpml1.setText(str(b))		

	def beat2(self):
		flag=2
		b=bpm.bperm(self.filepath2,3,flag)	
		self.bpmlabel2.setScaledContents(True)
		self.bpmlabel2.setPixmap(QPixmap("bpm2.png"))
		self.bpml2.setText(str(b))

	def cut1(self):
	    	cutf=int(self.lineEdit_3.text())
		cutto=int(self.lineEdit_4.text())
		cutf=cutf*1000
		cutto=cutto*1000
		self.temp1 = self.song1
      		self.song1 = self.song1[cutf:cutto]

	def cut2(self):
	    	cutf=int(self.lineEdit_5.text())
		cutto=int(self.lineEdit_6.text())
		cutf=cutf*1000
		cutto=cutto*1000
		self.temp1 = self.song2
        	self.song2 = self.song2[cutf:cutto]

	def crossfade1(self):
		crossf=int(self.lineEdit_7.text())
		crossto=int(self.lineEdit_8.text())
		crossf=crossf*1000
		crossto=crossto*1000
		self.temp1 = self.song1
		self.song1 = self.song1.fade_in(crossf).fade_out(crossto)

	def crossfade2(self):
		crossf=int(self.lineEdit_9.text())
		crossto=int(self.lineEdit_10.text())
		crossf=crossf*1000
		crossto=crossto*1000
		self.temp2 = self.song2
		self.song2 = self.song2.fade_in(crossf).fade_out(crossto)

	def fnundo1(self):
		self.song1=self.temp1

	def fnundo2(self):
		self.song2=self.temp2

	def exp(self):
		self.merged=self.song1+self.song2
		self.merged.export("mixed.mp3", format="mp3")

	def playfile1(self):
		player.play(self.filepath1)

	def playfile2(self):
		player.play(self.filepath2)


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()	
