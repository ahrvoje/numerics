import struct


def ulp(x):
    """
    Computing ULP of input double precision number x exploiting
    lexicographic ordering property of positive IEEE-754 numbers.
    Author: Hrvoje Abraham
    Date:   11.12.2015
    MIT License https://opensource.org/licenses/MIT
    Args:
        x (float) : Float for which ULP will be calculated
    Returns:
        float: ULP of input float number
    """

    # setting sign bit to 0, e.g. -0.0 becomes 0.0
    t = abs(x)

    # converting double to 64-bit unsigned integer
    ll = struct.unpack('Q', struct.pack('d', t))[0]

    # computing first smaller integer, bigger in a case of ll=0 (t=0)
    near_ll = abs(ll - 1)

    # converting back to double, its value will be nearest to t
    near_t = struct.unpack('d', struct.pack('Q', near_ll))[0]

    # abs takes care of case t=0.0
    return abs(t - near_t)
