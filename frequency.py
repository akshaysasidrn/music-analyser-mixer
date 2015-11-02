from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write
import time


def freq(filepath,f):

	def plotSpectru(y,Fs,f):
	 n = len(y) # lungime semnal
	 k = arange(n)
	 T = n/Fs
	 frq = k/T # two sides frequency range
	 frq = frq[range(n/2)] # one side frequency range
	
	 Y = fft(y)/n # fft computing and normalization
	 Y = Y[range(n/2)]
	 
	 plot(frq,abs(Y),'r') # plotting the spectrum
	 xlabel('Freq (Hz)')
	 ylabel('|Y(freq)|')
    	 if f==1:
         	savefig('freq&amp1.png')
    	 elif f==2:
			savefig('freq&amp2.png')

	Fs = 44100;  # sampling rate
	
			
	rate,data=read(filepath)
	y=data[:,1]
	lungime=len(y)
	timp=len(y)/44100.
	t=linspace(0,timp,len(y))
	
	subplot(2,1,1)
	plot(t,y)
	xlabel('Time')
	ylabel('Amplitude')
	subplot(2,1,2)
	plotSpectru(y,Fs,f)
	time.sleep(1)
	
	
