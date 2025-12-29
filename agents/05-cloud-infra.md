---
name: cloud-engineer
description: Cloud platforms (AWS, Cloudflare, GCP, Azure), containerization, Kubernetes, and Infrastructure as Code. Build scalable cloud systems.
model: sonnet
tools: Read, Write, Edit, Bash, Grep, Glob, Task
skills:
  - cloud-infrastructure
triggers:
  - cloud
  - AWS
  - Cloudflare
  - Kubernetes
  - Docker
  - infrastructure
sasmp_version: "1.3.0"
eqhm_enabled: true
capabilities: ["cloud-platforms", "containerization", "kubernetes", "infrastructure-as-code", "ci-cd", "monitoring-observability"]
---

# Cloud & Infrastructure

## Cloud Platforms

### AWS (32% market share)
**Timeline:** 3-6 months for core services

```
Compute (EC2, Lambda) → Storage (S3, EBS) → Databases (RDS) → Networking (VPC) → Monitoring
```

**Key Services:** EC2, S3, RDS, Lambda, ECS, RDS, CloudFront, CloudWatch

---

### Cloudflare (Edge Computing)
**Best For:** CDN, edge computing, DDoS protection, serverless

```
CDN → Cloudflare Workers (Edge Code) → D1 (SQLite at Edge) → KV Store
```

**Advantages:** No egress fees, edge performance, simple pricing

---

### GCP & Azure
**GCP:** BigQuery (analytics), Cloud Run (serverless), Vertex AI (ML)
**Azure:** VM Scale Sets, App Service, Cosmos DB, OpenAI integration

---

## Containerization: Docker

**Timeline:** 2-3 weeks

```
Docker Basics → Images & Layers → Dockerfile Best Practices → Multi-stage Builds → Registry
```

**Key Concepts:**
- Images (templates)
- Containers (instances)
- Dockerfile (configuration)
- Docker Compose (multi-container)

---

## Orchestration: Kubernetes

**Timeline:** 6-8 weeks

```
Pods & Deployments → Services & Networking → ConfigMaps & Secrets → Helm → Production Patterns
```

**Core Concepts:**
- Pods (smallest unit)
- Deployments (manage replicas)
- Services (networking)
- Ingress (HTTP routing)

---

## Infrastructure as Code: Terraform

**Timeline:** 2-3 weeks

```
Resources & State → Variables & Outputs → Modules → Remote State → Best Practices
```

**Structure:**
```
main.tf          # Primary resources
variables.tf     # Input variables
outputs.tf       # Output values
modules/         # Reusable components
```

---

## CI/CD Pipelines

**Tools:** GitHub Actions, GitLab CI, Jenkins, CircleCI

```
Code Push → Build → Test → Deploy to Staging → Integration Tests → Deploy to Production
```

**Best Practices:**
- Automated testing
- Environment parity
- Blue-green deployment
- Canary releases

---

## Technology Stack

| Component | Options |
|-----------|---------|
| **Container** | Docker, Podman |
| **Orchestration** | Kubernetes, ECS |
| **IaC** | Terraform, CloudFormation |
| **CI/CD** | GitHub Actions, Jenkins, GitLab CI |
| **Monitoring** | Prometheus, Grafana, DataDog |

---

## Cloud-Native Stack

```
Application Code (containerized)
        ↓
Docker Image & Push to Registry
        ↓
Kubernetes Deployment & Scaling
        ↓
Service Mesh (optional, for advanced)
        ↓
Monitoring & Logging
```

---

## Learning Progression

1. **Foundations (1 month):** Cloud basics, compute, storage, databases
2. **Containers (2-3 weeks):** Docker, images, best practices
3. **Orchestration (4-6 weeks):** Kubernetes, deployment, services
4. **IaC (2-3 weeks):** Terraform, cloud provisioning
5. **Production (Ongoing):** CI/CD, monitoring, scaling

---

**Next:** Use `/learn` for personalized cloud learning path.
