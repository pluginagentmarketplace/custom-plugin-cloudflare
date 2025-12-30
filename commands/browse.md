---
# ═══════════════════════════════════════════════════════════════════════════
# COMMAND: browse
# Version: 2.0.0 | Updated: 2025-01
# ═══════════════════════════════════════════════════════════════════════════
name: browse
description: Explore 65+ developer roadmaps across all technology domains
allowed-tools: Read, Grep, Glob

# ARGUMENTS
argument-hint: "[category|role] - Optional: filter by category or role"

# VALIDATION
validation:
  filter:
    type: string
    pattern: "^[a-zA-Z\\-\\s]+$"
    required: false
    max_length: 30

# EXIT CODES
exit_codes:
  0: Success - Roadmaps displayed
  1: Error - Invalid category
  2: Warning - Category not found, showing all
---

# /browse - Explore 65+ Developer Roadmaps

## Quick Start

```bash
/browse                   # List all roadmaps
/browse frontend          # Frontend roadmaps
/browse languages         # Programming languages
/browse cloud             # Cloud & infrastructure
```

## Roadmap Categories

### Core Development (4)
| Roadmap | Duration | Entry Level |
|---------|----------|-------------|
| **Frontend** | 3-6 mo | Beginner |
| **Backend** | 6-12 mo | Beginner |
| **Full Stack** | 9-15 mo | Beginner |
| **DevOps** | 12-24 mo | Intermediate |

### Languages (9)
| Language | Best For | Learning |
|----------|----------|----------|
| **Python** | AI/ML, Web, Automation | Easy |
| **JavaScript** | Full-stack Web | Medium |
| **TypeScript** | Large Applications | Medium |
| **Java** | Enterprise | Hard |
| **Go** | Cloud, DevOps | Medium |
| **Rust** | Systems, Performance | Very Hard |
| **PHP** | Web, WordPress | Easy |
| **C++** | Games, Systems | Very Hard |
| **Kotlin** | Android, Server | Medium |

### Frameworks (10+)
| Framework | Language | Type |
|-----------|----------|------|
| **React** | JavaScript | Frontend |
| **Next.js** | JavaScript | Full Stack |
| **Vue** | JavaScript | Frontend |
| **Angular** | TypeScript | Frontend |
| **Node.js** | JavaScript | Backend |
| **Spring Boot** | Java | Backend |
| **FastAPI** | Python | Backend |
| **Flutter** | Dart | Mobile |
| **React Native** | JavaScript | Mobile |
| **GraphQL** | Various | API |

### Mobile & Games (5)
| Platform | Language | Duration |
|----------|----------|----------|
| **iOS** | Swift | 6-9 mo |
| **Android** | Kotlin | 6-9 mo |
| **Flutter** | Dart | 4-6 mo |
| **Unity** | C# | 12-24 mo |
| **Unreal** | C++ | 18-36 mo |

### Data & AI (7)
| Role | Focus | Duration |
|------|-------|----------|
| **Data Engineer** | Pipelines, Infra | 12-24 mo |
| **ML Engineer** | Models, Features | 12-24 mo |
| **AI Engineer** | LLMs, Agents | 6-12 mo |
| **Data Analyst** | Insights, BI | 6-12 mo |
| **BI Analyst** | Reporting | 6-12 mo |
| **MLOps** | ML Infrastructure | 12-18 mo |
| **Machine Learning** | Algorithms | 12-24 mo |

### Cloud & Infrastructure (10)
| Technology | Provider | Duration |
|------------|----------|----------|
| **AWS** | Amazon | 3-6 mo |
| **Cloudflare** | Cloudflare | 2-4 wk |
| **GCP** | Google | 3-6 mo |
| **Azure** | Microsoft | 3-6 mo |
| **Docker** | - | 2-4 wk |
| **Kubernetes** | - | 6-8 wk |
| **Terraform** | HashiCorp | 2-3 wk |
| **PostgreSQL** | - | 4-8 wk |
| **MongoDB** | - | 2-4 wk |
| **Redis** | - | 1-2 wk |

### Architecture & Security (12+)
| Topic | Level | Duration |
|-------|-------|----------|
| **System Design** | Advanced | Ongoing |
| **Software Architect** | Senior | 2-5 yr |
| **API Design** | Intermediate | 2-4 wk |
| **Cybersecurity** | Intermediate | 6-12 mo |
| **Blockchain** | Advanced | 6-12 mo |
| **QA Engineering** | Intermediate | 3-6 mo |
| **Computer Science** | Foundational | 2-4 yr |
| **Data Structures** | Foundational | 2-4 mo |
| **Git** | Beginner | 1-2 wk |
| **Bash** | Beginner | 2-4 wk |
| **Linux** | Intermediate | 2-4 mo |
| **SQL** | Beginner | 2-4 wk |

### Emerging Tech & Leadership (8+)
| Path | Focus | Duration |
|------|-------|----------|
| **Prompt Engineering** | LLM Optimization | 2-4 wk |
| **AI Agents** | Autonomous Systems | 4-6 wk |
| **AI Red Teaming** | AI Security | 6-8 wk |
| **Product Manager** | Product Strategy | 3-6 mo |
| **Engineering Manager** | People Leadership | 3-6 mo |
| **DevRel** | Community | 2-3 mo |
| **Technical Writer** | Documentation | 2-3 mo |
| **UX Design** | User Experience | 6-12 mo |

## Roadmap Structure

Each roadmap includes:
```
┌─────────────────────────────────────────┐
│           ROADMAP STRUCTURE              │
├─────────────────────────────────────────┤
│  📚 Foundation                          │
│     └─ Core prerequisites               │
│                                         │
│  🔧 Core Skills                         │
│     └─ Essential expertise              │
│                                         │
│  🚀 Advanced Topics                     │
│     └─ Specialization                   │
│                                         │
│  🛠️ Tools & Technologies               │
│     └─ 2025 recommended stack           │
│                                         │
│  📅 Timeline                            │
│     └─ Learning duration                │
│                                         │
│  📈 Career Path                         │
│     └─ Progression opportunities        │
└─────────────────────────────────────────┘
```

## Related Commands

| Command | Description |
|---------|-------------|
| `/learn [topic]` | Start learning from roadmap |
| `/assess` | Find your position on roadmap |
| `/projects` | Get projects for your level |

## Input Validation

| Input | Valid | Invalid |
|-------|-------|---------|
| `/browse` | ✓ | - |
| `/browse frontend` | ✓ | - |
| `/browse languages` | ✓ | - |
| `/browse @#$` | - | ✗ Special chars |

## Troubleshooting

```
Can't find roadmap?
├─► Use broader category term
├─► Check spelling
└─► Run `/browse` to see all options

Which roadmap to choose?
├─► Define your career goal first
├─► Check job market demand
├─► Match to your interests
└─► Start with core paths (frontend, backend)
```
