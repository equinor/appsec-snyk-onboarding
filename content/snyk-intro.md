<!-- .slide: data-background-image="./content/images/appsec-icon.svg" data-background-size="7%" data-background-position="right 2% top 2%"-->

# Snyk Intro

---

## Snyk Products

* [Snyk Open Source](https://docs.snyk.io/products/snyk-open-source) (OSS Libraries and Licenses)
* [Snyk Container](https://docs.snyk.io/products/snyk-container)
* [Snyk Infrastructure As Code](https://docs.snyk.io/products/snyk-infrastructure-as-code)*
* [Snyk Code](https://docs.snyk.io/products/snyk-code)* (SAST)

\* Equinor has not purchased licenses, we have access through evaluation mode <!-- .element: style="font-size:0.5em"-->

---

## Snyk in the SDLC

<img src="./content/images/Snyk-SDLC.png">

[Snyk Docs](https://docs.snyk.io/)
---

## Getting started

- A good starting point will be to focusing on the Snyk GitHub integration (the SCM Integration) <!-- .element: style="font-size:0.8em"-->

- Some capabilities <!-- .element: style="font-size:0.8em"-->
  - Vulnerability discovery for many [programming languages](https://docs.snyk.io/products/snyk-open-source/language-and-package-manager-support), container and infrastructure as code <!-- .element: style="font-size:0.8em"-->
  - Triaging of vulnerabilities (inspect, prioritize, fix-manage)
  - Detailed Explanation of vulnerabilities <!-- .element: style="font-size:0.8em"-->
  - Advice on upgrade <!-- .element: style="font-size:0.8em"-->
  - Manual and automated pull requests for fixes <!-- .element: style="font-size:0.8em"-->
  - Reportings and statistics <!-- .element: style="font-size:0.8em"-->

---

## Evaluating and prioritizing vulnerabilities

Some advice on how to evaluate and handle dependency upgrades!

- Remove unused dependencies <!-- .element: style="font-size:0.8em"-->
- Differentiate between development and production dependencies  <!-- .element: style="font-size:0.8em"-->
- Spend the energy on upgrading instead of evaluating if this hits you</br>(Assumes support by automated test suite) <!-- .element: style="font-size:0.8em"-->
- Outdated dependencies are technical debt <!-- .element: style="font-size:0.8em"-->
- [Prioritizing and fixing issues](https://docs.snyk.io/features/fixing-and-prioritizing-issues) and [Issue Management](https://docs.snyk.io/features/fixing-and-prioritizing-issues/issue-management)

> "If your automated tests are not good enough<br>
> to make it acceptable to deploy updated components,<br>
> then you have a serious security problem" <!-- .element: style="font-size:0.6em"-->

<div>Linux Foundation Secure Software Development course <!-- .element: style="font-size:0.4em;"--> </div>

