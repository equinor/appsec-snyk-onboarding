<!-- .slide: data-background-image="./content/images/appsec-icon.svg" data-background-size="7%" data-background-position="right 2% top 2%"-->

# Limitations

---

## Limitations 

- Snyk SCM can only "see" your files outside the context of a built project
  - Docker? Only vulnerabilities in base image are reported
  - Python requirements.txt? Transitive dependencies not scanned
  - C++? We don't even do that (yet)
- Remedy
  - Use lockfile based package managers (e.g. npm, composer)

Note:

- Instructor notes