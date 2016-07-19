import operator

from numpy import array
from numpy.linalg import eig


def quaternion_to_matrix(q):
    """
    Conversion of the normalized quaternion to the rotation matrix.

    :param q: normalized quaternion
    :return: corresponding rotation matrix
    """

    w = q[0]
    x = q[1]
    y = q[2]
    z = q[3]

    return array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)],
        [2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)],
        [2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)]
    ])


def to_nearest_rotation(R):
    """
    Calculation of the valid (orthonormal) rotation matrix nearest to the input matrix, based on the adapted Version 3 algorithm from:

    Itzhack Y. Bar-Itzhack.  "New Method for Extracting the Quaternion from a Rotation Matrix",
    Journal of Guidance, Control, and Dynamics, Vol. 23, No. 6 (2000), pp. 1085-1087.
    http://dx.doi.org/10.2514/2.4654

    :param R: matrix needed to be reorthogonalized
    :return: rotation matrix nearest to R
    """

    K = array([
        [R[0][0] + R[1][1] + R[2][2], R[2][1] - R[1][2], R[0][2] - R[2][0], R[1][0] - R[0][1]],
        [R[2][1] - R[1][2], R[0][0] - R[1][1] - R[2][2], R[1][0] + R[0][1], R[2][0] + R[0][2]],
        [R[0][2] - R[2][0], R[1][0] + R[0][1], R[1][1] - R[0][0] - R[2][2], R[2][1] + R[1][2]],
        [R[1][0] - R[0][1], R[2][0] + R[0][2], R[2][1] + R[1][2], R[2][2] - R[0][0] - R[1][1]]
    ])

    # get the eigenvector with the largest eigenvalue
    eigen = eig(K)
    index, value = max(enumerate(eigen[0]), key=operator.itemgetter(1))
    quaternion = eigen[1][:, index]

    return quaternion_to_matrix(quaternion)


# example of the valid rotation matrix:
#
# [
#     [0.36, 0.48, -0.8],
#     [-0.8, 0.6, 0],
#     [0.48, 0.64, 0.6]
# ]
#
#
# fix slightly broken rotation matrix:
#
# print(to_nearest_rotation([
#     [0.35, 0.48, -0.81],
#     [-0.8, 0.6, 0],
#     [0.5, 0.64, 0.6]
# ]))
