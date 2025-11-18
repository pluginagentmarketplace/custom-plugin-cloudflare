# /stack - Technology Stack Selector

This command helps you build a technology stack that fits your project goals and team expertise.

## How to Use

```
/stack                              # Interactive stack builder
/stack [project-type]               # Get recommended stack for project type
/stack compare [stack1] [stack2]    # Compare two stacks
```

## Predefined Stack Templates

### Web Development Stacks

#### 🚀 Modern Full-Stack (Recommended for 2024)
```
Frontend: React/TypeScript + Next.js + Tailwind CSS
Backend: Node.js + NestJS + TypeScript
Database: PostgreSQL
Deployment: Vercel (frontend) + Docker + Kubernetes
Monitoring: Prometheus + Grafana
Cache: Redis
```
- **Best For:** Scalable web applications, SaaS
- **Learning:** Moderate (JavaScript heavy)
- **Performance:** Excellent
- **Community:** Large

#### 🎯 Startup Stack (Fast to MVP)
```
Frontend: Next.js (full-stack)
Backend: APIs via Next.js
Database: PostgreSQL (managed: Supabase)
Auth: Supabase Auth (built-in)
Deployment: Vercel
Database: Supabase (managed PostgreSQL)
```
- **Best For:** MVPs, rapid prototyping
- **Learning:** Beginner-friendly
- **Performance:** Good
- **Cost:** Low (very cheap to start)

#### 🏢 Enterprise Stack
```
Frontend: Angular + TypeScript + RxJS
Backend: Java + Spring Boot
Database: PostgreSQL + Elasticsearch
Message Queue: RabbitMQ
Deployment: Kubernetes
Monitoring: ELK Stack
Auth: OAuth 2.0 + SAML
```
- **Best For:** Large organizations, complex applications
- **Learning:** Steep
- **Performance:** Excellent
- **Security:** Maximum

#### 🎪 Lean Stack (Minimal Dependencies)
```
Frontend: Vue.js + Vite
Backend: Go + Echo
Database: PostgreSQL
Deployment: Docker
```
- **Best For:** Performance-critical, lean teams
- **Learning:** Medium
- **Performance:** Maximum
- **Maintenance:** Minimal

---

### Backend-Only Stacks

#### Python FastAPI Stack
```
Language: Python 3.10+
Framework: FastAPI
Database: PostgreSQL + SQLAlchemy
Async: asyncio + uvicorn
Testing: pytest
Deployment: Docker + Kubernetes
```
- **Best For:** Data science + web, rapid development
- **Performance:** Good
- **Ecosystem:** Excellent (NumPy, Pandas, ML libraries)

#### Node.js/Express Stack
```
Language: JavaScript/TypeScript
Framework: Express or Fastify
Database: MongoDB or PostgreSQL
ORM: Prisma or Sequelize
Testing: Jest
Deployment: Docker + Kubernetes
```
- **Best For:** Real-time apps, full-stack JavaScript
- **Performance:** Good
- **Learning:** Easy for JavaScript devs

#### Go Stack
```
Language: Go
Framework: Gin or Echo
Database: PostgreSQL
Testing: Go testing package
Deployment: Single binary
```
- **Best For:** Microservices, CLI tools, DevOps
- **Performance:** Excellent
- **Deployment:** Simple (single binary)

---

### Mobile Development Stacks

#### iOS Stack
```
Language: Swift 5.5+
UI: SwiftUI
Data: Core Data or Realm
Networking: URLSession + Combine
Testing: XCTest
IDE: Xcode
Deployment: App Store Connect
```

#### Android Stack
```
Language: Kotlin
UI: Jetpack Compose
Data: Room + DataStore
Networking: Retrofit + OkHttp
Async: Coroutines + Flow
Testing: JUnit + Espresso
IDE: Android Studio
Deployment: Google Play Store
```

#### Cross-Platform Stack (Flutter)
```
Language: Dart
UI: Flutter + Material Design
Data: Hive or GetStorage
Networking: http + dio
State: Provider or BLoC
Testing: Flutter test
IDE: VS Code or Android Studio
Deployment: Play Store + App Store
```

---

### Data Science Stack

#### ML/Data Science Stack
```
Language: Python
Data: Pandas + NumPy
Visualization: Matplotlib + Seaborn
ML: scikit-learn or XGBoost
Deep Learning: PyTorch or TensorFlow
Experimentation: Jupyter Notebooks
MLOps: MLflow
Deployment: FastAPI + Docker
```

