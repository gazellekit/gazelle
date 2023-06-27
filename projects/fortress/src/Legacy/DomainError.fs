namespace Fortress

type ConcreteError = InvalidAge of message: string

type ReinforcedConcreteError = ConcreteError of ConcreteError
