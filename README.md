# Open Source vulnerability scanning with Snyk

> Onboard your DevOps team on using Snyk.

Training material for basic introduction to use Snyk for scanning open source libraries and it's dependencies for vulnerabilities.

The slides are created with [Reveal.js](https://revealjs.com/), and automatically deployed to [Omnia Radix](https://radix.equinor.com) on new commits to the `main` branch.

## Updating content

The contents of the onboarding slides are contained in a set of markdown file in the [`content`](content) folder. The markdown files are referenced from the [`index.html`](index.html) file.

## Development environment

### Live Server

- To host the files, use the "Live Server" plugin to VSCode. (It's included in recommend extensions the workspace)
- Press to "Go Live" icon toolbar bottom right, and the port 5500 is forwarded to your client.

### Docker container

- `docker build -t "ossnyk" .`
- `docker run -d --name ossnyk_web -p 8080:8080 ossnyk`
- User your browser to visit localhost:8080 (if builded locally) - or open the Ports tab in in codespaces, and visit your private link.

### SRI - Integrity check for own provided source files

How to provide a hash for the .js and .css file provided in the source.

- `cat ./content/js/app.js | openssl dgst -sha512 -binary | openssl base64 -A`
- `cat ./content/css/equinor.css | openssl dgst -sha512 -binary | openssl base64 -A`
