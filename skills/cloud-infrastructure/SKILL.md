---
name: cloud-infrastructure
description: Cloud platforms (AWS, Cloudflare, GCP, Azure), containerization (Docker), Kubernetes, Infrastructure as Code (Terraform), CI/CD, and observability.
---

# Cloud & Infrastructure

## Cloud Platforms

| Platform | Market | Best For | Timeline |
|----------|--------|----------|----------|
| **AWS** | 32% | Compute, Storage, Databases | 3-6 mo |
| **Cloudflare** | Edge | CDN, Workers, Edge Computing | 2-4 weeks |
| **GCP** | 11% | Analytics, ML, Data | 3-6 mo |
| **Azure** | 24% | Enterprise, Microsoft Stack | 3-6 mo |

---

## AWS Core Learning Path

```
Compute (EC2, Lambda) → Storage (S3) → Databases (RDS) → Networking (VPC) → Monitoring
```

**Key Services:** EC2, S3, RDS, Lambda, IAM, CloudWatch, CloudFront

**Timeline:** 3-6 months for job-readiness

---

## Docker & Containerization

```
Docker Basics → Images & Layers → Dockerfile → Multi-stage Builds → Registry → Optimization
```

**Timeline:** 2-3 weeks

**Key Concepts:**
- Images (templates)
- Containers (instances)
- Dockerfile (configuration)
- Docker Compose (multi-container)

---

## Kubernetes Orchestration

```
Pods → Deployments → Services → ConfigMaps/Secrets → Helm → Production Patterns
```

**Timeline:** 6-8 weeks

**Core:** Pods, Deployments, Services, Ingress, StatefulSets

---

## Infrastructure as Code: Terraform

```
Resources & State → Variables & Outputs → Modules → Remote State → Best Practices
```

**Timeline:** 2-3 weeks

**Structure:**
```
main.tf           # Resources
variables.tf      # Inputs
outputs.tf        # Outputs
modules/          # Reusable components
environments/     # dev, staging, prod
```

---

## CI/CD Pipelines

```
Code Push → Build → Test → Deploy Staging → Integration Tests → Deploy Production
```

**Tools:** GitHub Actions, GitLab CI, Jenkins, CircleCI

**Best Practices:**
- Automated testing
- Blue-green deployment
- Canary releases
- Monitoring & alerts

---

## Cloud-Native Stack

```
Application (containerized)
        ↓
Docker Image & Push
        ↓
Kubernetes Deploy
        ↓
CI/CD Pipeline Automation
        ↓
Monitoring & Logging
```

---

## Technology Choices

| Component | Options |
|-----------|---------|
| **Container** | Docker, Podman |
| **Orchestration** | Kubernetes, ECS |
| **IaC** | Terraform, CloudFormation |
| **CI/CD** | GitHub Actions, Jenkins, GitLab CI |
| **Monitoring** | Prometheus, Grafana, DataDog |

---

## Learning Timeline

1. **Cloud Fundamentals (1 month):** Services, compute, storage
2. **Containers (2-3 weeks):** Docker, images, best practices
3. **Orchestration (4-6 weeks):** Kubernetes, deployments
4. **IaC (2-3 weeks):** Terraform, provisioning
5. **Production (Ongoing):** CI/CD, monitoring, scaling

---

## Best Practices

- Infrastructure as Code (version control)
- Immutable infrastructure
- Environment parity
- Automated deployments
- Continuous monitoring

---

**Use `/learn` for cloud infrastructure guidance.**
