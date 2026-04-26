from __future__ import annotations

from fastapi import APIRouter

from app.services.agent_company import AgentCompany
from app.services.project_board import ProjectBoard
from app.services.risk_engine import RiskEngine


router = APIRouter(prefix="/api")
company = AgentCompany.default()
board = ProjectBoard.demo()
risk_engine = RiskEngine()


@router.get("/health")
def health() -> dict[str, object]:
    return {"ok": True, "service": "production-suite"}


@router.get("/agents")
def agents() -> dict[str, object]:
    return {"agents": [agent.as_dict() for agent in company.agents]}


@router.get("/projects")
def projects() -> dict[str, object]:
    return {"projects": [project.as_dict() for project in board.projects]}


@router.get("/risks")
def risks() -> dict[str, object]:
    return {"risks": risk_engine.evaluate_board(board).as_dict()}
