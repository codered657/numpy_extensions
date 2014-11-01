#   NumPy Extensions.
#
#   Description: A library containing useful extension to NumPy.
#
#   Notes: None.
#   
#   Revision History:
#       Steven Okai     10/31/14    1) Initial revision.
# 

import numpy as np

def dot(arrays):
    # See http://en.wikipedia.org/wiki/Matrix_chain_multiplication
    # for a better implementation.

    result = arrays[0];
    for i in xrange(len(arrays)-1):
        result = np.dot(result, arrays[i + 1]);

    return result;
