# ai-lab-repo-intelligence-suite-18

ai-lab-repo-intelligence-suite-18 is a production-oriented local product created by Autonomous AI Lab.
It is built as a real GitHub-ready tool, not as a bare scaffold: the repository
contains a FastAPI backend, static operator dashboard, CLI entrypoint, domain
services, tests, security notes, operations docs, and Docker packaging.

## Who It Is For

Technical founders, maintainers, and solo builders who want a useful local tool
that can run without paid infrastructure and can be published to the owner's
GitHub only after explicit approval.

## Product Value

The product implements the idea below as a local-first system:

A repository intelligence platform that audits GitHub projects, scores production readiness, builds security/readme/test reports, and exports actionable roadmaps.

The release is allowed only when the README run path, API surface, CLI, UI,
tests, security scan, Product Reviewer, and Definition of Done are all green.

## Features

- FastAPI application with `/api/health` and product endpoints.
- Static dashboard served by the backend.
- CLI command for a quick local smoke/demo workflow.
- Domain services that model the product behavior.
- Risk/readiness logic used before publication.
- Unit tests for core behavior.
- Dockerfile and docker-compose for local operation.
- `.env.example` with placeholders only; `.env` is ignored.
- Documentation for architecture, operations, security, backlog, and quality.

## Local Setup

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s tests
python -m compileall app scripts tests
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open the dashboard at:

```text
http://localhost:8000/
```

Check the API:

```bash
curl http://localhost:8000/api/health
```

Run the CLI smoke demo:

```bash
python cli.py
```

## Docker Run

```bash
docker compose up --build
```

## Definition Of Done

This repository is not considered ready if it is only a skeleton, if the UI is
empty, if tests fail, if Product Reviewer finds blockers, if security checks
fail, or if a user cannot run the product by following this README.

## Release Policy

Publication is owner-gated. Autonomous AI Lab may prepare commits, releases,
and GitHub Pages/Docker-ready artifacts, but it must not publish a red project
or a project that cannot be genuinely used from this README.
