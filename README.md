<div align="center">
  <img src="assets/images/gazelle-250x250-rounded.png" height="175px" width="175px" />
  <h1>Gazelle</h1>
  <p>A fast, cross-platform engine for structural analysis & design.</p>

  [![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/gazellekit/gazelle)
  [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](https://github.com/gazellekit/gazelle/blob/main/CODE_OF_CONDUCT.md)
  [![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-00add8)](https://choosealicense.com/licenses/agpl-3.0/)
  
  [![Staging](https://github.com/gazellekit/gazelle/actions/workflows/staging.yml/badge.svg)](https://github.com/gazellekit/gazelle/actions/workflows/staging.yml)
  [![Production](https://github.com/gazellekit/gazelle/actions/workflows/production.yml/badge.svg)](https://github.com/gazellekit/gazelle/actions/workflows/production.yml)
  
  [![.NET](https://img.shields.io/badge/.NET-8.0-8a2be2)](https://dotnet.microsoft.com)
</div>

## Table of Contents

- [Overview](#overview)
- [Supported Platforms](#supported-platforms)
- [Documentation](#documentation)
- [Why F#?](#why-f)
- [Open Source](#open-source)
- [Contributing](#contributing)
- [Community](#community)
- [Errata](#errata)

## Overview

Gazelle aspires to: 

1. Underpin academic research.
2. Support Structural Engineering education.
3. Accelerate AEC software innovation.
4. Become an authoritative *source of truth*.
5. Offer first-class support for [Polyglot Notebooks](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.dotnet-interactive-vscode).
6. Demonstrate that F# is ideal for Civil Engineers.

## Supported Platforms

Gazelle runs everywhere that [.NET](https://dotnet.microsoft.com/en-us/learn/dotnet/what-is-dotnet) runs!

- Windows, 
- Linux, 
- MacOS, 
- iOS, 
- Android, 
- IoT, 
- WASM
- And more...

In fact, the project is actively developed on Ubuntu Linux running inside of [GitHub Codespaces](https://github.com/features/codespaces).

## Documentation

Please visit [docs.gazelle.sh](https://docs.gazelle.sh) to learn more.

## Why F#?

<p align="justify">
  Many programming languages were considered before committing to <a href="https://dotnet.microsoft.com/en-us/languages/fsharp" target="_blank">F#</a>. Whilst the community of F# developers is smaller than for C#, Python, JavaScript, Rust etc. the language offers a number of distinct features that make it ideal for Civil & Structural Engineering software.
</p>

1. **Runs on .NET:** this makes it fast, extremely portable and fully interoperable with C#.
2. **Polyglot Notebooks:** F# has great support for Polyglot Notebooks in VSCode. Check out our [examples](./examples/). 
3. **Functional-first:** the FP paradigm allows for succinct, maintainable, elegant solutions.
4. **Units-of-Measure:** mathematical unit systems (e.g., Metres, Newtons) can be [encoded and checked at compile time](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/units-of-measure)!
5. **Great for Cloud:** REST API services are stateless by definition; the Functional Programming paradigm mirrors this nicely.
6. **ML type system:** it's very strict and if your code *builds* then it probably runs too!

For some, the choice of F# will be an odd one. However, we believe it's perfect for solving our domain problems. We also really enjoy working with the language and want to see it more widely adopted.

> One who takes the road less traveled earns the rewards most missed. - Matshona Dhliwayo

## Open Source

<p align="justify">
  Engineers accept phenomenal responsibility when dedicating their lives to improve our built environment. However, the vast majority of professional engineering software is, regrettably, closed source and proprietary. This is unfair and must change. Engineers should be offered the respect and freedom to inspect, validate and influence the algorithms used to design our buildings and bridges. 
</p>

<p align="justify">
  Gazelle is proudly open-source.
</p>

## Contributing

<p align="justify">
  For those interested in helping to build <a href="https://github.com/gazellekit/gazelle" target="_blank">Gazelle</a>, please ⭐️ and 'watch' this repository so that you can track its progress in real-time.
</p>

<p align="justify">
  We are always on the lookout for new contributors to help: 
</p>

- Propose design improvements,
- Develop and maintain the engine, 
- Enhance our testing and performance suite,
- Verify algorithmic correctness.

## Community

<p align="justify">
  For those keen to build upon the core Gazelle engine and extend its reach and capabilities, here are a few suggested project ideas: 
</p>

- Organise local meetups to discuss how Gazelle could enhance your existing workflows,
- Plan conferences and community engagement events to broaden Gazelle's adoption,
- Install the Gazelle NuGet package and run it inside Polyglot Notebooks.

```fsharp
// Polyglot Notebooks sample.

// Install package from NuGet Package Gallery.
#r "nuget: Gazelle" 


open Gazelle.Units

let moment = 2.5<kNm>
let force = 5.0<kN>

printfn $"Moment / Force = %.2f{moment / force} m" // => 0.50 m
```

## Errata

<p align="justify">
  Gazelle aspires to achieve the highest standards of professional rigour. We consider Structural Analysis & Design software to be safety critical. We strive to ensure stability, robustness and correctness throughout the source code, test suite and companion documentation. Nevertheless, our team are human and mistakes <em>are</em> possible. 
</p>

<p align="justify">
  We recommend that all users carefully review the code, tests and documentation. Please submit error reports and suggestions for improvement via <a href="https://github.com/gazellekit/gazelle/issues" target="_blank">GitHub Issues</a>. For anyone who would like to attempt a fix or improvement, we would encourage you to review our <a href="#contributing">Contributing</a> guidance and submit a Pull Request.
</p>
