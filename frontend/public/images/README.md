This folder is for static images used by the portal UI.

Usage notes:
- Files placed here are served statically by the dev server and will be available at `/images/<filename>` in the browser.
- In React code you can reference them directly, for example:

  - <img src="/images/logo-placeholder.svg" alt="Logo" />

- Add production-ready images here (SVG, PNG, JPG, WebP). For large or generated assets, consider keeping them in `src/assets` and importing them.
