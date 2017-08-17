/* Calculating ULP of double precision x by explicity calculating
 * the value of the least significant bit towards the nearest representable double.
 * Author: Hrvoje Abraham
 * Date: 12.12.2015
 * Revisions: 15.08.2017
 * MIT License https://opensource.org/licenses/MIT 
 */

#include <math.h>
#include <float.h>


double ulp(double x)
{
    if (isnan(x)) {
        return NAN;
    }

    if (isinf(x)) {
        return INFINITY;
    }

    double t = fabs(x), l, u;

    if (t <= 2 * DBL_MIN) {
        return DBL_EPSILON * DBL_MIN;
    }

    l = log2(t);
    u = floor(l);

    if (u > 1023) {
        u = 1023.;
    }

    if (t > pow(2.0, u)) {
        return pow(2.0, u - 52);
    } else {
        return pow(2.0, u - 53);
    }
}
