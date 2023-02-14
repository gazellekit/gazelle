namespace Calcpad

type DesignSituation = Persistent | Transient | Accidental 
type LimitState = ULS of DesignSituation | SLS 