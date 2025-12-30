---
# ═══════════════════════════════════════════════════════════════════════════
# COMMAND: projects
# Version: 2.0.0 | Updated: 2025-01
# ═══════════════════════════════════════════════════════════════════════════
name: projects
description: Discover portfolio projects appropriate for your skill level and career path
allowed-tools: Read, Grep, Glob

# ARGUMENTS
argument-hint: "[level|category] - Optional: beginner/intermediate/advanced or category"

# VALIDATION
validation:
  filter:
    type: string
    pattern: "^[a-zA-Z\\-\\s]+$"
    required: false
    max_length: 30
    enum: [beginner, intermediate, advanced, frontend, backend, fullstack, mobile, games, data, ml, ai, devops]

# EXIT CODES
exit_codes:
  0: Success - Projects displayed
  1: Error - Invalid filter
  2: Warning - Filter not found, showing all
---

# /projects - Discover Project Ideas

## Quick Start

```bash
/projects                  # Show all projects
/projects beginner         # Beginner-level projects
/projects intermediate     # Intermediate projects
/projects frontend         # Frontend projects
/projects ml               # Machine learning projects
```

## Projects by Level

### Beginner (0-3 months)
**Goal:** Learn fundamentals, complete first projects

| Project | Skills | Time |
|---------|--------|------|
| **Todo App** | CRUD, State | 1-2 wk |
| **Calculator** | JavaScript logic | 1 wk |
| **Weather App** | API integration | 1-2 wk |
| **Quiz App** | DOM manipulation | 1-2 wk |
| **Portfolio Site** | HTML/CSS | 1-2 wk |

### Intermediate (3-12 months)
**Goal:** Build complete applications

| Project | Skills | Time |
|---------|--------|------|
| **E-commerce UI** | Components, State | 2-4 wk |
| **Real-time Chat** | WebSockets, Auth | 3-4 wk |
| **Blog Platform** | Full Stack, CMS | 4-6 wk |
| **Dashboard** | Data viz, APIs | 2-3 wk |
| **Task Manager** | CRUD, Database | 2-3 wk |

### Advanced (1+ years)
**Goal:** Production-ready systems

| Project | Skills | Time |
|---------|--------|------|
| **SaaS Platform** | Multi-tenant, Payments | 3-6 mo |
| **Microservices** | Distributed systems | 2-4 mo |
| **ML Pipeline** | MLOps, Production | 2-3 mo |
| **Multiplayer Game** | Networking, Real-time | 3-6 mo |
| **AI Agent System** | LLM, Tool calling | 1-2 mo |

## Projects by Category

### Frontend
```
Beginner:
├─ Todo App (HTML/CSS/JS)
├─ Portfolio Website
└─ Calculator

Intermediate:
├─ E-commerce Product Page (React)
├─ Social Media Feed
├─ Admin Dashboard
└─ Real-time Chat UI

Advanced:
├─ Design System Library
├─ Micro-frontend Architecture
└─ Performance-optimized SPA
```

### Backend
```
Beginner:
├─ REST API (User CRUD)
├─ Simple Blog API
└─ URL Shortener

Intermediate:
├─ E-commerce Backend
├─ Authentication System
├─ Real-time Notifications
└─ File Upload Service

Advanced:
├─ GraphQL Federation
├─ Event-driven Architecture
└─ High-throughput API
```

### Full Stack
```
Beginner:
├─ Blog Platform
├─ Note-taking App
└─ Budget Tracker

Intermediate:
├─ Project Management Tool
├─ E-commerce Store
├─ Booking System
└─ Social Platform MVP

Advanced:
├─ Multi-tenant SaaS
├─ Real-time Collaboration
└─ Marketplace Platform
```

### Mobile
```
Beginner:
├─ Todo List App
├─ Weather App
└─ Calculator

Intermediate:
├─ Photo Gallery
├─ News Reader
├─ Expense Tracker
└─ Chat App

Advanced:
├─ Social Media App
├─ E-commerce App
└─ Fitness Tracking App
```

### Games
```
Beginner:
├─ Tic-Tac-Toe
├─ Pong Clone
└─ Snake Game

Intermediate:
├─ 2D Platformer
├─ Tower Defense
├─ Puzzle Game
└─ Endless Runner

Advanced:
├─ 3D Adventure Game
├─ Multiplayer Battle Arena
└─ Open World RPG
```

### Data/ML
```
Beginner:
├─ Data Analysis (Pandas)
├─ Visualization Dashboard
└─ CSV Processor

Intermediate:
├─ Classification Model
├─ Recommendation System
├─ Sentiment Analysis
└─ Time Series Forecast

Advanced:
├─ RAG Chatbot
├─ AI Agent with Tools
├─ ML Pipeline (MLflow)
└─ Multi-Agent System
```

### DevOps
```
Beginner:
├─ Containerize an App
├─ CI Pipeline Setup
└─ Basic Monitoring

Intermediate:
├─ Kubernetes Deployment
├─ IaC with Terraform
├─ Multi-stage CI/CD
└─ Log Aggregation

Advanced:
├─ Service Mesh
├─ Multi-cloud Setup
└─ GitOps Implementation
```

## Project Selection Guide

```
How to choose?
│
├─► What's your current level?
│   ├─ New to programming → Beginner projects
│   ├─ Can build basic apps → Intermediate projects
│   └─ Building production systems → Advanced projects
│
├─► What's your goal?
│   ├─ Get first job → 3-5 intermediate projects
│   ├─ Level up skills → Mix of intermediate + advanced
│   └─ Career change → Focus on target role projects
│
└─► How much time?
    ├─ 1-2 weeks → Single feature projects
    ├─ 1-2 months → Complete applications
    └─ 3+ months → Full systems
```

## Project Checklist

For every project:
- [ ] Define clear requirements
- [ ] Build MVP first
- [ ] Add testing
- [ ] Deploy live
- [ ] Write README
- [ ] Push to GitHub
- [ ] Share on LinkedIn

## Related Commands

| Command | Description |
|---------|-------------|
| `/learn` | Get guidance while building |
| `/assess` | Verify skills after completion |
| `/browse` | Find related learning paths |

## Troubleshooting

```
Don't know which project?
├─► Start with classic: Todo App
├─► Match to job descriptions in your target role
└─► Ask: "Would I use this?" If yes, build it

Project too hard?
├─► Break into smaller pieces
├─► Build simpler version first
├─► Use `/learn` for help with specific parts
└─► It's okay to struggle - that's learning

Project too easy?
├─► Add more features
├─► Add testing (unit, integration)
├─► Add authentication, authorization
└─► Move to next level
```

## Tips for Success

1. **Finish what you start** - Incomplete projects don't count
2. **Deploy everything** - Live demos impress employers
3. **Document well** - README, comments, screenshots
4. **Build in public** - Share progress on Twitter/LinkedIn
5. **Iterate** - V1 → V2 → V3 shows growth
