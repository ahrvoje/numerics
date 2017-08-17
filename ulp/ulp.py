from math import isnan
from struct import pack, unpack
from sys import float_info


def ulp(x):
    """
    Computing ULP of input double precision number x exploiting
    lexicographic ordering property of positive IEEE-754 numbers.

    The implementation correctly handles the special cases:
      - ulp(NaN) = NaN
      - ulp(-Inf) = Inf
      - ulp(Inf) = Inf

    Author: Hrvoje Abraham
    Date: 11.12.2015
    Revisions: 15.08.2017
    MIT License https://opensource.org/licenses/MIT

    :param x: (float) float for which ULP will be calculated
    :returns: (float) ULP of the input float number
    """

    # setting sign bit to 0, e.g. -0.0 becomes 0.0
    t = abs(x)

    # converting double to 64-bit unsigned integer
    ll = unpack('Q', pack('d', t))[0]

    # computing first smaller integer, bigger in a case of ll=0 (t=0)
    near_ll = abs(ll - 1)

    # converting back to double, its value will be nearest to t
    near_t = unpack('d', pack('Q', near_ll))[0]

    # abs takes care of case t=0.0
    return abs(t - near_t)


if __name__ == '__main__':
    assert ulp(-0.0) == 5e-324
    assert ulp(0.0) == 5e-324
    assert ulp(4.9406564584124654e-324) == 5e-324
    assert ulp(4.4501477170144018e-308) == 5e-324
    assert ulp(2.220446049250313e-16) == 2.465190328815662e-32
    assert ulp(1.7976931348623157e+308) == 1.99584030953472e+292
    assert isnan(ulp(float('nan')))
    assert ulp(float('-inf')) == float('inf')
    assert ulp(float('inf')) == float('inf')

    for e in range(-1021, 1023 + 1):
        assert ulp(float(2 ** e)) == float(2 ** (e - 53))
        assert ulp(float(2 ** e) * (1 + float_info.epsilon)) == float(2 ** (e - 52))
