from app.engine import evaluate_poc
from app.models import PocInput


def test_should_recommend_go_for_strong_low_risk_case() -> None:
    payload = PocInput(
        title="Automatyczna analiza dokumentów obsługowych",
        business_unit="Operacje",
        problem_statement="Klasyfikacja dokumentów i skrócenie czasu obsługi zgłoszeń klientów.",
        data_sensitivity="medium",
        uses_personal_data=True,
        business_impact=5,
        technical_feasibility=5,
        risk_level=1,
        ai_policy_compliance=True,
        requires_human_in_the_loop=True,
        estimated_users=500,
        status="idea",
    )

    result = evaluate_poc(payload)

    assert result.final_score >= 75
    assert result.recommendation.value == "GO"


def test_should_recommend_no_go_for_non_compliant_high_risk_case() -> None:
    payload = PocInput(
        title="Pełna automatyzacja decyzji bez kontroli człowieka",
        business_unit="Ryzyko",
        problem_statement="Automatyczne podejmowanie decyzji na podstawie danych wrażliwych bez udziału człowieka.",
        data_sensitivity="high",
        uses_personal_data=True,
        business_impact=2,
        technical_feasibility=2,
        risk_level=5,
        ai_policy_compliance=False,
        requires_human_in_the_loop=False,
        estimated_users=50,
        status="idea",
    )

    result = evaluate_poc(payload)

    assert result.final_score < 40
    assert result.recommendation.value == "NO_GO"
