from os.path import dirname, abspath, join as pjoin
from matplotlib.image import imread

DIR = dirname(abspath(__file__))


def rotated_lena():
    return imread(pjoin(DIR, 'rotated_lena.png'))


def rotated_parabola():
    return imread(pjoin(DIR, 'rotated_lena.png'))