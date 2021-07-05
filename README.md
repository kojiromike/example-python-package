# Example App for Testing Packaging


## Automatic Releasing

### Pull Requests and Semantic Versioning

This project will try to stick to versions that are compatible with both [PEP 440](https://www.python.org/dev/peps/pep-0440/) and [Semantic Versioning 2.0.0](https://semver.org/) as much as possible. This means...

- ...a *major* version, as in 1.0.2 -> 2.0.0 indicates an incompatible/breaking API change.
- ...a *minor* version, as in 1.3.2 -> 1.4.0 indicates new functionality that maintains backwards compatibility for existing features.
- ...a *patch* version, as in 1.1.2 -> 1.1.3 indicates a bugfix or other improvement with no significant api changes or new features.

Deciding the semantics of a version bump are something best done by humans, and what better place to make that decision than in the pull request itself? Each pull request should have a new version of the project. When a PR is merged, that version information will be used to automatically create a build, release and deploy to pypi.
