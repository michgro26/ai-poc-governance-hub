from app.models import PocEvaluation, PocInput, Recommendation


def evaluate_poc(payload: PocInput) -> PocEvaluation:
    business_score = payload.business_impact * 20
    technology_score = payload.technical_feasibility * 15
    risk_penalty = payload.risk_level * 8

    governance_penalty = 0.0
    rationale: list[str] = []

    if not payload.ai_policy_compliance:
        governance_penalty += 20
        rationale.append("Use case nie spełnia obecnej polityki AI.")

    if payload.data_sensitivity == "high":
        governance_penalty += 10
        rationale.append("Wysoka wrażliwość danych wymaga dodatkowych zabezpieczeń.")

    if payload.uses_personal_data and not payload.requires_human_in_the_loop:
        governance_penalty += 15
        rationale.append("Dane osobowe bez Human-in-the-Loop zwiększają ryzyko operacyjne i zgodności.")

    adoption_bonus = 5 if payload.estimated_users >= 100 else 0
    if adoption_bonus:
        rationale.append("Wysoki potencjał adopcji zwiększa wartość biznesową PoC.")

    final_score = business_score + technology_score + adoption_bonus - risk_penalty - governance_penalty
    final_score = max(0.0, min(100.0, round(final_score, 2)))

    if final_score >= 75 and governance_penalty <= 10:
        recommendation = Recommendation.GO
    elif final_score >= 60:
        recommendation = Recommendation.GO_WITH_GUARDRAILS
    elif final_score >= 40:
        recommendation = Recommendation.REVIEW
    else:
        recommendation = Recommendation.NO_GO

    if not rationale:
        rationale.append("Use case spełnia podstawowe kryteria biznesowe i technologiczne.")

    return PocEvaluation(
        business_score=round(business_score, 2),
        technology_score=round(technology_score, 2),
        risk_penalty=round(risk_penalty, 2),
        governance_penalty=round(governance_penalty, 2),
        adoption_bonus=round(adoption_bonus, 2),
        final_score=final_score,
        recommendation=recommendation,
        rationale=rationale,
    )
