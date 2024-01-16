import sys
import os

sys.path[0] = os.path.join(sys.path[0], 'FaceCropAnime')

from face_crop import FaceCrop

__all__= ['FaceCropAnime', 'FaceCrop']