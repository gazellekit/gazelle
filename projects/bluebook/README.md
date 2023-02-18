# BlueBook

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md)

## Contents

- [Acknowledgements](#acknowledgements)
  - [Errata](#errata)
- [Overview](#overview)
- [Scope](#scope)
- [Open Source](#open-source)
- [Getting Started](#getting-started)
  - [JavaScript](#javascript)
- [API Docs](#api-docs)
  - [API v1](#api-v1)
    - [Section Properties](#section-properties)

## Acknowledgements

This free and open source product would not be possible without the great  work completed by Steel for Life. All steel section data made available through this service has been sourced directly from https://www.steelforlifebluebook.co.uk.   

### Errata

If errors or omissions are found in the original datasets, please contact Steel for Life directly.

## Overview

As our Civil & Structural Engineers continue to adopt and/or build modern workflows to help them solve their most pressing engineering challenges, the availability of key data in useful formats becomes increasingly important. A significant portion of relevant design data is captured within Excel spreadsheets, books, tables and figures. For software developers, this is problematic. Mapping the data from one format to another can be a source of error, especially if the data must be transformed manually. Moreover, the task of transforming data is time-consuming and often frustrating.

This project looks to solve the challenge of data availability for UK steel sections, by providing the Steel for Life 'Blue Book' data as a service. The various Excel sheets available on the Steel for Life website have been converted to JSON file formats and uploaded, so that developers can simply query the section data through a clean, convenient and consistent web API. 

This service is provided freely to all developers and hopes to ease the on-boarding process for new developers looking to build innovative, automated processes for any platform. The beauty of offering a web-first API is that the HTTP protocol is programming language **agnostic**, so developers can query an identical dataset using JavaScript, Python, C#, F#, Go, PowerShell, Bash etc. To accelerate innovation in the Architecture, Engineering & Construction (AEC) arena, it is important that the services we provide are portable and usable across ecosystems.  

## Scope

At the current time, as a proof-of-concept, the various Steel Section datasets are provided as static JSON files that can be queried via HTTP `GET` requests and deserialized by the caller. Future iterations of this project may see a more sophisticated API implemented, allowing for more complex queries, filters etc. 

## Open Source

The sourced data was made freely available by Steel for Life. In the same spirit, the contents of this repository are also made available through the MIT License to anyone interested. Transparency is vital in AEC, as the projects being developed rely on accurate, reliable data to ensure the safety of all designed structures. 

## Getting Started

### JavaScript

Perhaps the easiest way to get started with the API is to simply fire up a *developer console* in your preferred browser and make a standard JavaScript `fetch` request. 

**Note:** To find how to launch your developer console, please consult the relevant documentation for your browser.

Within your console, run the following two commands:

```javascript
let res = await fetch('https://jamesbayley.github.io/cdn/v1/section-properties/ub.json')
let sections = await res.json();
```

Your `sections` variable should now contain the full selection of available UB sections and can be queried and manipulated accordingly.

```javascript
// Get the full set of UB section designations.
const designations = Object.keys(sections);
console.log(designations)

// Get the total number of unique sections.
const count = designations.length;
console.log(`Number of unique UB sections: ${count}.`);
```

## API Docs

### API v1

The following API `GET` endpoints are available. All endpoints presume the same base URL address of: `https://jamesbayley.github.io/cdn/v1`, so for clarity this URL is shortened to `root` in all examples.

#### Section Properties

- Universal Beams: `root/section-properties/ub.json`
- Universal Columns: `root/section-properties/uc.json`
- Parallel-Flange Channel: `root/section-properties/pfc.json`
- Universal Bearing Pile: `root/section-properties/ubp.json`
- Equal-L: `root/section-properties/equal-l.json`
- Unequal-L: `root/section-properties/unequal-l.json`
- T Split From Universal Beam: `root/section-properties/t-split-from-ub.json`
- T Split from Universal Column: `root/section-properties/t-split-from-uc.json`
- Hot-Formed Circular Hollow Section: `root/section-properties/hf-chs.json`
- Hot-Formed Elliptical Hollow Section: `root/section-properties/hf-ehs.json`
- Hot-Formed Rectangular Hollow Section: `root/section-properties/hf-rhs.json`
- Hot-Formed Square Hollow Section: `root/section-properties/hf-shs.json`
- Cold-Formed Circular Hollow Section: `root/section-properties/cf-chs.json`
- Cold-Formed Rectangular Hollow Section: `root/section-properties/cf-rhs.json`
- Cold-Formed Square Hollow Section: `root/section-properties/cf-shs.json`
