# pyrig-webapp

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-webapp/health-check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-webapp/actions/workflows/health-check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-webapp/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-webapp/actions/workflows/release.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-webapp/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-webapp)
[![SecurityPracticesChecker](https://api.scorecard.dev/projects/github.com/Winipedia/pyrig-webapp/badge)](https://scorecard.dev/viewer/?uri=github.com/Winipedia/pyrig-webapp)
[![Best Practices](https://www.bestpractices.dev/en/projects?as=badge&url=https%3A%2F%2Fgithub.com%2FWinipedia%2Fpyrig-webapp)](https://www.bestpractices.dev/en/projects?as=entry&url=https%3A%2F%2Fgithub.com%2FWinipedia%2Fpyrig-webapp)
[![Baseline](https://www.bestpractices.dev/en/projects?as=baseline&url=https%3A%2F%2Fgithub.com%2FWinipedia%2Fpyrig-webapp)](https://www.bestpractices.dev/en/projects?as=entry&url=https%3A%2F%2Fgithub.com%2FWinipedia%2Fpyrig-webapp)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://prek.j178.dev/reference/built-in-hooks/#fix-byte-order-marker)
[![CICDLinter](https://img.shields.io/badge/CI/CD-actionlint-blue)](https://github.com/rhysd/actionlint)
[![CICDSecurityChecker](https://img.shields.io/badge/%F0%9F%8C%88-zizmor-white?labelColor=white)](https://github.com/zizmorcore/zizmor)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-case-conflict)
[![CodeAnalyzer](https://img.shields.io/badge/code--analysis-CodeQL-181717?logo=github)](https://codeql.github.com/docs/)
[![DeadCodeChecker](https://img.shields.io/badge/dead--code-vulture-blue)](https://github.com/jendrikseipp/vulture)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![EndOfFileFormatter](https://img.shields.io/badge/EOF-end--of--file--fixer-orange)](https://prek.j178.dev/reference/built-in-hooks/#end-of-file-fixer)
[![EndOfLineFormatter](https://img.shields.io/badge/EOL-mixed--line--ending-orange)](https://prek.j178.dev/reference/built-in-hooks/#mixed-line-ending)
[![FuzzTester](https://img.shields.io/badge/fuzzing-hypothesis-blue)](https://hypothesis.readthedocs.io/en/latest/)
[![JSONFormatter](https://img.shields.io/badge/JSON-pretty--format--json-orange)](https://prek.j178.dev/reference/built-in-hooks/#pretty-format-json)
[![JSONLinter](https://img.shields.io/badge/JSON-check--json-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-json)
[![LargeFileChecker](https://img.shields.io/badge/large--files-check--added--large--files-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-added-large-files)
[![MarkdownLinter](https://img.shields.io/badge/Markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![MergeConflictChecker](https://img.shields.io/badge/merge--conflict-check--merge--conflict-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-merge-conflict)
[![ModuleTestNamingChecker](https://img.shields.io/badge/test--naming-name--tests--test-blue)](https://github.com/pre-commit/pre-commit-hooks#name-tests-test)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![PythonOrderLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Winipedia/pyorder/main/docs/assets/badge.json)](https://github.com/Winipedia/pyorder)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![ShellFormatter](https://img.shields.io/badge/shell-shfmt-orange)](https://github.com/mvdan/sh)
[![ShellLinter](https://img.shields.io/badge/shell-shellcheck-blue)](https://github.com/koalaman/shellcheck)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TOMLLinter](https://img.shields.io/badge/TOML-tombi-blueviolet)](https://github.com/tombi-toml/tombi)
[![TrailingWhitespaceFormatter](https://img.shields.io/badge/whitespace-trailing--whitespace-orange)](https://prek.j178.dev/reference/built-in-hooks/#trailing-whitespace)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![XMLLinter](https://img.shields.io/badge/XML-check--xml-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-xml)
[![YAMLLinter](https://img.shields.io/badge/YAML-ryl-red)](https://github.com/owenlamont/ryl)
<!-- tooling -->
[![ContainerEngine](https://img.shields.io/badge/Container-Podman-A23CD6?logo=podman&logoColor=grey&colorA=0D1F3F&colorB=A23CD6)](https://github.com/podman-container-tools/podman)
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Winipedia/pyrig/main/docs/assets/badge.json)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-webapp?style=social)](https://github.com/Winipedia/pyrig-webapp)
[![VersionControlHookManager](https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge.svg)](https://github.com/j178/prek)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
[![WebAppFramework](https://img.shields.io/badge/reflex-1C1C1E?logo=reflex&logoColor=white)](https://github.com/reflex-dev/reflex)
[![WebServer](https://img.shields.io/badge/caddy-0059D1?logo=caddy&logoColor=22B638)](https://github.com/caddyserver/caddy)
<!-- project-info -->
[![ContainerRegistry](https://img.shields.io/badge/GHCR-Container_Image-black?logo=github&logoColor=white)](https://github.com/Winipedia/pyrig-webapp/pkgs/container/pyrig-webapp)
[![DocsBuilder](https://img.shields.io/badge/Documentation-zensical-326CE5)](https://Winipedia.github.io/pyrig-webapp)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-webapp?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-webapp)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-webapp)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-webapp)](https://github.com/Winipedia/pyrig-webapp/blob/main/LICENSE)

---

> A pyrig plugin to build web applications.

---

## Overview

pyrig-webapp is a [pyrig](https://github.com/Winipedia/pyrig) plugin that
scaffolds a [Reflex](https://github.com/reflex-dev/reflex) web application and
packages it with a [Caddy](https://github.com/caddyserver/caddy) reverse proxy
for local or production use.

## Requirements

In addition to pyrig's requirements, you will also need the requirements for
[pyrig-containers](https://github.com/Winipedia/pyrig-containers).
For local composing port forwarding from ports 80/443 to 8080/8443 is required,
you may use the `scripts/forward-ports.sh` script to set it up.
You may need to trust Caddy's local certificate authority in your browser or
operating system for local HTTPS to work without warnings.

## What it adds

- **Reflex application** — a starter app module and `rxconfig.py` are generated
  for the project. The default page displays “Hello, World!” and can be
  customized in the generated app module.
- **Framework tooling** — Reflex is added as a runtime dependency, its generated
  files are ignored by version control, and pyrig compiles the app after project
  synchronization and in a pre-push hook.
- **Caddy configuration** — a `caddy/Caddyfile` reverse-proxies requests to the
  Reflex application. `SITE_ADDRESS` configures the site address; it defaults
  to `localhost`.
- **Container configuration** — the container and Compose configuration runs the
  app alongside Caddy, with health checks, persistent Caddy data, and HTTP,
  HTTPS, and HTTP/3 ports published on higher host ports 8080 and 8443.
  to GHCR on release.
- **Port forwarding** — `scripts/forward-ports.sh` sets up permanent forwarding
  from ports 80/443 to the Compose-published ports 8080/8443.

## Usage

```bash
uv add pyrig-webapp --dev
uv run pyrig sync
sudo bash scripts/forward-ports.sh
```

After synchronization, edit the generated app module to build your application.
Start the application and proxy together from the project root:

```bash
bash scripts/compose-up.sh build
# or to use the published image
bash scripts/compose-up.sh pull
```

## Documentation

Full documentation is available on the [documentation site](https://Winipedia.github.io/pyrig-webapp).
