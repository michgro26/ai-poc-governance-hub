from app.engine import evaluate_poc
from app.models import PocInput, PocRecord


class InMemoryPocRepository:
    def __init__(self) -> None:
        self._records: list[PocRecord] = []
        self._current_id = 1

    def list_all(self) -> list[PocRecord]:
        return self._records

    def add(self, payload: PocInput) -> PocRecord:
        evaluation = evaluate_poc(payload)
        record = PocRecord(id=self._current_id, payload=payload, evaluation=evaluation)
        self._records.append(record)
        self._current_id += 1
        return record


repository = InMemoryPocRepository()
