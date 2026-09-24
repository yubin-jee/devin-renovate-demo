# svc-orders (demo sandbox)

Backend service used to demo Renovate dependency PRs + Devin validation.
Deliberately pinned to old, vulnerable versions across npm, pip, Docker and GitHub Actions.

- `requirements.txt` — pydantic 1.x (breaking major available), urllib3/requests/PyYAML/cryptography/Jinja2 with known CVEs
- `package.json` — lodash/minimist/node-fetch/jsonwebtoken/tar with known CVEs
- `renovate.json` — non-majors batched into one PR, majors split and labelled `needs-devin-validation`
