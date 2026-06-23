# Deployment Notes

1. Back up the current site.
2. Copy all files from this bundle's `public/` folder into the repository's public/static output folder.
3. Confirm that `assets/styles.css` is uploaded.
4. Deploy through Netlify.
5. Test these paths after deploy:
   - `/`
   - `/start-here.html`
   - `/architecture.html`
   - `/services.html`
   - `/request.html`
   - `/thank-you.html`
6. Submit a test request through the form. If Netlify Forms does not capture it, use the mailto CTA until Netlify Forms is configured.

## Navigation

The header links assume `.html` routes. If your existing Netlify site uses extensionless routes like `/architecture`, either keep redirects or rename links in the HTML.
