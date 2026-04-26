# Architecture

## Modules

- `app.main`: FastAPI application entrypoint.
- `app.api.routes`: HTTP API for dashboard data.
- `app.core.domain`: typed domain objects.
- `app.services.agent_company`: role model for the AI company.
- `app.services.project_board`: project and approval state.
- `app.services.risk_engine`: deploy and operations risk scoring.
- `app.static`: operator dashboard.

## Deployment

The first production target is GitHub publication with Docker-ready packaging.
External hosting adapters are intentionally disabled until the owner approves them.
