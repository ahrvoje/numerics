from math import copysign, floor, pi, sin
from fractions import Fraction


def modpi(x, k=1):
    """
    Precise argument reduction for float x into (-k*pi/2, k*pi/2) interval by exploiting Python Fraction arithmetic.

    :param x: input number
    :param k: multiple of pi factor, can be non-integer value, e.g. fraction
    :returns: coil number (how many times x 'got out' of the target interval), and x mod k*pi conserving the sign
    """

    if k <= 0:
        raise ValueError('modpi(x, k): k should be larger than zero')

    # kpi_2 = k * pi/2
    kpi_2 = Fraction(1, 2) * Fraction(k) * Fraction(98395409743112851784817266986676997509698079238573205159838931333434993172354821263477465823698017440314154046782834235204152982124843487148243755458342086854628729995185902052073391789803316681563605345766763638032469655204215441645210920806592867067725864123381138457374520297213478419852864245886473588103543036413321187259819015604102283393806563,
                                                    31320231676337699569680585584233332126277536636641689113700043556310885271599082660754874336336881557665712387519236631830763012277778509132970811847787840351265010161398078491192208996872168652601371039816615896109116302374314853677592643664025611696588719088575879102271898933000013823033879402787802745580823671382443286151515196625621528139005952)

    fx = Fraction(abs(x))
    modd = (fx + kpi_2) % (2 * kpi_2)
    return copysign(floor(fx / (2 * kpi_2)), x), copysign(float(modd - kpi_2), x)


if __name__ == '__main__':
    print("modpi(pi, 0.5) = %d %.17g" % modpi(pi, 0.5))
    print("mx = %d %.17g" % modpi(15.608571137831408, 0.5))

    print("sin x = %.17g" % sin(15.608571137831408))
    print("sin mx = %.17g" % sin(modpi(15.608571137831408, 0.5)[1]))
