---
# ═══════════════════════════════════════════════════════════════════════════
# COMMAND: learn
# Version: 2.0.0 | Updated: 2025-01
# ═══════════════════════════════════════════════════════════════════════════
name: learn
description: Start personalized learning journey with AI-guided roadmaps
allowed-tools: Read, Grep, Glob, Task

# ARGUMENTS
argument-hint: "[topic] - Optional: specific topic to learn"

# VALIDATION
validation:
  topic:
    type: string
    pattern: "^[a-zA-Z\\-\\s]+$"
    required: false
    max_length: 50

# EXIT CODES
exit_codes:
  0: Success - Learning path generated
  1: Error - Invalid topic specified
  2: Warning - Topic not found, showing alternatives
---

# /learn - Start Your Learning Journey

## Quick Start

```bash
/learn                    # Interactive path selection
/learn frontend           # Start frontend path
/learn python             # Learn Python
/learn kubernetes         # Learn Kubernetes
```

## Available Paths

| Path | Command | Duration | Skill Level |
|------|---------|----------|-------------|
| **Frontend** | `/learn frontend` | 3-6 mo | Beginner |
| **Backend** | `/learn backend` | 6-12 mo | Beginner |
| **Full Stack** | `/learn fullstack` | 9-15 mo | Beginner |
| **DevOps** | `/learn devops` | 12-24 mo | Intermediate |
| **Mobile** | `/learn mobile` | 6-12 mo | Beginner |
| **AI/ML** | `/learn ml` | 12-24 mo | Intermediate |
| **AI Agents** | `/learn ai-agents` | 4-6 wk | Intermediate |
| **Cloud** | `/learn aws` | 3-6 mo | Intermediate |

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     /learn WORKFLOW                              │
├─────────────────────────────────────────────────────────────────┤
│  1. SELECT PATH                                                  │
│     └─ Choose from 7 main paths or 65+ specific topics          │
│                                                                  │
│  2. PERSONALIZATION                                              │
│     ├─ Current experience level                                  │
│     ├─ Time available per week                                   │
│     └─ Career goals                                              │
│                                                                  │
│  3. ROADMAP GENERATION                                           │
│     ├─ Step-by-step learning sequence                           │
│     ├─ 2024-2025 recommended resources                          │
│     ├─ Project ideas for each stage                             │
│     └─ Timeline to job-readiness                                │
│                                                                  │
│  4. AGENT MATCHING                                               │
│     └─ Connected to specialist agent for ongoing guidance       │
└─────────────────────────────────────────────────────────────────┘
```

## Example Roadmaps

### Frontend (3-6 months)
```
HTML/CSS (2-3 wk) → JavaScript (4-6 wk) → React 19 (4-6 wk) → Testing (2-4 wk) → Deploy (1-2 wk)
```

### Backend (6-12 months)
```
Python (4-6 wk) → FastAPI (4-6 wk) → PostgreSQL (3-4 wk) → APIs (3-4 wk) → Deploy (2-4 wk)
```

### AI Agents (4-6 weeks)
```
LLM Basics (1 wk) → Tool Calling (1 wk) → Agent Loop (2 wk) → Production (ongoing)
```

## Input Validation

| Input | Valid | Invalid |
|-------|-------|---------|
| `/learn frontend` | ✓ | - |
| `/learn react-19` | ✓ | - |
| `/learn kubernetes` | ✓ | - |
| `/learn @#$%` | - | ✗ Special chars |
| `/learn` | ✓ (interactive) | - |

## Related Commands

| Command | Description |
|---------|-------------|
| `/assess` | Evaluate current skills first |
| `/projects` | Find projects for your level |
| `/browse` | Explore all 65+ roadmaps |

## Troubleshooting

```
Path not found?
├─► Check spelling
├─► Try broader term (e.g., "frontend" not "react-components")
└─► Use `/browse` to see all available paths

Not sure where to start?
├─► Run `/assess` to find your level
├─► Start with core path (frontend, backend, etc.)
└─► Don't overthink - pick one and start today
```
