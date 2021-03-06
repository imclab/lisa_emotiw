"""
This script makes a dataset of 32x32 contrast normalized, approximately
whitened (aligned) EmotiW face images.

"""

from pylearn2.utils import serial
from pylearn2.datasets import preprocessing
from pylearn2.utils import string_utils
from emotiw.gdesjardins.cf3rbm import data

data_dir = string_utils.preprocess('/data/lisatmp/desjagui/data/emotiwfaces')

print 'Loading EmotiwFaces valid dataset...'
valid = data.EmotiwFaces(which_set='Val', one_hot=True, gcn=True)

print "Preparing output directory..."
output_dir = '%s/gcn_whitened' % data_dir
serial.mkdir( output_dir )
README = open(output_dir + '/README','w')

README.write("""
        Generated with emotiw.gdesjardins.make_emotiw_faces_gcn_whitened.py
        """)
README.close()

print "Learning the preprocessor and preprocessing the unsupervised valid data..."
preprocessor = preprocessing.ZCA()
valid.apply_preprocessor(preprocessor = preprocessor, can_fit = True)

print 'Saving the unsupervised data'
valid.use_design_loc(output_dir+'/valid.npy')
serial.save(output_dir + '/valid.pkl', valid)

"""
print "Loading the test data"
test = CIFAR10(which_set = 'test', gcn = 55.)

print "Preprocessing the test data"
test.apply_preprocessor(preprocessor = preprocessor, can_fit = False)

print "Saving the test data"
test.use_design_loc(output_dir+'/test.npy')
serial.save(output_dir+'/test.pkl', test)
"""

serial.save(output_dir + '/preprocessor.pkl',preprocessor)

