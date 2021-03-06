import os
import inspect

import tensorflow as tf

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


PERMITTED_VIDEO_EXTENSIONS = ['mp4', 'avi']
MAX_FILE_SIZE = 50000000
NUMBERS_OF_FRAMES_TO_SHOW = 10
TMP_DIR = 'tmp/'
GPU = True

FEATURE_BATCH_SIZE = 32
DEFAULT_FRAMES_SAMPLING_MODE = 0
DEFAULT_RL_MODE = 0
DEFAULT_IMAGE_ASSESSMENT_MODE = 0

DEFAULT_STYLE_TRANSFER_MODE = 0
COMIX_GAN_MODEL_PATH = os.path.join(BASE_DIR, 'ComixGAN', 'pretrained_models', 'generator_model.h5')
MAX_FRAME_SIZE_FOR_STYLE_TRANSFER = 600

NIMA_MODEL_PATH = os.path.join(BASE_DIR, 'neural_image_assessment', 'pretrained_model', 'nima_model.h5')

CAFFE_ROOT = 'caffe_git/'


config_dict = {name: value for (name, value) in locals().items() if not name.startswith('_')}

# IMPORTANT: fix issues in colab
# See https://www.tensorflow.org/tutorials/using_gpu#allowing_gpu_memory_growth
config = tf.ConfigProto()
config.gpu_options.allow_growth = True


with tf.Session(config=config) as sess:
  sess.run(tf.global_variables_initializer())

class SettingObject(object):
    def __init__(self):
        super(SettingObject, self).__init__()

settings = SettingObject()

for key, value in config_dict.items():
    if not inspect.ismodule(value):
        if not isinstance(value, list):
            os.environ[key] = str(value)
        setattr(settings, key, value)
        print("Setting: {}={}".format(key, value))
