namespace Calcpad.Core

type DesignSituation = Persistent | Transient | Accidental 
type LimitState = ULS of DesignSituation | SLS 