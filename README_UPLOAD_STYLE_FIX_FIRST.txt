TA-14 Emergency Style Fix

The live site text is loading but the page looks unstyled. That means CSS is missing or the HTML is pointing to a CSS path that does not exist.

Upload these files FIRST, directly into the repo root:

- styles.css
- style.css

Also upload the assets folder if your GitHub uploader allows folders:

- assets/styles.css

Do not delete anything.

After deploy, refresh:
https://ta14-architecture.netlify.app/

If the site becomes styled again, the issue was CSS path/loading.

Suggested commit message:
Restore TA-14 site styling
