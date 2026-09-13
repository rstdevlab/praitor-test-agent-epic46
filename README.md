# praitor-test-agent

**This repository is disposable and non-production.**

It exists solely as the authorized live-evidence target for
[`rstdevlab/praitor`](https://github.com/rstdevlab/praitor) Epic 76
("Stand Up a Disposable Live Target for Epic 46's Evidence Stories").
Epic 46's Stories 46.3-46.9 are the consumers of the workflow/deployment
this repository supports.

It contains no secrets, and nothing here should ever be treated as a real
deployable product agent. The service is intentionally trivial: a single
`GET /` endpoint returning a fixed JSON "hello" body, implemented with only
the Python standard library, plus a minimal single-stage `Dockerfile` to
build it.

Run locally:

```bash
python3 main.py
curl http://localhost:8080/
```

Build the container image:

```bash
docker build -t praitor-test-agent .
docker run --rm -p 8080:8080 praitor-test-agent
```
