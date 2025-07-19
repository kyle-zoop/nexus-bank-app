# Production Deployment Security Checklist

## Environment Variables (set on hosting platform):
- DEBUG=false
- SECRET_KEY=<32-character-random-string>
- PORT=<platform-assigned-port>

## Domain Recommendations:
- Use a convincing bank-like domain name
- Ensure HTTPS is enabled (most platforms do this automatically)
- Consider using Cloudflare for additional protection

## Monitoring:
- Check server logs regularly for scammer activity
- Monitor for any actual legitimate users (redirect them away)
- Keep track of IP addresses and patterns

## Legal Considerations:
- Add disclaimer that this is for educational/security research
- Don't actually collect real personal information
- Consider consulting legal advice for your jurisdiction

## Backup Plan:
- Keep repository private until deployment
- Have multiple deployment options ready
- Monitor for takedown requests
