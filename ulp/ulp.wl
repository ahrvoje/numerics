(* Calculating ULP of double precision x by explicity calculating
 * the value of the least significant bit towards the nearest representable double.
 * Author:Hrvoje Abraham
 * Date:21.12.2015
 * MIT License https://opensource.org/licenses/MIT 
 *)

ulp[x_]:=
  Module[{machEps, machMin, t, l, u},
    {machEps, machMin, t} =
      SetPrecision[{$MachineEpsilon, $MinMachineNumber, Abs[x]}, \[Infinity]];
    If[t <= 2 machMin,
      machEps*machMin,
      l = Log[2, t];
      u = Floor[l];
      If[l > u, 2^(u - 52), 2^(u - 53)]
    ]
  ];
