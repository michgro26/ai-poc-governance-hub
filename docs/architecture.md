# Architektura rozwiązania

```mermaid
flowchart TD
    A[Zgłoszenie potrzeby biznesowej] --> B[API FastAPI]
    B --> C[Silnik scoringu PoC]
    C --> D[Ocena ryzyka i zgodności AI]
    D --> E[Repozytorium inicjatyw]
    E --> F[Dashboard Streamlit]
    E --> G[Raporty / KPI dla analityki biznesowej]
```

## Warstwy
- **Presentation**: dashboard Streamlit + Swagger UI
- **Application**: FastAPI endpoints
- **Domain**: modele danych i silnik rekomendacyjny
- **Analytics**: KPI i priorytetyzacja portfela PoC

## Rozszerzenia produkcyjne
- PostgreSQL zamiast pamięci lokalnej,
- Keycloak / Azure AD do uwierzytelniania,
- audyt zmian,
- integracja z lokalnym LLM,
- ocena zgodności z regulacjami.
