import numpy as np

import pyximport
pyximport.install(setup_args={"script_args" : ["--verbose"]})
from cython_bbox import bbox_overlaps

def main():
   bbox_overlaps(
    np.ascontiguousarray(np.ones((2, 3), order='C'), dtype=np.float32),
    np.ascontiguousarray(np.ones((2, 3), order='F'), dtype=np.float32)
   )

if __name__ == '__main__':
    main()
