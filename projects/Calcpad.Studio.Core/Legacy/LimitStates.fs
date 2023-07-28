namespace Calcpad.Studio.Core.Structures

type DesignSituation =
    | Persistent
    | Transient
    | Accidental

type LimitState =
    | ULS of DesignSituation
    | SLS
