namespace Calcpad

type ConcreteError = 
    | InvalidAge of message : string

type ReinforcedConcreteError = 
    | ConcreteError of ConcreteError