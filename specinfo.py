# import the pyoracle high-level functions
from pyoracle import *
import os

# Filepaths passed via the main program
def create(feat,filepath1,filepath2):
	fft_size1 = 8192
	hop_size1 = fft_size1 / 2
	fft_size2 = 8192
	hop_size2 = fft_size2 / 2
	# call the feature extractors
	features1 = make_features(filepath1, fft_size1, hop_size1, feat)
	features2 = make_features(filepath2, fft_size2, hop_size2, feat)
	thresholds = (0.001, 2.0, 0.01) # specify a range of possible thresholds
	print 'Please wait while the audio features are being extacted:'
	print '--------------------------------------------------------'
	print 'Extracting '+feat+' information:'
	ideal_t1 = calculate_ideal_threshold(thresholds, features1, feat)
	ideal_t2 = calculate_ideal_threshold(thresholds, features2, feat)
	# ideal threshold is stored in ideal_t[0][1]
	print '\nideal distance threshold of file1:', ideal_t1[0][1]
	print 'ideal distance threshold of file2:', ideal_t2[0][1]
	print '\n'
	# after determining the ideal threshold, we build an oracle using that threshold
	thresh1 = ideal_t1[0][1]
	thresh2 = ideal_t2[0][1]
	oracle1 = make_oracle(thresh1, features1, feat)
	oracle2 = make_oracle(thresh2, features2, feat)
	# then write an image of the oracle to disk
	if feat =='rms':
	 draw_oracle(oracle1, 'wave_rms1.png', size=(800,300))
	 draw_oracle(oracle2, 'wave_rms2.png', size=(800,300))
	 return 1
	elif feat=='mfcc':
  	 draw_oracle(oracle1, 'wave_mfcc1.png', size=(800,300))
	 draw_oracle(oracle2, 'wave_mfcc2.png', size=(800,300))
	 return 1
	elif feat=='centroid':
  	 draw_oracle(oracle1, 'wave_centroid1.png', size=(800,300))
	 draw_oracle(oracle2, 'wave_centroid2.png', size=(800,300))
	 return 1
	elif feat=='chroma':
  	 draw_oracle(oracle1, 'wave_chroma1.png', size=(800,300))
	 draw_oracle(oracle2, 'wave_chroma2.png', size=(800,300))
	 return 1
