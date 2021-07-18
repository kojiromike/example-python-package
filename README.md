# Example App for Testing Packaging


## Automatic Releasing

### Conventional Pull Requests -> Semantic Versioning

This project will try to stick to versions that are compatible with both [PEP 440](https://www.python.org/dev/peps/pep-0440/) and [Semantic Versioning 2.0.0](https://semver.org/) as much as possible. This means...

- ...a *major* version, as in 1.0.2 -> 2.0.0 indicates an incompatible/breaking API change.
- ...a *minor* version, as in 1.3.2 -> 1.4.0 indicates new functionality that maintains backwards compatibility for existing features.
- ...a *patch* version, as in 1.1.2 -> 1.1.3 indicates a bugfix or other improvement with no significant api changes or new features.

The pull request title and body become the commit message when the pull request is squashed. The title and boy must follow [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/). [Commitizen](https://commitizen-tools.github.io/commitizen/) will ensure that. If a conventional commit is...

- ... starts with `feat!`, or contains `BREAKING` in the footer, then the version bump will be *major*.
- ... starts with `feat` and does not contain `BREAKING` in the footer, then the version bump will be *minor*.
- ... starts with `fix`, `refactor`, `perf` or `build`, then the version bump will be *patch*.
- ... starts with `docs`, `style`, `test` or `ci`, then no automatic version bump will be done.


#### How does it work?

When a pull request is created, GitHub Actions will run on it. The workflow will

1. Check if the pull request title is conventional.
2. Determine what the new version should be.
3. Suggest corrections to the version of the application in the pull request, if necessary.
