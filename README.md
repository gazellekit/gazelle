<div align="center">
  <img 
    height="150px" 
    src=".github/assets/images/fortress.png" 
    alt="Blue Fortress Logo. "
  />

  <h1>Fortress</h1>
  <p>Robust & Transparent Structural Design</p>

  [![Production](https://github.com/jamesbayley/Fortress/actions/workflows/publish.yml/badge.svg)](https://github.com/jamesbayley/Fortress/actions/workflows/publish.yml)
  [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md)
</div>

## Table of Contents

1. [Why?](#why)
2. [What?](#what)
3. [Values](#values)
4. [Open-Source](#open-source)
5. [Tech Stack](#tech-stack)
6. [Sponsors](#sponsors)

## Why?

<p align="justify"> 
Engineers accept phenomenal responsibility when dedicating their lives to improve our built environment. Nevertheless, the vast majority of professional engineering software is closed source and proprietary. Engineers can rarely inspect, validate or influence the algorithms used to design our buildings and bridges. I believe this is unfair and must change. Fortress aspires to become the <em>single source of truth</em> for Structural Engineering Design algorithms. 
</p>

## What?

<p align="justify"> 
Fortress is an AEC Developer Platform that offers API-as-a-Service infrastructure for Structural Engineers. The core library hosts an open-source collection of structural design algorithms, which are then exposed via RESTful API endpoints over the network allowing Technologists and Developers working in AEC organisations to integrate these fundamentals checks and calculations into their projects and products, regardless of their specific technology stack. 
</p>

<p align="justify"> 
Web APIs are standardly built upon the standard HTTP/TLS network protocol, which is language-agnostic; whether you're developing desktop apps in C#, Machine Learning scripts in Python, or web apps in JavaScript, you can rely on these battle-tested Design APIs to power your applications and supercharge your workflows. This way, you can focus on developing the bespoke features that matter to your teams and clients: those that drive competitive business value. 
</p>

## Values


Three core values underpin all software design decisions in this project:

1. Transparency, 
2. Robustness, 
3. Simplicity.

<p align="justify"> 
Re-inventing the wheel is costly and it risks introducing errors into calculations. Fortress abstracts you away from the underlying implementation details by exposing developer-friendly entrypoints, whilst still allowing you the freedom to read, verify and validate the calculations for your own peace-of-mind.
</p>

## Open-Source

<p align="justify"> 
A transparent, verifiable AEC Developer Platform designed specifically for Structural Engineers and BIM Professionals is certainly needed. However, no single engineering consultancy is incentivised to build such a platform. Quite simply, this is the platform I wish had existed when I started out as an AEC Developer. 
</p>

<p align="justify"> 
I genuinely understand how overwhelming it can be to explore the various rabbit-holes that exist when transitioning into Software Engineering. Tutorials and API documentation often presume a programming background, which for many in AEC is simply not the case. My hope is that by (1) building this project in the open, (2) allowing any interested party to study the codebase, and (3) providing rich, intuitive documentation to ease onboarding, Engineers interested in developing new applications, scripts, tools and workflows can learn and grow in confidence.
</p>

<p align="justify"> 
For the AEC development ecosystem to thrive, I believe that it falls upon <em>us</em> in the open-source community to innovate, collaborate and share our combined experiences and intellects to build the infrastructure we deserve.
</p>

## Tech Stack

### F#

<p align="justify">
Many developers reading this may have never come across the F# programming language. It's a shame, because I truly believe that it is a perfect fit for the Structural Engineering domain. At its core F# runs atop the .NET Common Language Runtime (CLR) and compiles down to exactly the same Intermediate Language (IL) as C#. For that reason alone, F# can be used anywhere that C# can. However, the language offers a number of intriguing features that make it a uniquely ideal choice for building safety-critical engineering software; in particular, for server-side APIs where parallelism is desirable and functions are stateless (i.e., no in-memory persistence).
</p>

1. **[Units of Measure](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/units-of-measure)**. Compile-time checking of engineering units, built directly into the language, is an incredible feature that I always miss when I programming in any other language. So many errors come about due to mismatched units, especially when implementing Design Codes that often have constants with implicitly defined units. Try it out; you'll never look back.
2. **File-Order Matters**. F# expects that types and functions have been defined <em>either</em> above in the same file, or in a separate file defined above. Literally. It may seem odd to begin with, but it makes it extremely easy to onboard new developers, as when they open their code editor they can simply read from top to bottom and the program flows accordingly. No more jumping around folders looking for definitions!
3. **Functional-First Paradigm**. F# is technically multi-paradigm, as is C#. However, they emphasise different styles; F# favours FP over OOP. It takes a little adjustment, but I personally believe that for mathematically-minded Engineers, Functional Programming is actually more aligned with how we think. Moreover, when used for API development, Functional Programming makes tremendous sense: pass in a Request and return a Response. APIs are really just function machines; the kind you studied in school.
4. **Immutability By Default**. Unless you specifically ask for mutable values, your variables cannot be re-assigned after they have been initialised (you can <em>shadow</em> variables, but I won't touch upon that here). Again, it requires a little change in mindset, but once you grasp the concept, you'll find that you rarely ever reach for mutable values in any other programming language. Your code is simpler to reason about and can be immediately parellelised without any risk of race conditions. No need for locks or mutexes.
5. **Pipe-Forward Operators** |> allow you to pass the result from the previous function or value as the <em>final</em> argument of the next function's parameter list. This operator alone mitigates multiple sets of parentheses wrapping results from inner function calls. 
6. **Pythonic, But Statically-Typed.** For those developers coming from a Python background, F# will look very familiar. Indentation matters, and succintness is preferred. However, F# has a feature prevalent in FP languages known as type-inference. Unlike C#, Java etc., you are not required to write every type declaration against a variable/parameter, because the language can infer the majority of types from the context alone. Whilst it is often helpful to type your code regardless, for future readability, it does mean that F# codebases are very neat and concise. Don't be fooled however, F# adopts the Hindley-Milner type system and is actually <em>more</em> type-safe than C#, Java, Go etc. In fact, you'll often hear the mantra in the F# world that: if the code compiles, it probably works. It's a wonderful feeling for those unaccustomed to such strong type systems.

<p align="justify">
There is much more to explore, but you get the idea. F# can offer enormous advantages over many other programming languages when used for engineering applications where correctness and performance matter. It is also very approachable and relatively easy to pick up. For these reasons, Fortress is built on F# at its core.
</p>

## Sponsors

<p align="justify"> 
I work on this project entirely in my spare time, because I believe in a more <em>open</em> AEC industry. Nevertheless, server costs and admin fees are real! I welcome all financial contributions that can help to keep the vision alive. Please check out my <strong>GitHub Sponsors</strong> link if you'd like to donate.
</p>

Thank You.
