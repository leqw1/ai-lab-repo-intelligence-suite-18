# Decision Log

Project: ai-lab-repo-intelligence-suite-18

Idea: A repository intelligence platform that audits GitHub projects, scores production readiness, builds security/readme/test reports, and exports actionable roadmaps.

Stack: Production Suite: FastAPI + static web dashboard + CLI + tests + Docker



## Definition Of Done

Target user: A technical founder or maintainer who needs a locally runnable production tool with GitHub-ready packaging and no paid infrastructure.

Required features:
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

## Agent Notes

- idea: A repository intelligence platform that audits GitHub projects, scores production readiness, builds security/readme/test reports, and exports actionable roadmaps. Strategy=ollama/qwen2.5-coder:7b.
- research: Production scope is intentionally modular: backend, operator UI, tests, docs, Docker packaging, and approval-gated GitHub publication inside sandbox. Reasoner=ollama/qwen2.5-coder:7b. Research references: research query recorded (about:blank)
- product_brief: Target user: A technical founder or maintainer who needs a locally runnable production tool with GitHub-ready packaging and no paid infrastructure.. Required features=12; API scenarios=4; CLI scenarios=3; UI scenarios=2. A GitHub release is forbidden until README instructions can run a useful product.
- architecture: production_suite:github_release_docker_ready; reasoner=ollama/qwen2.5-coder:7b
- codegen: ollama/qwen2.5-coder:7b
- qa: tests=True; build=True; repair_attempts=0; quality=100; iterations=3; e2e=True
- product_review: blocked=False
- security: secrets=0; dependency_findings=0

## Green Checks

- tests_passed: True
- build_passed: False
- secret_scan_passed: True
- dependency_scan_acceptable: True
- repo_owner_verified: True
- no_forbidden_files: True
- risk_score_acceptable: False
- readme_exists: True
- env_example_exists: True
- audit_log_written: True

## End To End Checks

- readme_has_run_path: True
- api_health_declared: True
- ui_nonblank: True
- cli_runs: True
- docker_ready: True

## Product Reviewer

- no blocking findings

Risk score: 0.85
