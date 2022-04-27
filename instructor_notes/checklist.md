# Instructors checklist

## Before workshop

- Create org for team if not created
- Create a demo project from template "https://github.com/equinor/appsec-snyk-onboarding" - place on Equinor Playground
- Explore & Test Team Projects (using Snyk CLI)
  - Consider importing into Snyk Org "ISC-Snyk-On-Boarding"
- Send invitation to team lead, and ask to forward to team members

### Good practise

- Fork the repo and add github integration to isc-appsec or own org to check integration
- Run snyk test from cli to check if it has any advantages over github integration
- Check plugin result to see if Snyk Code finds any improvements

## Invitation email
```
Hi,

We're excited to introduce Snyk (https://snyk.io) to your team. Snyk is a tool to find and automatically fix vulnerabilities in code, open source dependencies, containers, and infrastructure as code. We will walk your team through the basics of setting up Snyk, and how to interpret the results.

Preparations:

- Apply for access to Snyk through AccessIT: https://accessit.equinor.com/Search/Search?term=snyk
- After Access in granted, please log in to Snyk with SSO to activate your account: https://app.snyk.io/login/sso

NB: At the moment AccessIT is only available when connected to the corporate network, so if you are at home - VPN or connectIT is required.

All the best,

AppSec team

---

Relevant links :
- AppSec Team - our objectives (Why) - https://iscappsec.app.radix.equinor.com/tasks/objectives-and-activities/
- Community - #AppSec channel @ Slack => https://equinor.slack.com/archives/CMM6FSW5V
- Equinor AppSec info pages - https://equinor.github.io/appsec
```

## During workshop
- Make sure everyone get access to org
- Show vulnerabilities and how to fix them
- Show how to ignore vulns until fix is available
- Show how to resolve auto fixable vulnerabilities

## After workshop
- Register team and onboarding session in [spreadsheet](https://statoilsrm.sharepoint.com/:x:/r/sites/ISCAppSec/Shared%20Documents/General/Snyk%20adoption/Onboarding%20sessions.xlsx?d=w3316d62130554a1ca6b9f7db08ca50d2&csf=1&web=1&e=bsg2fv)
- Fill in workshop experience in [experience document](https://statoilsrm.sharepoint.com/:w:/r/sites/ISCAppSec/Shared%20Documents/General/Snyk%20adoption/Workshop%20experience.docx?d=wf85532313c6a493a9ff1d2030a6e58f0&csf=1&web=1&e=cKaJAr)
- Delete demo project on "github.com/equinor-playground" and the "ISC-Snyk-Onboarding" Snyk Organization
