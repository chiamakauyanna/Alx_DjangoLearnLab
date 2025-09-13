# Security Best Practices Implemented

## Step 1: Secure Settings
- `DEBUG = False` in production
- `SECURE_BROWSER_XSS_FILTER = True`
- `X_FRAME_OPTIONS = "DENY"`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `CSRF_COOKIE_SECURE = True`
- `SESSION_COOKIE_SECURE = True`

## Step 2: CSRF Protection
- All forms include `{% csrf_token %}` in templates.

## Step 3: Safe Data Access
- ORM used instead of raw SQL queries.
- User inputs validated via Django forms.

## Step 4: Content Security Policy (CSP)
- Configured via `django-csp` middleware to restrict allowed sources for scripts, styles, and images.

## Step 5: Testing
- Verified that forms reject missing/invalid CSRF tokens.
- Checked search input for SQL injection attempts → blocked by ORM.
- CSP tested by attempting inline JavaScript injection → blocked by browser.
