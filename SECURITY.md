# 🔒 Security Best Practices

## API Keys

✅ **DO**
- Store keys in `.env` (not in code)
- Add `.env` to `.gitignore` ✓
- Use `.env.example` as template
- Rotate keys regularly
- Use minimal permissions

❌ **DON'T**
- Commit `.env` to Git
- Hardcode API keys
- Share `.env` via email/chat
- Use weak passwords
- Reuse keys across projects

## Database Passwords

```env
# ✅ Good: Strong password
POSTGRES_PASSWORD=SecurePassword123!

# ❌ Bad: Weak password
POSTGRES_PASSWORD=admin
```

## File Permissions

```bash
# Restrict .env access
chmod 600 .env
```

## Docker Security

- Use specific Python versions (not `latest`)
- Expose only needed ports
- Use strong secrets
- Keep images updated

## Code Security

- Never log API keys
- Use environment variables
- Validate inputs
- Keep dependencies updated

See SECURITY.md for detailed guidelines.
