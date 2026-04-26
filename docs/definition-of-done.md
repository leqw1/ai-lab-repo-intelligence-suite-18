# Definition of Done

Target user: A technical founder or maintainer who needs a locally runnable production tool with GitHub-ready packaging and no paid infrastructure.

## Required Features

- A useful core domain engine, not only a generated project skeleton.
- FastAPI service with health/readiness endpoints and product APIs.
- A non-empty local web dashboard that shows real product state.
- CLI commands for smoke/demo workflows.
- Persistent local data or import/export workflow where the product needs state.
- Risk and readiness scoring before publication.
- Operator docs with setup, demo, troubleshooting, and limits.
- Automated tests for the main user scenarios.
- Docker-ready local run path with .env.example and no secrets.
- Repository audit counts code, docs, tests, and release risks.
- Readiness score produces an actionable release decision.
- Roadmap export lists concrete follow-up work.

## API Scenarios

- /health returns ok
- /api/health returns ok
- /api/* returns real product data
- /api/audit returns repository readiness data

## CLI Scenarios

- python cli.py --help or python cli.py exits successfully
- make test documents the test path
- python cli.py audit <path> documents a real audit path

## UI Scenarios

- app/static/index.html renders meaningful product UI
- app/static/app.js contains product logic

## Not Ready If

- Only a scaffold/template exists without domain behavior.
- README promises features that the code does not implement.
- Tests, build, e2e, product reviewer, or security checks fail.
- The product cannot be used by following README instructions.
