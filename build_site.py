from pathlib import Path
root = Path('/mnt/data/ta14-architecture-premium-site/public')
email = 'greggbutlerac@gmail.com'
nav = '''
<header class="site-header">
  <nav class="nav" aria-label="Primary navigation">
    <a class="brand" href="index.html"><span class="brand-mark">14</span><span>TA-14</span></a>
    <div class="nav-links">
      <a href="start-here.html">Start Here</a>
      <a href="architecture.html">Architecture</a>
      <a href="services.html">Services</a>
      <a href="evidence.html">Evidence</a>
      <a href="environmental-integrity.html">Environmental</a>
      <a href="partners.html">Partners</a>
      <a href="resources.html">Records</a>
      <a class="nav-cta" href="request.html">Request Review</a>
    </div>
  </nav>
</header>'''
footer = '''
<footer class="footer">
  <div class="footer-inner">
    <div>
      <strong>TA-14 Admissible Execution Architecture</strong>
      <p>No admissible evidence. No admissible execution.</p>
      <p>Architecture-facing reviews only. Not a legal opinion, security audit, certification, endorsement, or production validation unless separately stated in written scope.</p>
    </div>
    <div class="footer-links">
      <a href="request.html">Request Review</a>
      <a href="services.html">Services</a>
      <a href="resources.html">Public Records</a>
      <a href="mailto:greggbutlerac@gmail.com?subject=TA-14%20Review%20Request">Email</a>
    </div>
  </div>
</footer>'''

