---
name: system-design
description: System design, software architecture, API design, cybersecurity, and threat modeling. Build secure, scalable systems at scale.
---

# System Design & Architecture

## System Design Fundamentals

### Scalability
```
Single Server → Load Balancer → Multiple Servers → Caching (Redis) → Read Replicas → Sharding
```

**Vertical:** Increase server resources
**Horizontal:** Add more servers

---

### High Availability
- **Redundancy:** Eliminate single points of failure
- **Load Balancing:** Distribute traffic
- **Replication:** Master-slave, master-master
- **Auto-failover:** Automatic recovery
- **Multi-region:** Geographic distribution

---

## Architecture Patterns

| Pattern | Best For | Complexity | Scaling |
|---------|----------|-----------|---------|
| **Monolith** | Startups | Low | Limited |
| **Microservices** | Large teams | High | Excellent |
| **Serverless** | Event-driven | Medium | Auto |
| **Hybrid** | Flexible | High | Mixed |

---

## API Design

### REST Best Practices
```
GET /api/users              # List
GET /api/users/{id}         # Get
POST /api/users             # Create
PUT /api/users/{id}         # Update
DELETE /api/users/{id}      # Delete
```

**Status Codes:** 2xx Success, 4xx Client Error, 5xx Server Error

**Versioning:** /api/v1/, /api/v2/

---

## Database Selection

| Use Case | Best Choice |
|----------|-------------|
| **Transactions** | PostgreSQL, MySQL |
| **Scaling Reads** | Redis, DynamoDB |
| **Analytics** | BigQuery, Snowflake |
| **Full-Text Search** | Elasticsearch |
| **Real-time** | Redis, Kafka |

---

## Cybersecurity Essentials

### OWASP Top 10

1. **Access Control** - Verify authorization
2. **Cryptographic Failures** - Encrypt sensitive data
3. **Injection** - Use parameterized queries
4. **Insecure Design** - Threat modeling
5. **Security Misconfiguration** - Change defaults
6. **Vulnerable Components** - Update dependencies
7. **Authentication Failures** - MFA, rate limiting
8. **Data Integrity Issues** - Verify origins
9. **Logging Failures** - Track events
10. **SSRF** - Validate URLs

---

### Encryption

**At Rest:** AES-256
**In Transit:** TLS 1.2+, HTTPS everywhere
**Passwords:** bcrypt, Argon2

---

### Authentication Methods

- **OAuth 2.0** - Delegated authorization
- **JWT** - Stateless tokens
- **MFA** - Multi-factor authentication
- **SAML** - Enterprise SSO

---

## Threat Modeling: STRIDE

- **S**poofing - Identity fraud
- **T**ampering - Data modification
- **R**epudiation - Deny actions
- **I**nformation Disclosure - Privacy breach
- **D**enial of Service - Availability
- **E**levation of Privilege - Unauthorized access

---

## Compliance

- **GDPR** - EU data protection
- **HIPAA** - Healthcare data
- **SOC 2** - Service security
- **PCI DSS** - Payment card data

---

## Disaster Recovery

**RTO:** Recovery Time Objective
**RPO:** Recovery Point Objective
**Backup:** Multiple locations, immutable
**Failover:** Active-active, blue-green

---

**Use `/learn` for system design guidance.**
