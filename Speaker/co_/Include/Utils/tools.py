import numpy as np
def zero_pad(vector, maxlen):
    """
    this function assumption column is 20. Only check raw!
    """
    vector_shape = vector.shape

    #if vector_shape[1] > maxlen:
     #   vector = vector[:, 0:maxlen]
     #   return vector

    pad_vector = np.zeros([vector_shape[0], maxlen - vector_shape[1]]).astype(np.float32)

    vector = np.hstack([vector, pad_vector])

    return vector