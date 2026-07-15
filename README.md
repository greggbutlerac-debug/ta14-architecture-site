# TA-14 Architecture Site

Public authority portal for the **TA-14 Admissible Execution Architecture**.

This repository contains the static website deployed at:

**https://ta14-architecture.netlify.app/**

TA-14 governs consequence-bearing execution through a complete evidence-to-outcome chain:

**Reality → Record → Continuity → Admissibility → Binding → Commit → Execution → Outcome**

The public site documents the architecture, live technical capabilities, review services, use cases, public record, environmental governance work, Partner Review Network, and pathways for organizations seeking TA-14 evaluation.

> **No admissible evidence. No admissible execution.**

---

## Repository Purpose

This repository is the source for the main TA-14 public website.

It is responsible for:

- explaining the TA-14 architecture;
- establishing TA-14’s public positioning and scope;
- providing access to the live Admissible Execution Gate;
- providing access to the public API Sandbox;
- hosting the Independent Route Replay Verifier;
- documenting governance review services and pricing;
- preserving public-record and architectural references;
- routing organizations into the TA-14 Review Desk;
- presenting Environmental Integrity Governance and Evidence Integrity work;
- documenting the TA-14 Partner Review Network.

This repository is **not** the source repository for the TA-14 API Sandbox or Admissible Execution Gate implementation.

---

## Related TA-14 Repositories

### Public Architecture Website

`greggbutlerac-debug/ta14-architecture-site`

This repository.

### TA-14 API Sandbox and Replay Verification

`greggbutlerac-debug/greggbutlerac-debug-ta14-api-sandbox`

Contains the public API reference implementation, OpenAPI documentation, replay verification service, replay-package standard, and synthetic verification samples.

### TA-14 Admissible Execution Gate

`greggbutlerac-debug/ta14-admissible-execution-gate`

Contains the broader execution-gate architecture and implementation record.

Do not overwrite Gate or Sandbox files when updating this website repository.

---

## Major Public Routes

### Core Architecture

- `/`
- `/start-here.html`
- `/architecture.html`
- `/positioning.html`
- `/what-ta14-is-not.html`
- `/no-build-before-boundary.html`

### Live Technical Surfaces

- `/gate.html`
- `/replay-verification.html`
- `/resources.html`
- `/public-record.html`

### Services and Reviews

- `/services.html`
- `/review-offers.html`
- `/governance-review.html`
- `/certification-readiness.html`
- `/pricing.html`
- `/request-evaluation.html`

### Use Cases and Procurement

- `/use-cases.html`
- `/ai-procurement.html`

### Governance Domains

- `/environmental-integrity.html`
- `/environmental-integrity-governance.html`
- `/evidence-integrity.html`
- `/evidence.html`

### Network and Institutional Pages

- `/partner-review-network.html`
- `/partners.html`
- `/founder.html`

---

## Independent Route Replay Verification

The website includes a live public verification surface that allows visitors to:

1. download a valid synthetic replay package;
2. upload it into the public verifier;
3. receive an independent verification report;
4. test intentionally altered packages;
5. observe package tampering, ledger discontinuity, and signature mismatch detection.

The verifier evaluates:

- package and file integrity;
- SHA-256 digests;
- Ed25519 signatures;
- route identity;
- receipt dependencies;
- evidence integrity;
- ruleset integrity;
- action binding;
- commit integrity;
- ledger continuity;
- execution correspondence;
- outcome correspondence.

Live verifier:

**https://ta14-architecture.netlify.app/replay-verification**

DOI-backed archival reference:

**https://doi.org/10.5281/zenodo.21365307**

---

## Site Architecture

The site is primarily static HTML and CSS.

Important files include:

```text
/
├── index.html
├── start-here.html
├── architecture.html
├── services.html
├── use-cases.html
├── resources.html
├── pricing.html
├── replay-verification.html
├── request-evaluation.html
├── public-record.html
├── partner-review-network.html
├── founder.html
├── style.css
├── styles.css
├── netlify.toml
├── _redirects
├── public/
└── review-desk/
