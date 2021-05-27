#
# Author: Hrvoje Abraham
# e-mail: ahrvoje@gmail.com
#


from operator import itemgetter

from numpy import array
from numpy.linalg import eig


def quaternion_to_matrix(q):
    """
    Conversion of the normalized quaternion to the rotation matrix.

    :param q: normalized quaternion
    :return: corresponding rotation matrix
    """

    w, x, y, z = q

    return array([
        [1 - 2 * (y * y + z * z),     2 * (x * y - w * z),     2 * (x * z + w * y)],
        [    2 * (x * y + w * z), 1 - 2 * (x * x + z * z),     2 * (y * z - w * x)],
        [    2 * (x * z - w * y),     2 * (y * z + w * x), 1 - 2 * (x * x + y * y)],
    ])


def to_nearest_rotation(R):
    """
    Calculation of valid (orthonormal) rotation matrix nearest to some input matrix, based on the adapted Version 3 algorithm from:

    Itzhack Y. Bar-Itzhack.  "New Method for Extracting the Quaternion from a Rotation Matrix",
    Journal of Guidance, Control, and Dynamics, Vol. 23, No. 6 (2000), pp. 1085-1087.
    http://dx.doi.org/10.2514/2.4654

    :param R: 3x3 matrix to be orthonormalized
    :return: orthonormalized matrix 'nearest' to R
    """

    X, Y, Z = R

    K = array([
        [X[0] + Y[1] + Z[2], Z[1] - Y[2],        X[2] - Z[0],        Y[0] - X[1]],
        [Z[1] - Y[2],        X[0] - Y[1] - Z[2], Y[0] + X[1],        Z[0] + X[2]],
        [X[2] - Z[0],        Y[0] + X[1],       -X[0] + Y[1] - Z[2], Z[1] + Y[2]],
        [Y[0] - X[1],        Z[0] + X[2],        Z[1] + Y[2],       -X[0] - Y[1] + Z[2]],
    ])

    # the desired quaternion is eigenvector with the largest eigenvalue
    eigen = eig(K)
    index, value = max(enumerate(eigen[0]), key=itemgetter(1))
    quaternion = eigen[1][:, index]

    return quaternion_to_matrix(quaternion)


if __name__ == '__main__':
    # example of the valid orthonormal rotation matrix, no fix needed
    print(to_nearest_rotation([
         [0.36, 0.48, -0.8],
         [-0.8, 0.6, 0],
         [0.48, 0.64, 0.6],
    ]))

    # fixing a slightly broken rotation matrix
    print(to_nearest_rotation([
        [0.35, 0.48, -0.81],
        [-0.8, 0.6, 0],
        [0.5, 0.64, 0.6],
    ]))
