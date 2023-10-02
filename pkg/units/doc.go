// Science and engineering applications typically
// rely on units of measure for dimensional analysis.
// Whilst Go does not have built-in support for
// mathematical units, this package offers a custom
// solution using Types and Generics to enable more
// strongly-typed, robust calculations.

// Where calculations require the user to jump between
// alternate units, it can be valuable to have the
// compiler support warn about mismatched unit
// operations.

// Since Go does not support operator overloading,
// unit conversions and typical operations are
// implemented via Method definitions.
package units
