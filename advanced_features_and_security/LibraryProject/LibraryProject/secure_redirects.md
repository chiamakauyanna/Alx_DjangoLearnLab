# HTTPS and Secure Redirects Configuration

## Django Settings
- `SECURE_SSL_REDIRECT = True`: Redirects all HTTP traffic to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS-only communication for 1 year.
- `SESSION_COOKIE_SECURE = True`: Ensures cookies are sent only over HTTPS.
- `CSRF_COOKIE_SECURE = True`: Protects CSRF cookies from being transmitted over insecure connections.
- `X_FRAME_OPTIONS = "DENY"`: Prevents clickjacking by disallowing the site from being displayed in frames.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents browsers from MIME-sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS filtering.

## Deployment Notes
- Use a valid SSL/TLS certificate (e.g., Let's Encrypt).
- Configure your web server (Nginx/Apache) to enforce HTTPS.
- Redirect all HTTP traffic to HTTPS at the server level.

## Review
These measures ensure:
- Encrypted communication (protects against eavesdropping).
- Protection against XSS, clickjacking, and MIME sniffing.
- Secure cookie handling over HTTPS only.
