from enum import Enum
from pydantic import BaseModel, Field


class DataSensitivity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class PocStatus(str, Enum):
    IDEA = "idea"
    IN_REVIEW = "in_review"
    POC = "poc"
    PILOT = "pilot"
    REJECTED = "rejected"
    COMPLETED = "completed"


class Recommendation(str, Enum):
    GO = "GO"
    GO_WITH_GUARDRAILS = "GO_WITH_GUARDRAILS"
    REVIEW = "REVIEW"
    NO_GO = "NO_GO"


class PocInput(BaseModel):
    title: str = Field(..., min_length=5, max_length=120)
    business_unit: str = Field(..., min_length=2, max_length=80)
    problem_statement: str = Field(..., min_length=15, max_length=500)
    data_sensitivity: DataSensitivity
    uses_personal_data: bool
    business_impact: int = Field(..., ge=1, le=5)
    technical_feasibility: int = Field(..., ge=1, le=5)
    risk_level: int = Field(..., ge=1, le=5)
    ai_policy_compliance: bool
    requires_human_in_the_loop: bool
    estimated_users: int = Field(..., ge=1, le=100000)
    status: PocStatus = PocStatus.IDEA


class PocEvaluation(BaseModel):
    business_score: float
    technology_score: float
    risk_penalty: float
    governance_penalty: float
    adoption_bonus: float
    final_score: float
    recommendation: Recommendation
    rationale: list[str]


class PocRecord(BaseModel):
    id: int
    payload: PocInput
    evaluation: PocEvaluation
