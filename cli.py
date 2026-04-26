from __future__ import annotations

from app.services.agent_company import AgentCompany


def main() -> int:
    company = AgentCompany.default()
    print("Agents:")
    for role in company.role_names():
        print(f"- {role}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
