# HTTPS and Security Configuration in LibraryProject

## Overview
This Django application enforces HTTPS and implements security best practices.

## Settings (settings.py)
- `SECURE_SSL_REDIRECT = True`: Redirects all HTTP to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS for 1 year via HSTS.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows HSTS preload for browser trust.
- `SESSION_COOKIE_SECURE = True`: Session cookies over HTTPS only.
- `CSRF_COOKIE_SECURE = True`: CSRF cookies over HTTPS only.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Stops MIME sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables XSS filter.
- CSP via `django-csp`: Restricts content sources.

## Deployment (deployment/nginx.conf)
- Nginx config redirects HTTP to HTTPS and serves SSL/TLS.
- Uses Let’s Encrypt certificates for secure communication.

## Security Review
- **Measures**: HTTPS enforced, cookies secured, headers protect against XSS/clickjacking.
- **Benefits**: Data encrypted, reduced attack surface.
- **Improvements**: Tighten CSP (remove 'unsafe-inline'), use production-grade database, monitor SSL certificate renewal.

## Testing
- Local: Use `DEBUG = True` and a proxy like `ngrok` for HTTPS testing.
- Production: Deploy with Nginx, verify redirects and headers with browser tools.