def page(title, desc, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="stylesheet" href="assets/styles.css" />
</head>
<body>
{nav}
{body}
{footer}
</body>
</html>
'''

chain_visual = '''
<div class="hero-card" aria-label="TA-14 chain visualization">
  <div class="chain-visual">
    <div class="chain-step"><div class="step-no">01</div><div><strong>Reality</strong><span>Identify the actual state before reliance.</span></div></div>
    <div class="chain-step"><div class="step-no">02</div><div><strong>Record</strong><span>Preserve provenance, context, and chronology.</span></div></div>
    <div class="chain-step"><div class="step-no">03</div><div><strong>Continuity</strong><span>Detect drift, breaks, substitution, and staleness.</span></div></div>
    <div class="chain-step"><div class="step-no">04</div><div><strong>Admissibility</strong><span>Decide whether evidence can support reliance.</span></div></div>
    <div class="chain-step"><div class="step-no">05-08</div><div><strong>Binding → Commit → Execution → Outcome</strong><span>Govern consequence before and after action.</span></div></div>
  </div>
</div>'''

pages = {}
pages['index.html'] = page('TA-14 Admissible Execution Architecture', 'Proof-bound governance for consequential systems before binding, commit, execution, or outcome.', f'''
<main>
  <section class="hero">
    <div>
      <p class="kicker">Proof-bound governance for consequential systems</p>
      <h1>Govern execution before consequence happens.</h1>
      <p class="lead">TA-14 determines whether a system has enough evidence, continuity, authority, scope, and accountability before it is allowed to bind, commit, execute, or create consequential reliance.</p>
      <div class="actions">
        <a class="button" href="request.html">Request a TA-14 Review</a>
        <a class="button secondary" href="start-here.html">Start Here</a>
        <a class="button ghost" href="architecture.html">Explore Architecture</a>
      </div>
    </div>
    {chain_visual}
  </section>

  <div class="strip"><section class="section metric-row">
    <div class="metric"><strong>Full-chain</strong><span>Reality through Outcome, not only audit or runtime gating.</span></div>
    <div class="metric"><strong>Evidence-first</strong><span>Information must become governed evidence before reliance.</span></div>
    <div class="metric"><strong>Boundary-safe</strong><span>Strengths-plus-gaps reviews without unsupported private-capability claims.</span></div>
    <div class="metric"><strong>Commercial-ready</strong><span>Clear review lanes, intake, and partner-review structure.</span></div>
  </section></div>

  <section class="section">
    <p class="kicker">Core philosophy</p>
    <h2>No admissible evidence. No admissible execution.</h2>
    <p class="lead">Monitoring can show conditions. Logs can preserve traces. Policies can express intent. TA-14 asks whether the chain that produces consequence-bearing action is admissible enough to allow execution at all.</p>
    <div class="flow"><div>Reality</div><div>Record</div><div>Continuity</div><div>Admissibility</div><div>Binding</div><div>Commit</div><div>Execution</div><div>Outcome</div></div>
  </section>

  <section class="section grid three">
    <article class="card"><span class="tag">Offer 01</span><h3>Public-Material Architecture Review</h3><p>Map public documentation, repositories, demos, and claims against the TA-14 admissible-execution chain.</p></article>
    <article class="card"><span class="tag">Offer 02</span><h3>Evidence Gap Review</h3><p>Determine whether records, logs, sensor data, outputs, baselines, thresholds, and outcomes support reliance.</p></article>
    <article class="card"><span class="tag">Offer 03</span><h3>Production-Readiness Review</h3><p>Evaluate whether consequence-bearing routes are governed from reality through outcome before scaling or deployment.</p></article>
  </section>

  <section class="section">
    <div class="quote"><p>TA-14 is not monitoring, audit logging, a policy dashboard, or only an execution gate. It is an admissible-execution architecture.</p><span><a href="what-ta14-is-not.html">Read the boundary page →</a></span></div>
  </section>

  <section class="section grid two">
    <div><p class="kicker">Begin review</p><h2>Need to know whether a system is ready to act?</h2><p class="lead">Use the request path to frame the system, consequence, evidence, authority, binding point, and risk of error before any review begins.</p><div class="actions"><a class="button" href="request.html">Open Request Page</a><a class="button secondary" href="mailto:{email}?subject=TA-14%20Review%20Request">Email Request</a></div></div>
    <div class="card"><h3>Review boundary</h3><p>TA-14 reviews are architecture-facing, evidence-first, chronology-first, continuity-first, strengths-plus-gaps assessments. Unless separately scoped, they are not legal opinions, certifications, endorsements, security audits, or production validations.</p></div>
  </section>
</main>
''')

pages['start-here.html'] = page('Start Here | TA-14', 'A plain-English starting point for understanding TA-14 admissible execution.', '''
<main>
  <section class="page-hero"><p class="kicker">Start Here</p><h1>Why TA-14 exists.</h1><p class="lead">Modern systems can generate outputs, recommendations, actions, environmental changes, institutional decisions, and downstream reliance faster than people can verify whether the underlying evidence is still valid.</p></section>
  <article class="article">
    <div class="quote"><p>Should this system be allowed to act, bind, commit, or create reliance based on the evidence available right now?</p></div>
    <section><h2>Why ordinary governance is not enough</h2><p>Many systems are monitored. Many systems produce logs. Many systems have policies, dashboards, human approvals, or after-the-fact audit trails. Those controls may be useful, but they do not automatically prove that a consequence-bearing action should have been allowed to proceed.</p><p>TA-14 focuses on the admissibility of execution itself. It asks whether the chain that produced a proposed action has enough governed evidence, continuity, authority, scope, binding basis, commit discipline, execution control, and outcome accountability before consequence attaches.</p></section>
    <section><h2>What TA-14 protects against</h2><div class="grid two"><div class="card"><h3>Execution without admissible evidence</h3><p>A system may act on data, signals, model outputs, sensor readings, or records that have not been governed enough to support reliance.</p></div><div class="card"><h3>Continuity breaks</h3><p>Evidence may degrade, drift, become stale, lose chronology, or disconnect from the real-world condition it represents.</p></div><div class="card"><h3>Authority mismatch</h3><p>Technical ability to act is not the same as admissible authority to act.</p></div><div class="card"><h3>After-the-fact accountability</h3><p>Logs may explain what happened; TA-14 asks whether action should have been allowed before it happened.</p></div></div></section>
  </article>
</main>''')

pages['architecture.html'] = page('Architecture | TA-14', 'The TA-14 chain and architecture domains.', '''
<main>
  <section class="page-hero"><p class="kicker">Architecture</p><h1>The full admissible-execution chain.</h1><p class="lead">TA-14 is not merely upstream or downstream. It governs the full stream through which reality becomes record, record becomes reliance, reliance becomes binding, binding becomes commit, commit becomes execution, and execution becomes outcome.</p></section>
  <section class="section"><div class="flow"><div>Reality</div><div>Record</div><div>Continuity</div><div>Admissibility</div><div>Binding</div><div>Commit</div><div>Execution</div><div>Outcome</div></div></section>
  <section class="section grid two">
    <article class="card"><h3>Parent architecture</h3><p>TA-14 Admissible Execution Architecture governs whether consequence-bearing systems are ready to act at all.</p></article>
    <article class="card"><h3>Evidence Governance</h3><p>Evidence must be classified, continuous, sufficient, preserved, and capable of supporting admissibility.</p></article>
    <article class="card"><h3>Reliance Governance</h3><p>No admissible reliance. No admissible execution. TA-14 asks what must be true before evidence can be relied upon.</p></article>
    <article class="card"><h3>Environmental Integrity Governance</h3><p>Atmospheric and HVACDR evidence must be governed as admissible records rather than ordinary monitoring alone.</p></article>
  </section>
</main>''')

pages['what-ta14-is-not.html'] = page('What TA-14 Is Not | TA-14', 'Boundary page explaining what TA-14 is not.', '''
<main>
  <section class="page-hero"><p class="kicker">Boundary</p><h1>What TA-14 is not.</h1><p class="lead">TA-14 is often easiest to understand by drawing clear boundaries around what it is not.</p></section>
  <section class="section grid two">
    <article class="card"><h3>Not ordinary monitoring</h3><p>Monitoring may observe activity. TA-14 asks whether evidence supports action before execution is allowed.</p></article>
    <article class="card"><h3>Not audit logging after the fact</h3><p>Audit logs may preserve what happened. TA-14 governs whether the chain was admissible before action occurred.</p></article>
    <article class="card"><h3>Not a policy dashboard</h3><p>Policy dashboards display controls. TA-14 determines whether evidence and authority are enough to bind, commit, execute, or create reliance.</p></article>
    <article class="card"><h3>Not only an execution gate</h3><p>TA-14 includes execution-boundary governance but covers the full stream from Reality through Outcome.</p></article>
  </section>
  <section class="section"><div class="quote"><p>TA-14 is an admissible-execution architecture. It asks whether the evidence, continuity, authority, scope, binding basis, commit boundary, execution control, and outcome record are sufficient before consequence-bearing action is allowed to proceed.</p></div></section>
</main>''')

pages['services.html'] = page('Services | TA-14 Review Offers', 'TA-14 public-material, evidence gap, and production-readiness reviews.', '''
<main>
  <section class="page-hero"><p class="kicker">Review offers</p><h1>Structured review lanes for consequence-bearing systems.</h1><p class="lead">Each review lane is designed to move serious systems from vague governance claims toward evidence clarity, admissibility posture, and scoped next steps.</p><div class="actions"><a class="button" href="request.html">Request Review</a><a class="button secondary" href="mailto:greggbutlerac@gmail.com?subject=TA-14%20Review%20Request">Email Request</a></div></section>
  <section class="section grid three">
    <article class="card"><span class="tag">Offer 01</span><h3>Public-Material Architecture Review</h3><p>For organizations, projects, or adjacent governance systems where TA-14 reviews public materials and maps observable strengths, gaps, and admissible-execution posture.</p></article>
    <article class="card"><span class="tag">Offer 02</span><h3>Evidence Gap Review</h3><p>For teams that need to know whether records, logs, sensor data, outputs, baselines, thresholds, determinations, and outcomes support reliance.</p></article>
    <article class="card"><span class="tag">Offer 03</span><h3>Production-Readiness Review</h3><p>For consequence-bearing workflows that need route-complete evidence from reality through outcome before deployment, scaling, or institutional reliance.</p></article>
  </section>
  <section class="section"><div class="notice"><strong>Boundary:</strong> Reviews identify strengths, gaps, posture, evidence requirements, and readiness pathways. They are not certifications, endorsements, legal opinions, security audits, or guarantees unless separately scoped in writing.</div></section>
</main>''')

pages['request.html'] = page('Request Review | TA-14', 'Submit or email a TA-14 review request.', f'''
<main>
  <section class="page-hero"><p class="kicker">Request Evaluation</p><h1>Start a TA-14 review request.</h1><p class="lead">Use the form below for Netlify Forms, or use the email button for a direct written request. The intake is designed to clarify the consequence-bearing pathway before review begins.</p><div class="actions"><a class="button" href="mailto:{email}?subject=TA-14%20Review%20Request&body=System%20/%20workflow:%0AConsequence-bearing%20action:%0AWho%20relies%20on%20it:%0AEvidence%20available:%0AAuthority:%0ABinding%20/%20commit%20point:%0AWhat%20happens%20if%20wrong:%0ARequested%20review%20type:%0A">Email a Review Request</a><a class="button secondary" href="services.html">View Review Offers</a></div></section>
  <section class="section">
    <form class="form-panel" name="ta14-review-request" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thank-you.html">
      <input type="hidden" name="form-name" value="ta14-review-request" />
      <p style="display:none"><label>Do not fill this out: <input name="bot-field" /></label></p>
      <div class="form-grid">
        <label>Full name <input name="name" required /></label>
        <label>Email <input name="email" type="email" required /></label>
        <label class="full">Organization / project <input name="organization" /></label>
        <label class="full">System / workflow to be reviewed <textarea name="system" required></textarea></label>
        <label class="full">Consequence-bearing action involved <textarea name="consequence" required></textarea></label>
        <label class="full">Who or what relies on the system output? <textarea name="reliance"></textarea></label>
        <label class="full">What evidence exists before action? <textarea name="evidence"></textarea></label>
        <label class="full">What authority allows the action? <textarea name="authority"></textarea></label>
        <label class="full">Where does binding or commit occur? <textarea name="binding"></textarea></label>
        <label class="full">What happens if the system is wrong? <textarea name="wrong"></textarea></label>
        <label>Requested review type <select name="review_type"><option>Public-Material Architecture Review</option><option>Evidence Gap Review</option><option>Partner Alignment Review</option><option>Environmental Integrity Review</option><option>Production-Readiness Review</option></select></label>
        <label>Preferred response path <select name="response_path"><option>Email / written response</option><option>Scoped proposal</option><option>Public-material review discussion</option></select></label>
        <div class="full"><button class="button" type="submit">Submit Review Request</button></div>
      </div>
      <p class="form-note">If the form is not active in your Netlify deployment yet, use the Email a Review Request button above. Written communications preserve review scope and provenance.</p>
    </form>
  </section>
</main>''')

pages['thank-you.html'] = page('Thank You | TA-14', 'Confirmation page for TA-14 review requests.', '''
<main><section class="page-hero"><p class="kicker">Received</p><h1>Thank you.</h1><p class="lead">Your TA-14 review request has been submitted. If the submission path is not active in your deployment, please send the request by email using the button below.</p><div class="actions"><a class="button" href="mailto:greggbutlerac@gmail.com?subject=TA-14%20Review%20Request">Email Request</a><a class="button secondary" href="index.html">Return Home</a></div></section></main>''')

pages['evidence.html'] = page('Evidence Integrity | TA-14', 'Evidence Integrity Governance and admissible evidence principles.', '''
<main>
  <section class="page-hero"><p class="kicker">Evidence Integrity</p><h1>Information is not evidence until it is governed.</h1><p class="lead">Evidence Governance asks what must be true of information before it can support reliance, admissibility, binding, commit, execution, or outcome accountability.</p></section>
  <section class="section grid three"><article class="card"><h3>Classification</h3><p>What kind of evidence is this, and what claim does it support?</p></article><article class="card"><h3>Continuity</h3><p>Has the record preserved chronology, provenance, context, and chain integrity?</p></article><article class="card"><h3>Sufficiency</h3><p>Is the evidence strong enough for the consequence-bearing action proposed?</p></article><article class="card"><h3>Authority</h3><p>Who may rely on the evidence, for what purpose, and under what scope?</p></article><article class="card"><h3>Survivability</h3><p>Does evidence remain usable under runtime pressure, drift, latency, or ambiguity?</p></article><article class="card"><h3>Outcome proof</h3><p>Can the outcome be verified, preserved, and reviewed after execution?</p></article></section>
</main>''')

pages['environmental-integrity.html'] = page('Environmental Integrity Governance | TA-14', 'Environmental Integrity Governance for atmospheric evidence and HVACDR pathways.', '''
<main>
  <section class="page-hero"><p class="kicker">Environmental Integrity Governance</p><h1>Atmospheric evidence is not ordinary monitoring.</h1><p class="lead">Environmental Integrity Governance treats sensing, IAQ, HVACDR, filtration, refrigeration, intervention, and post-intervention verification as evidence pathways that must be preserved, thresholded, interpreted, authorized, and verified.</p></section>
  <section class="section grid two"><article class="card"><h3>Evidence before intervention</h3><p>Non-invasive evidence should govern whether consequence-bearing refrigerant-side or environmental intervention is justified.</p></article><article class="card"><h3>Atmospheric continuity</h3><p>Records must preserve baseline, chronology, thresholds, diagnostic determination, intervention basis, and post-intervention proof.</p></article></section>
</main>''')

pages['partners.html'] = page('Partner Review Network | TA-14', 'TA-14 partner review network and alignment pathway.', '''
<main>
  <section class="page-hero"><p class="kicker">Partner Review Network</p><h1>Adjacent architectures keep their identity. TA-14 reviews admissible execution.</h1><p class="lead">TA-14 can operate as a second-layer admissible-execution review authority for serious adjacent governance systems, environmental evidence processes, runtime enforcement tools, and specialized partner frameworks.</p></section>
  <section class="section grid three"><article class="card"><h3>Boundary-only</h3><p>Light review of fit and non-overlap.</p></article><article class="card"><h3>Referral-only</h3><p>TA-14 routes appropriate opportunities without co-delivery.</p></article><article class="card"><h3>Scoped review candidate</h3><p>Partner receives defined TA-14 review language under written scope.</p></article><article class="card"><h3>Partner-track candidate</h3><p>Repeatable review relationship with approved use boundaries.</p></article><article class="card"><h3>Strategic ecosystem partner</h3><p>Co-delivered value where TA-14 remains the parent admissible-execution layer.</p></article><article class="card"><h3>Name-use rule</h3><p>TA-14 status, alignment, review, certification-readiness, or credibility language requires written approval.</p></article></section>
</main>''')

pages['resources.html'] = page('Public Records | TA-14', 'Public record and preservation anchors for TA-14.', '''
<main>
  <section class="page-hero"><p class="kicker">Public Records</p><h1>Preservation anchors and public entry points.</h1><p class="lead">Public resources support chronology, transparency, preservation, and review. They do not automatically certify, approve, endorse, or validate any third-party system.</p></section>
  <section class="section grid two">
    <article class="card"><h3>TA-14 homepage</h3><p><a href="https://sites.google.com/view/ta-14-admissible-execution-arc/home">Canonical Google Sites entry point →</a></p></article>
    <article class="card"><h3>Volume 1 Preservation</h3><p><a href="https://sites.google.com/view/ta-14-volume-1-preservation-ed/home">Institutional memory and preservation page →</a></p></article>
    <article class="card"><h3>Environmental Integrity Governance</h3><p><a href="https://sites.google.com/view/environmental-integrity-gover/home">Applied atmospheric evidence domain →</a></p></article>
    <article class="card"><h3>TA-14 Academy</h3><p><a href="https://sites.google.com/view/ta-14academy/the-14-step-system">14-step system →</a></p></article>
  </section>
</main>''')

pages['no-build-before-boundary.html'] = page('No Build Before Boundary | TA-14', 'Commercial boundary for TA-14 architecture value.', '''
<main>
  <section class="page-hero"><p class="kicker">Commercial Boundary</p><h1>No build-before-boundary.</h1><p class="lead">Free interaction may include brief fit assessment, public-material gap identification, and short threshold comments. Solution shaping, route definitions, test matrices, implementation guidance, evidence packet design, and maturity roadmaps require paid or reciprocal scope.</p></section>
  <section class="section"><div class="quote"><p>If the other party receives architecture value, TA-14 should receive payment, evidence, attribution, partnership, or another clear exchange of value.</p></div></section>
</main>''')

for name, content in pages.items():
    (root / name).write_text(content, encoding='utf-8')

(root.parent / 'README.md').write_text('''# TA-14 Premium Static Website Pack\n\nThis bundle is a complete static-site upgrade for the TA-14 public portal. It is zero-dependency: plain HTML and CSS.\n\n## Upload\n\nCopy the contents of `public/` into the site repository public/static folder, or replace the existing static pages after backing up the current repo.\n\n## Primary pages\n\n- `index.html` - upgraded homepage\n- `start-here.html` - plain-English entry point\n- `architecture.html` - full TA-14 chain and architecture domains\n- `what-ta14-is-not.html` - boundary-protection page\n- `services.html` - review offer lanes\n- `request.html` - Netlify form and mailto request path\n- `thank-you.html` - Netlify form success page\n- `evidence.html` - Evidence Integrity Governance\n- `environmental-integrity.html` - Environmental Integrity Governance\n- `partners.html` - Partner Review Network\n- `resources.html` - public records and anchors\n- `no-build-before-boundary.html` - commercial boundary page\n\n## Form note\n\n`request.html` includes both a Netlify Forms-compatible form and an email CTA to `greggbutlerac@gmail.com`. Netlify Forms will only work when the page is deployed through Netlify and form detection is enabled.\n\n## Suggested commit message\n\n`Upgrade TA-14 public portal static site`\n''', encoding='utf-8')

(root.parent / 'DEPLOYMENT_NOTES.md').write_text('''# Deployment Notes\n\n1. Back up the current site.\n2. Copy all files from this bundle's `public/` folder into the repository's public/static output folder.\n3. Confirm that `assets/styles.css` is uploaded.\n4. Deploy through Netlify.\n5. Test these paths after deploy:\n   - `/`\n   - `/start-here.html`\n   - `/architecture.html`\n   - `/services.html`\n   - `/request.html`\n   - `/thank-you.html`\n6. Submit a test request through the form. If Netlify Forms does not capture it, use the mailto CTA until Netlify Forms is configured.\n\n## Navigation\n\nThe header links assume `.html` routes. If your existing Netlify site uses extensionless routes like `/architecture`, either keep redirects or rename links in the HTML.\n''', encoding='utf-8')

(root.parent / 'COMMIT_MESSAGES.md').write_text('''# Commit Messages\n\nRecommended:\n\n```text\nUpgrade TA-14 public portal static site\n```\n\nAlternatives:\n\n```text\nAdd premium TA-14 static website pack\nAdd request form and review offer pages\nAdd TA-14 public portal conversion pages\n```\n''', encoding='utf-8')
