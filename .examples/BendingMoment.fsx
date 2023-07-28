open FSharp.Data.UnitSystems.SI.UnitSymbols

// 0. Custom units.
[<Measure>]
type mm

// 1. Partial safety factors.
let γ_c = 1.5
let γ_s = 1.15

// 2. Factors to account for long-term effects on concrete.
let α_cc = 0.85
let α_ct = 1.0

// 3. Selected concrete strength.
let fck = 25.0<N / mm^2>

// 4. Ultimate concrete design stress.
let fcd = α_cc * fck / 1.5

// 5. Concrete strain limits.
let εc2 = 0.002
let εcu2 = 0.0035

// 6. Rebar steel strength.
let fyk = 500.0<N / mm^2>

// 7. Rebar steel modulus.
let Es = 200_000.0<N / mm^2>

// 8. Rebar design yield strain.
let εy = fyk / (γ_s * Es)

// 9. Equation to calculate neutral axis, x.
let x εst εcu2 (d: float<mm>) = d / (1.0 + (εst / εcu2))
let x_partial = x 0.00217 0.0035

(* EC2 limits depth of N.A. to 0.45d.
   The UK annex can change this, but 
   0.45d is a sensible start point. *)

// 10. Stress block reduced to 0.8x depth.
let s d = (x_partial d) * 0.8

// 11. Calculate concrete compressive force.
let Fcc d (b: float<mm>) = fcd * (s d) * b

// 12. Calculate moment.
let z d = d - (s d / 2.0)
let M d b = (Fcc d b) * (z d)

// 13. Calculate area of steel.
let As d b = (M d b) / (0.87 * fyk * (z d))

M 440.0<mm> 260.0<mm> / 10E6
As 440.0<mm> 260.0<mm>


(*
  Rectangular section in bending with compression 
  reinforcement at the ultimate limit state.
*)

// Assumes zero moment redistribution.

let x_limit = 0.45
let z_bal (d: float<mm>) = d - (0.8 * x_limit * d) / 2.0
