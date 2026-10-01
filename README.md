# Automation Portfolio 2026

> Hands-on QA Automation portfolio — test frameworks, real bug reports, and a structured path toward a remote SDET role.

**Estéfano Gigena** · QA / Automation Engineer · Villa Carlos Paz, Córdoba, Argentina
Moving from functional QA into test automation, and building everything in public.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)

## About me

I'm a QA professional transitioning from manual and functional testing into automation. I've worked as a QA Tester running regression suites and built workflow automations with n8n (integrating Airtable, HubSpot, Twilio and PostgreSQL). My focus now is writing robust, maintainable test frameworks in Python.

This repository is my public lab: every week I ship something that runs.

## What I can do today

- Design UI test suites with the **Page Object Model** (Playwright, sync API): a shared `BasePage` and one class per page, locators as attributes, actions as methods, assertions kept in the tests.
- Write **happy-path and negative tests** (invalid login, rejecting an already-registered email on signup).
- Cover full **end-to-end flows**: login → search → add to cart → checkout → payment confirmation.
- Keep suites reliable and debuggable: pytest fixtures, `.env`-based credentials (no secrets in the repo), and automatic **trace / video / screenshot capture on failure**.
- Perform **exploratory testing and bug reporting** with clear, reproducible reports (see `BUGS.md` below).
- Solid Python foundations: OOP, pytest, decorators, context managers, logging, and CSV/JSON handling.

## Highlighted work

### Page Object Model framework — Playwright + pytest
`module-2/week-06/`

Two end-to-end suites that also document my progression:

- **`saucedemo/`** — a deliberately simpler, more repetitive first pass
  (hardcoded URLs, no shared base class). Covers valid & invalid login,
  add to cart, and complete checkout.
- **`automation-exercise/`** — the refactored version: a shared `BasePage`
  holds the base URL and navigation, each page declares its own `PATH` and
  inherits from it. Covers valid & invalid login, negative signup, product
  search, add single & multiple products to cart, and a full checkout flow.

The contrast between the two is intentional — it shows the move from
"make it work" to "make it clean."

### Real bug found & documented
`module-2/week-06/automation-exercise/BUGS.md`

**BUG-001 (Critical):** the payment form accepts invalid card data (card number `"abc"`, CVC `"5"`) and still places and confirms the order. Reported with steps to reproduce, expected vs. actual result, and screenshot evidence.

### Python fundamentals, tested
`module-1/`

Exercism katas, an OOP gym-booking domain with unit tests, a price calculator, a CSV-driven test runner, and small utilities covering decorators, context managers and logging.

## Tech stack

**Core:** Python · Playwright · pytest · python-dotenv
**Also:** Selenium · PostgreSQL · n8n
**Practices:** Page Object Model · fixtures · negative testing · trace/video/screenshot on failure · secrets via `.env`

## Repository structure

```
module-1/                  # Python & pytest fundamentals
  week-02..05/             # katas, OOP, decorators, context managers, logging
  exam-1/                  # CSV-driven test runner
module-2/
  week-06/
    automation-exercise/   # POM suite + BUGS.md (bug evidence)
    saucedemo/             # POM suite
```

## Roadmap

A self-directed, structured path toward a remote **SDET** role, with a differentiator in **AI / LLM evaluation**:

- [x] Python & pytest fundamentals
- [x] UI automation with the Page Object Model
- [ ] API testing (requests + schema validation) and hybrid E2E
- [ ] CI with GitHub Actions
- [ ] AI quality suite — LLM evaluations (promptfoo / DeepEval)

## Running the tests

```bash
# from a project folder, e.g. module-2/week-06/saucedemo
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install pytest-playwright python-dotenv
playwright install
pytest
```

For `automation-exercise`, copy `.env.example` to `.env` and set `AE_EMAIL` / `AE_PASSWORD`.

## Contact

- LinkedIn: [estefano-gigena](https://www.linkedin.com/in/estefano-gigena)
- Open to **remote QA Automation / SDET** opportunities.
