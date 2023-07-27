namespace Calcpad.Studio.Structures

type DesignSituation =
    | Persistent
    | Transient
    | Accidental

type LimitState =
    | ULS of DesignSituation
    | SLS
