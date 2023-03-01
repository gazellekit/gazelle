<div align="center">
  <img 
    height="150px" 
    src=".github/assets/images/fortress.png" 
    alt="Blue Fortress Logo. "
  />
  <h1>How To Contribute</h1>
</div>

## Table of Contents

1. [Tech Stack](#tech-stack)

## Tech Stack

### F#

Many developers reading this may have never come across the F# programming language. It's a shame, because I truly believe that it is a perfect fit for the Structural Engineering domain. At its core F# runs atop the .NET Common Language Runtime (CLR) and compiles down to exactly the same Intermediate Language (IL) as C#. For that reason alone, F# can be used anywhere that C# can. However, the language offers a number of intriguing features that make it a uniquely ideal choice for building safety-critical engineering software; in particular, for server-side APIs where parallelism is desirable and functions are stateless (i.e., no in-memory persistence).

1. [Units of Measure](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/units-of-measure). Compile-time checking of engineering units, built directly into the language, is an incredible feature that I always miss when I programming in any other language. So many errors come about due to mismatched units, especially when implementing Design Codes that often have constants with implicitly defined units. Try it out; you'll never look back.
2. File-Order Matters. F# expects that types and functions have been defined <em>either</em> above in the same file, or in a separate file defined above. Literally. It may seem odd to begin with, but it makes it extremely easy to onboard new developers, as when they open their code editor they can simply read from top to bottom and the program flows accordingly. No more jumping around folders looking for definitions!
3. Functional-First Paradigm. F# is technically multi-paradigm, as is C#. However, they emphasise different styles; F# favours FP over OOP. It takes a little adjustment, but I personally believe that for mathematically-minded Engineers, Functional Programming is actually more aligned with how we think. Moreover, when used for API development, Functional Programming makes tremendous sense: pass in a Request and return a Response. APIs are really just function machines; the kind you studied in school.
4. Immutability By Default. Unless you specifically ask for mutable values, your variables cannot be re-assigned after they have been initialised (you can <em>shadow</em> variables, but I won't touch upon that here). Again, it requires a little change in mindset, but once you grasp the concept, you'll find that you rarely ever reach for mutable values in any other programming language. Your code is simpler to reason about and can be immediately parellelised without any risk of race conditions. No need for locks or mutexes.
5. Pipe-Forward Operators |> allow you to pass the result from the previous function or value as the <em>final</em> argument of the next function's parameter list. This operator alone mitigates multiple sets of parentheses wrapping results from inner function calls. 
6. Pythonic, But Statically-Typed. For those developers coming from a Python background, F# will look very familiar. Indentation matters, and succintness is preferred. However, F# has a feature prevalent in FP languages known as type-inference. Unlike C#, Java etc., you are not required to write every type declaration against a variable/parameter, because the language can infer the majority of types from the context alone. Whilst it is often helpful to type your code regardless, for future readability, it does mean that F# codebases are very neat and concise. Don't be fooled however, F# adopts the Hindley-Milner type system and is actually <em>more</em> type-safe than C#, Java, Go etc. In fact, you'll often hear the mantra in the F# world that: if the code compiles, it probably works. It's a wonderful feeling for those unaccustomed to such strong type systems.
7. ASP.NET Core. Ok, this one isn't strictly about F#, but it does demonstrate that F# can adopt all of the great new features released in .NET!

There is much more to explore, but you get the idea. F# can offer enormous advantages over many other programming languages when used for engineering applications where correctness and performance matter. It is also very approachable and relatively easy to pick up. For these reasons, Fortress is built on F# at its core.
