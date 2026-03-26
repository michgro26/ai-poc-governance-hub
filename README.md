# AI PoC Governance Hub

Projekt przygotowałem jako demonstrację podejścia do wdrażania nowych technologii IT w dużej organizacji — szczególnie w obszarze AI, Big Data, oceny ryzyka, testowania i koordynowania PoC.

Inspiracją był dla mnie zakres obowiązków związany ze stanowiskiem **ds. nowych technologii IT**, w którym ważne są nie tylko kompetencje techniczne, ale też umiejętność łączenia technologii z potrzebami biznesowymi, governance oraz jakością wdrożeń.

## Cel projektu

Celem projektu było zaprojektowanie prostego, ale realistycznego systemu wspierającego ocenę i prowadzenie prototypów AI / Big Data w organizacji.

System pozwala:
- zgłosić pomysł na PoC,
- ocenić jego wartość biznesową i wykonalność technologiczną,
- uwzględnić ryzyka związane z danymi, zgodnością i bezpieczeństwem,
- wygenerować rekomendację wdrożeniową,
- monitorować podstawowe wskaźniki dla portfela inicjatyw.

Chciałem pokazać tym projektem, że potrafię myśleć nie tylko o implementacji rozwiązania, ale też o jego sensie biznesowym, ryzykach, zasadach testowania i miejscu w większym procesie organizacyjnym.

## Dlaczego ten projekt?

W wielu organizacjach wdrażanie nowych technologii nie kończy się na stworzeniu modelu albo API. Równie ważne są pytania:
- czy dany pomysł ma realną wartość biznesową,
- czy można go wdrożyć bezpiecznie,
- czy jest zgodny z polityką organizacji,
- jakie są kryteria testów,
- które inicjatywy powinny mieć priorytet.

Dlatego zamiast budować kolejny „chatbot”, przygotowałem projekt, który pokazuje szersze spojrzenie na obszar nowych technologii IT.

## Zakres funkcjonalny

### 1. Rejestracja pomysłu na PoC

Użytkownik może zgłosić inicjatywę, podając m.in.:
- nazwę projektu,
- jednostkę biznesową,
- opis problemu,
- poziom wrażliwości danych,
- przewidywany wpływ biznesowy,
- wykonalność technologiczną,
- poziom ryzyka,
- zgodność z polityką AI,
- potrzebę udziału człowieka w procesie decyzyjnym.

### 2. Scoring i rekomendacja

System ocenia zgłoszenie na podstawie uproszczonego modelu scoringowego i generuje:
- `business score`,
- `technology score`,
- `risk penalty`,
- `final score`,
- rekomendację:
  - `GO`
  - `GO_WITH_GUARDRAILS`
  - `REVIEW`
  - `NO_GO`

### 3. Element governance dla AI

W repozytorium zawarłem również przykładowe dokumenty wspierające governance:
- uproszczoną politykę AI,
- założenia architektoniczne,
- strategię testowania,
- materiał opisujący projekt z perspektywy portfolio.

Dzięki temu projekt pokazuje nie tylko warstwę programistyczną, ale też sposób dokumentowania i porządkowania wdrożeń nowych technologii.

### 4. Dashboard analityczny

Dodatkowo przygotowałem prosty dashboard, który prezentuje:
- liczbę aktywnych PoC,
- średni wynik końcowy,
- rozkład rekomendacji,
- inicjatywy o najwyższym priorytecie,
- przypadki wymagające dodatkowych zabezpieczeń.

## Jak ten projekt odpowiada na wymagania stanowiska?

Ten projekt dobrze odzwierciedla zadania związane z obszarem nowych technologii IT, ponieważ obejmuje:

- **analizę potrzeb biznesowych** — przez formularz zgłoszeń i ocenę use case’ów,
- **udział w projektach nowych technologii** — przez architekturę aplikacji, API i dashboard,
- **upowszechnianie wiedzy** — przez dokumentację techniczną i opis decyzji projektowych,
- **koordynację PoC** — przez statusy, scoring i rekomendacje,
- **udział w rozwoju polityki AI** — przez dokument `docs/ai_policy.md`,
- **przygotowanie zasad testowania** — przez `docs/test_strategy.md` i testy automatyczne,
- **wsparcie analityki biznesowej** — przez moduł dashboardowy i KPI.

## Stack technologiczny

- **Python 3.11+**
- **FastAPI** — REST API
- **Pydantic** — walidacja danych wejściowych
- **Pandas** — przetwarzanie i analiza danych
- **Streamlit** — dashboard analityczny
- **Pytest** — testy automatyczne

## Struktura repozytorium

```text
ai-poc-governance-hub/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── engine.py
│   ├── repository.py
│   ├── dashboard.py
│   └── services/
│       └── analytics.py
├── data/
│   └── sample_pocs.csv
├── docs/
│   ├── ai_policy.md
│   ├── architecture.md
│   ├── portfolio_pitch.md
│   └── test_strategy.md
├── tests/
│   └── test_engine.py
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml
