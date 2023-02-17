module Calcpad.Fable

open Calcpad.Core

let message = "Hello, Calcpad!"
let goodbye = "Goodbye, Calcpad!"
let sayHelloFable () = "Hello, Fable!"
let add x y = x + y
let bar = Rebar.getDiameter (UKBarSize H40)
let pow2 (n: float<'T>) : float<'T^2> = n * n
let getDiameter barSize = Rebar.getDiameter (UKBarSize barSize)
