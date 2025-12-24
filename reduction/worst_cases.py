from math import floor
from fractions import Fraction


def worst_case_kpi(b, n, emin, emax, k):
    """
    Implementation of Kahan-McDonald algorithm for calculation of the worst case for argument reduction against k*pi.
    The implementation is adapted Maple version from 'Elementary Functions: Algorithms and Implementation' page 182
    by Jean-Michel Muller.
    https://www.amazon.com/Elementary-Functions-Implementation-Jean-Michel-Muller/dp/0817643729

    :param b: radix
    :param n: full mantissa size, including the hidden bit
    :param emin: minimal scanning exponent
    :param emax: maximal scanning exponent
    :param k: multiple factor in k * pi
    :returns: mantissa and exponent of the worst case, k in fraction format and diff to exact k*pi multiple
    """
    # k * pi
    w = Fraction(k) * Fraction(98395409743112851784817266986676997509698079238573205159838931333434993172354821263477465823698017440314154046782834235204152982124843487148243755458342086854628729995185902052073391789803316681563605345766763638032469655204215441645210920806592867067725864123381138457374520297213478419852864245886473588103543036413321187259819015604102283393806563,
                               31320231676337699569680585584233332126277536636641689113700043556310885271599082660754874336336881557665712387519236631830763012277778509132970811847787840351265010161398078491192208996872168652601371039816615896109116302374314853677592643664025611696588719088575879102271898933000013823033879402787802745580823671382443286151515196625621528139005952)
    epsilonmin = 9999999
    power_bover_c = Fraction(b ** (emin - n)) / w

    for e in range(emin - n + 1, emax - n + 2):
        power_bover_c *= b

        a = floor(power_bover_c)
        r = Fraction(1) / (power_bover_c - a)
        p_last = a
        q_last = 1

        a = floor(r)
        p = p_last * a + 1
        q = a

        while q < b ** n - 1:
            r = Fraction(1) / (r - a)
            a = floor(r)

            new_p = p * a + p_last
            new_q = q * a + q_last

            p_last = p
            q_last = q

            p = new_p
            q = new_q

        epsilon = w * (p_last - q_last * power_bover_c)
        if epsilon < 0 and abs(epsilon) < epsilonmin:
            epsilonmin = abs(epsilon)
            numbermin = q_last
            expmin = e

    return numbermin, expmin, k, float(epsilonmin)


if __name__ == '__main__':
    for k in [1, 2, 3, 4, 5, 6, 7, 8, 10, 50, 1024, 9999, Fraction(3, 2), Fraction(7, 5), Fraction(13, 3), Fraction(93, 8)]:
        print("%d * 2 ** %3d mod %r * pi = %1.17g" % worst_case_kpi(2, 53, 5, 1023, Fraction(1) / k))
        print("%d * 2 ** %3d mod %r * pi = %1.17g" % worst_case_kpi(2, 53, 5, 1023, k))

    # 6381956970095103 * 2 ** 798 mod Fraction(1, 1) * pi = 9.3743318485092553e-19
    # 6381956970095103 * 2 ** 798 mod 1 * pi = 9.3743318485092553e-19
    # 6381956970095103 * 2 ** 797 mod Fraction(1, 2) * pi = 4.6871659242546277e-19
    # 6381956970095103 * 2 ** 799 mod 2 * pi = 1.8748663697018511e-18
    # 8509275960126804 * 2 ** 796 mod Fraction(1, 3) * pi = 3.1247772828364184e-19
    # 5850965514341686 * 2 ** 526 mod 3 * pi = 4.9707325752370692e-18
    # 6381956970095103 * 2 ** 796 mod Fraction(1, 4) * pi = 2.3435829621273138e-19
    # 6381956970095103 * 2 ** 800 mod 4 * pi = 3.7497327394037021e-18
    # 7621563645717625 * 2 **  42 mod Fraction(1, 5) * pi = 4.6271902625519713e-19
    # 6808218460873451 * 2 ** 563 mod 5 * pi = 7.3802180252162538e-18
    # 8509275960126804 * 2 ** 795 mod Fraction(1, 6) * pi = 1.5623886414182092e-19
    # 5850965514341686 * 2 ** 527 mod 6 * pi = 9.9414651504741384e-18
    # 6392553305823052 * 2 ** 159 mod Fraction(1, 7) * pi = 9.3599377963382148e-19
    # 7750232865711478 * 2 ** 436 mod 7 * pi = 1.6967741587615345e-17
    # 6381956970095103 * 2 ** 795 mod Fraction(1, 8) * pi = 1.1717914810636569e-19
    # 6381956970095103 * 2 ** 801 mod 8 * pi = 7.4994654788074042e-18
    # 7621563645717625 * 2 **  41 mod Fraction(1, 10) * pi = 2.3135951312759857e-19
    # 6808218460873451 * 2 ** 564 mod 10 * pi = 1.4760436050432508e-17
    # 7448359865014732 * 2 ** 655 mod Fraction(1, 50) * pi = 3.4451957972883025e-20
    # 5810242949076222 * 2 ** 716 mod 50 * pi = 3.3379844956402054e-16
    # 6381956970095103 * 2 ** 788 mod Fraction(1, 1024) * pi = 9.1546209458098196e-22
    # 6381956970095103 * 2 ** 808 mod 1024 * pi = 9.5993158128734774e-16
    # 5194647583145894 * 2 ** 561 mod Fraction(1, 9999) * pi = 2.3384339348389625e-22
    # 6478635370053307 * 2 ** 359 mod 9999 * pi = 4.0083054984171741e-15
    # 8509275960126804 * 2 ** 797 mod Fraction(2, 3) * pi = 6.2495545656728369e-19
    # 5850965514341686 * 2 ** 525 mod Fraction(3, 2) * pi = 2.4853662876185346e-18
    # 4821861851714696 * 2 ** 636 mod Fraction(5, 7) * pi = 2.2966785575123842e-18
    # 8831695978415509 * 2 ** 153 mod Fraction(7, 5) * pi = 1.9947636833721835e-18
    # 2958935982819588 * 2 ** -47 mod Fraction(3, 13) * pi = 2.8568337073308818e-19
    # 5648695676206402 * 2 ** 888 mod Fraction(13, 3) * pi = 1.248987129188666e-17
    # 6418638918091732 * 2 ** 120 mod Fraction(8, 93) * pi = 2.0391965340569134e-19
    # 5934575450785442 * 2 ** 553 mod Fraction(93, 8) * pi = 8.1175538969241169e-18

