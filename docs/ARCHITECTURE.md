# System Architecture

## Core Components

```
Commands Layer (/learn, /browse, /assess, /projects)
         ↓
Agent Selection & Matching
         ↓
7 Specialist Agents (Domain Expertise)
         ↓
7 Skill Modules (Detailed Guidance)
         ↓
Content Layer (65+ Roadmaps, Examples, Tools)
         ↓
Hooks & Analytics (Tracking, Personalization)
```

## Agent-Skill Alignment (100%)

| Agent | Skill | Focus | Coverage |
|-------|-------|-------|----------|
| Core Paths | Core Development | Frontend/Backend/Full-Stack/DevOps | 4 paths |
| Languages | Languages & Frameworks | 9 languages, 10+ frameworks | 19 paths |
| Mobile/Games | Mobile Development | iOS/Android/Flutter/Unity/Unreal | 5 paths |
| Data & AI | Data Engineering | Data Eng/ML/AI/MLOps/LLMs | 7 paths |
| Cloud/Infra | Cloud Infrastructure | AWS/K8s/Docker/Terraform/Cloud | 10 paths |
| Architecture | System Design | Design/Security/APIs/Compliance | 12+ paths |
| Emerging/Lead | Emerging Tech | PM/Manager/DevRel/UX/AI-Agents | 8+ paths |

## Data Flow

```
User Input (/learn)
  ↓
Assess Goals & Experience
  ↓
Match Best Agent
  ↓
Generate Personalized Path
  ↓
Link to Skills
  ↓
Provide Resources & Projects
  ↓
Track Progress
  ↓
Celebrate Milestones
```

## Scaling Strategy

- **Horizontal:** Stateless agents, cacheable content
- **Vertical:** Modular skills, lazy-loading, efficient hooks
- **Performance Target:** <500ms total user interaction

## Security

- ✅ No tracking or data collection
- ✅ GDPR compliant
- ✅ No external APIs required
- ✅ Open-source, auditable

---

**Version:** 1.0.0 | **Status:** Production Ready
