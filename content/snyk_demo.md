<!-- .slide: data-background-image="./content/images/appsec-icon.svg" data-background-size="7%" data-background-position="right 2% top 2%"-->
<!-- markdownlint-disable MD033 -->

# Snyk - Demo

---

## Getting Access

* Apply for Snyk in AccessIT
  * Optional : Ask _**@appsecteam**_ in Slack channel _[#AppSec](https://equinor.slack.com/archives/CMM6FSW5V)_ to create a Snyk organization for your team
* Login to [app.snyk.io](https://app.snyk.io/) using sso
* After your first time sign in, you will be able to list organizations available at the Equinor Group overview (top level). If you see a relevant org to join, request one of the listed _**org admins**_ to add you to the org.

---

## Demo (1/2)

* Logging in to [app.snyk.io](https://app.snyk.io/)
* Select "Organization" (Equinor-Test/ISC-SNYK-Onboarding)
  * Dashboard, Reports, Projects, Integrations, Members
  * Organization Settings
  * User Settings
* Configure Github Integration (investigate)
* Import demo project (Equinor-Playground/xxx-Snyk-Onboard-Demo-Project)
  * Integrations -> Github
  * View import log
  </br>👇
  
---

## Demo (2/2)

* Explore Projects (NodeJS, Python, Dockerfile, Code)
  * Issues (Filters, Scoring, Details Info, "Ignore Options", Learn)
  * Open a Fix PR, explore the PR
  * Explore "projects setting" for Dockerfile, Package.Json
* Explore Reports Section
  * Selector (Projects, Filters)
  * Summary, Issues, Dependencies, Licenses
* Explore Dashboard
* Optional: Explore CLI and/or VSCode Plugin

---

## Evaluating and prioritizing vulnerabilities

Some advice on how to evaluate and handle dependency upgrades!

* Remove unused dependencies <!-- .element: style="font-size:0.8em"-->
* Differentiate between development and production dependencies  <!-- .element: style="font-size:0.8em"-->
* Spend the energy on upgrading instead of evaluating if this hits you</br>(Assumes support by automated test suite) <!-- .element: style="font-size:0.8em"-->
* Outdated dependencies are technical debt <!-- .element: style="font-size:0.8em"-->
* [Prioritizing and fixing issues](https://docs.snyk.io/features/fixing-and-prioritizing-issues) and [Issue Management](https://docs.snyk.io/features/fixing-and-prioritizing-issues/issue-management)

> "If your automated tests are not good enough<br>
> to make it acceptable to deploy updated components,<br>
> then you have a serious security problem" <!-- .element: style="font-size:0.6em"-->

<div>Linux Foundation Secure Software Development course <!-- .element: style="font-size:0.4em;"--> </div>
