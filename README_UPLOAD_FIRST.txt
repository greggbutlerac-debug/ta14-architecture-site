TA-14 Phase 1 Request Fix - Flat Upload

This zip has NO outer folder and NO public folder.

Upload these files first:

1. request-evaluation.html
2. request.html
3. thank-you.html
4. 404.html
5. _redirects

Where to upload:
Upload them into the SAME folder where the current live request-evaluation page is coming from.

Most likely:
- If your repo has a public folder, upload these files directly inside public/
- If your repo has HTML files at the root, upload these files at the root next to index.html

Do NOT upload a containing folder.

After deploy, test:
https://ta14-architecture.netlify.app/request-evaluation
https://ta14-architecture.netlify.app/request
https://ta14-architecture.netlify.app/request-evaluation.html
https://ta14-architecture.netlify.app/request.html

The page includes:
- Big Email TA-14 Review Request button
- mailto:ta14admissibleexecution@gmail.com
- Netlify form
- Thank-you page
- Redirect fallback

Suggested commit message:
Fix TA-14 request evaluation route and CTA