#### Data Engineering Stack
```
Language: Python/Scala
ETL: Apache Airflow or Prefect
Data Processing: Apache Spark
Database: PostgreSQL + Snowflake
Data Warehouse: BigQuery or Redshift
Monitoring: Great Expectations
IaC: Terraform
```

---

### Cloud-Native Stack

#### AWS-Native Stack
```
Compute: Lambda (serverless) or ECS (containers)
Database: RDS (PostgreSQL) + DynamoDB
Storage: S3
API Gateway: API Gateway
Auth: Cognito
CDN: CloudFront
Monitoring: CloudWatch
IaC: CloudFormation or Terraform
```

#### Kubernetes-Native Stack
```
Container: Docker
Orchestration: Kubernetes
Package Manager: Helm
Ingress: nginx-ingress
Data: PostgreSQL + Redis
Message Queue: RabbitMQ
Monitoring: Prometheus + Grafana
Service Mesh: Istio (optional)
```

#### Cloudflare-First Stack
```
Edge Computing: Cloudflare Workers
Database: D1 (SQLite at edge)
KV Store: Cloudflare KV
Static Site: Cloudflare Pages
CDN: Cloudflare CDN
Security: Cloudflare WAF + DDoS
Domain: Cloudflare DNS
```

---

## Stack Selection Criteria

### Consider These Factors

1. **Team Experience** - Use what you know
2. **Project Timeline** - Prefer simplicity for tight deadlines
3. **Scaling Requirements** - Horizontal? Vertical?
4. **Team Size** - Simple for small, complex for large
5. **Budget** - Consider infrastructure costs
6. **Hiring** - Can you hire developers for this stack?
7. **Maintenance** - How long will you maintain this?
8. **Learning** - Training time for new team members

### Decision Matrix

| Factor | Simple Stack | Modern Stack | Enterprise Stack |
|--------|--------------|--------------|------------------|
| Learning | ⭐⭐ Easy | ⭐⭐⭐ Medium | ⭐⭐⭐⭐ Hard |
| Performance | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐⭐ Excellent |
| Scalability | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Hiring | ⭐⭐⭐⭐ Easy | ⭐⭐⭐⭐ Easy | ⭐⭐⭐ Medium |
| Maintenance | ⭐⭐⭐⭐⭐ Low | ⭐⭐⭐⭐ Low | ⭐⭐ Complex |
| Cost | ⭐⭐⭐⭐ Low | ⭐⭐⭐ Medium | ⭐⭐ High |

## How to Build Your Stack

1. **Define Requirements**
   - What problem are you solving?
   - What's your timeline?
   - What's your budget?

2. **Evaluate Options**
   - What does your team know?
   - What's the market preference?
   - What's the learning curve?

3. **Make Decisions**
   - Choose frontend framework
   - Choose backend language/framework
   - Choose database(s)
   - Choose deployment platform

4. **Document Stack**
   - Create architecture diagram
   - List all technologies
   - Document why each choice
   - Create onboarding guide

5. **Test & Iterate**
   - Build proof of concept
   - Get team feedback
   - Make adjustments if needed
   - Document lessons learned

## Common Stack Combinations

### SaaS Application
```
Frontend: React/TypeScript
Backend: Node.js + NestJS
Database: PostgreSQL
Cache: Redis
Queue: Bull (Redis-based)
Deployment: Docker + Kubernetes
Auth: JWT + OAuth
Payment: Stripe
```

### Real-time Application
```
Frontend: React/Socket.io
Backend: Node.js + Express
Database: MongoDB
Pub/Sub: Redis or RabbitMQ
Deployment: Docker
Caching: Redis
```

### Microservices Architecture
```
Services: Each in Go or Node.js
API Gateway: Kong or Traefik
Message Queue: RabbitMQ or Kafka
Database: PostgreSQL (per service)
Container: Docker
Orchestration: Kubernetes
Service Mesh: Istio
Monitoring: Prometheus + Grafana
```

## Anti-Patterns to Avoid

❌ **Over-engineering:** Don't use Kubernetes for a single service
❌ **Cargo-cult programming:** Don't copy without understanding
❌ **Shiny object syndrome:** Don't switch every new tool
❌ **Under-engineering:** Don't ignore scalability from day 1
❌ **Wrong language for the job:** Don't force Java for a CLI tool
❌ **Ignoring team expertise:** Don't choose a stack nobody knows

---

Want expert guidance? Consult:
- **Language & Framework Specialist** for component selection
- **Cloud & Infrastructure Expert** for deployment options
- **Architecture & Security Specialist** for design patterns
