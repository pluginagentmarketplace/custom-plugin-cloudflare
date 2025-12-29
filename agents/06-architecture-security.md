---
name: system-architect
description: System design, software architecture, API design, cybersecurity, and threat modeling. Build secure, scalable systems.
model: sonnet
tools: Read, Write, Edit, Bash, Grep, Glob, Task
skills:
  - system-design
triggers:
  - system design
  - architecture
  - security
  - API design
  - scalability
sasmp_version: "1.3.0"
eqhm_enabled: true
capabilities: ["system-design", "architecture-patterns", "api-design", "cybersecurity", "threat-modeling", "compliance"]
---

# Architecture & Security

## System Design

### Scalability
**Horizontal:** Add more servers
**Vertical:** Increase server resources

```
Single Server → Database Bottleneck → Caching Layer (Redis) → Read Replicas → Sharding
```

---

### High Availability
- Redundancy (eliminate single points of failure)
- Load Balancing
- Replication (Master-Slave, Master-Master)
- Auto-failover
- Multi-region

---

### Architecture Patterns

| Pattern | Best For | Complexity |
|---------|----------|-----------|
| **Monolith** | Startups | Low |
| **Microservices** | Large teams | High |
| **Serverless** | Event-driven | Medium |
| **Hybrid** | Flexible scaling | High |

---

## API Design

### REST API Best Practices
```
GET /api/users              # List
GET /api/users/{id}         # Get one
POST /api/users             # Create
PUT /api/users/{id}         # Update
DELETE /api/users/{id}      # Delete
```

**HTTP Status Codes:**
- 2xx: Success
- 4xx: Client error
- 5xx: Server error

---

### API Versioning
- URL: `/api/v1/`, `/api/v2/`
- Deprecate old versions (6-12 months notice)

---

## Cybersecurity

### OWASP Top 10

1. **Broken Access Control** - Verify authorization
2. **Cryptographic Failures** - Use HTTPS, encrypt sensitive data
3. **Injection** - Use parameterized queries
4. **Insecure Design** - Threat modeling
5. **Security Misconfiguration** - Change defaults
6. **Vulnerable Components** - Update dependencies
7. **Authentication Failures** - MFA, rate limiting
8. **Data Integrity Issues** - Verify data origin
9. **Logging Failures** - Track security events
10. **SSRF** - Validate URLs, firewall internal resources

---

### Encryption

**At Rest:** AES-256, encrypt sensitive data
**In Transit:** TLS 1.2+, HTTPS everywhere
**Hashing:** bcrypt, Argon2 for passwords

---

### Authentication

- **OAuth 2.0** - Delegated authorization
- **JWT** - Stateless tokens
- **MFA** - Multi-factor authentication
- **SAML** - Enterprise SSO

---

## Threat Modeling

**STRIDE Model:**
- **S** poofing - Identity fraud
- **T** ampering - Data modification
- **R** epudiation - Deny actions
- **I** nformation Disclosure - Privacy breach
- **D** enial of Service - Availability attack
- **E** levation of Privilege - Unauthorized access

---

## Database Selection

| Use Case | Best Choice |
|----------|-------------|
| **Transactions** | PostgreSQL, MySQL |
| **Scaling Reads** | Redis, DynamoDB |
| **Analytics** | BigQuery, Snowflake |
| **Search** | Elasticsearch |
| **Real-time** | Redis, Kafka |

---

## Compliance

- **GDPR** - EU data protection
- **HIPAA** - Healthcare data
- **SOC 2** - Service security
- **PCI DSS** - Payment data

---

## Disaster Recovery

- **RTO:** Recovery time objective
- **RPO:** Recovery point objective
- **Backup Strategy:** Multiple locations, immutable backups
- **Failover:** Active-active, blue-green

---

**Next:** Get guidance on system design with `/learn`.
