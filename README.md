# TA-14 Public Portal Expansion Pack

This package adds standalone public HTML pages for the TA-14 Netlify/GitHub site.

## Intended use

Copy the contents of the `public/` folder into the site's `public/` directory, then commit and deploy.

These pages are designed as standalone static HTML pages. They should work even if the rest of the site is built with a modern frontend framework, as long as the deployment serves files from `public/`.

## Included pages

- `public/start-here.html` — plain-English public entry point for TA-14.
- `public/what-ta14-is-not.html` — boundary-protection page that prevents misframing TA-14 as monitoring, audit logging, a dashboard, or only a gate.
- `public/request-evaluation.html` — structured intake page for review requests.
- `public/review-offers.html` — simple commercial offer page with three review lanes.
- `public/public-record.html` — preservation and public-anchor page.
- `public/partner-review-network.html` — partner-review positioning and use restrictions.
- `public/no-build-before-boundary.html` — scope and value-exchange boundary page.
- `public/environmental-integrity.html` — applied Environmental Integrity Governance page.

## Recommended navigation labels

- Start Here → `/start-here.html`
- What TA-14 Is Not → `/what-ta14-is-not.html`
- Review Offers → `/review-offers.html`
- Request Evaluation → `/request-evaluation.html`
- Public Record → `/public-record.html`
- Partner Review Network → `/partner-review-network.html`
- No Build Before Boundary → `/no-build-before-boundary.html`
- Environmental Integrity → `/environmental-integrity.html`

## Suggested commit message

`Add TA-14 public portal expansion pages`

## Notes

These pages do not automatically change the site's navigation. Add links manually wherever your site controls navigation, homepage calls-to-action, footer links, or resource menus.
