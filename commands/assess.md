---
# ═══════════════════════════════════════════════════════════════════════════
# COMMAND: assess
# Version: 2.0.0 | Updated: 2025-01
# ═══════════════════════════════════════════════════════════════════════════
name: assess
description: Evaluate skills, identify gaps, and track learning progress
allowed-tools: Read, Grep, Glob, Task

# ARGUMENTS
argument-hint: "[topic|progress] - Optional: specific skill or 'progress'"

# VALIDATION
validation:
  topic:
    type: string
    pattern: "^[a-zA-Z\\-\\s]+$"
    required: false
    max_length: 50

# EXIT CODES
exit_codes:
  0: Success - Assessment completed
  1: Error - Invalid topic
  2: Warning - Partial assessment (some areas skipped)
---

# /assess - Evaluate Skills & Track Progress

## Quick Start

```bash
/assess                   # Full skill assessment
/assess javascript        # Assess JavaScript specifically
/assess react             # Assess React knowledge
/assess progress          # View learning progress
```

## Assessment Modes

| Mode | Command | Description |
|------|---------|-------------|
| **Full** | `/assess` | Complete skill evaluation |
| **Topic** | `/assess [topic]` | Single skill deep-dive |
| **Progress** | `/assess progress` | Track learning over time |

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    /assess WORKFLOW                              │
├─────────────────────────────────────────────────────────────────┤
│  1. SKILL MAPPING                                                │
│     └─ Identify all skills for your path                        │
│                                                                  │
│  2. EVALUATION                                                   │
│     ├─ Self-assessment questions                                │
│     ├─ Problem-solving challenges                               │
│     └─ Concept verification                                     │
│                                                                  │
│  3. SCORING                                                      │
│     ├─ Overall score (0-100)                                    │
│     ├─ Category breakdown                                       │
│     └─ Weakness identification                                  │
│                                                                  │
│  4. RECOMMENDATIONS                                              │
│     ├─ Priority learning areas                                  │
│     ├─ Resources for improvement                                │
│     └─ Timeline estimates                                       │
└─────────────────────────────────────────────────────────────────┘
```

## Skill Levels

| Level | Score | Description |
|-------|-------|-------------|
| **Novice** | 0-25 | Just starting, need guidance |
| **Beginner** | 25-50 | Basic understanding |
| **Intermediate** | 50-75 | Can build projects |
| **Advanced** | 75-90 | Deep expertise |
| **Expert** | 90-100 | Industry-leading |

## Example Output

```
JavaScript Assessment: 65/100 (Intermediate)
├─ ES6+ Syntax:      75/100 ✓ Strong
├─ Promises/Async:   45/100 ✗ Weak
├─ DOM Manipulation: 70/100 ✓ Good
└─ Event Handling:   65/100 ◐ Moderate

React Assessment: 60/100 (Intermediate)
├─ Components:       75/100 ✓ Strong
├─ Hooks:            50/100 ✗ Weak
├─ State Management: 45/100 ✗ Weak
└─ Performance:      55/100 ◐ Moderate

Priority Actions:
1. Deep-dive Promises and async/await
2. Master React hooks (useState, useEffect, useContext)
3. Learn Zustand or TanStack Query for state
4. Build 3 medium-complexity projects

Estimated Time to Advanced: 8-12 weeks
```

## Assessment Categories

### By Role
| Role | Skills Assessed |
|------|-----------------|
| **Frontend** | HTML/CSS, JavaScript, Framework, Testing |
| **Backend** | Language, Framework, Database, APIs |
| **DevOps** | Linux, Docker, Kubernetes, Cloud |
| **Data/ML** | SQL, Python, Statistics, ML algorithms |
| **Mobile** | Platform (iOS/Android), Framework, State |

### By Topic
| Topic | Sub-Skills |
|-------|------------|
| **JavaScript** | ES6+, Async, DOM, Events, Modules |
| **React** | Components, Hooks, State, Performance |
| **Python** | Syntax, Libraries, OOP, Testing |
| **Docker** | Images, Containers, Compose, Networks |

## Progress Tracking

```
Learning Progress:
├─ Current Streak:    14 days 🔥
├─ Total Hours:       127 hours
├─ Skills Mastered:   12/24
├─ Projects Completed: 5
└─ Current Milestone: Intermediate Frontend

History:
├─ Week 1: JavaScript 45 → 55 (+10)
├─ Week 2: React 40 → 52 (+12)
├─ Week 3: React 52 → 60 (+8)
└─ Week 4: JavaScript 55 → 65 (+10)
```

## Input Validation

| Input | Valid | Invalid |
|-------|-------|---------|
| `/assess` | ✓ | - |
| `/assess javascript` | ✓ | - |
| `/assess progress` | ✓ | - |
| `/assess 123` | - | ✗ Numbers only |

## Best Practices

1. **Be honest** - Self-assess accurately
2. **Actually solve** - Don't guess answers
3. **Reassess regularly** - Every 4 weeks
4. **Focus on weaknesses** - Priority improvement
5. **Build projects** - Reinforce learning

## Related Commands

| Command | Use After |
|---------|-----------|
| `/learn` | Get guidance on weak areas |
| `/projects` | Find projects to practice |
| `/browse` | Explore learning paths |

## Troubleshooting

```
Score seems wrong?
├─► Be more honest in self-assessment
├─► Actually try the challenges
└─► Score reflects current ability, not potential

Not improving?
├─► Are you actively practicing? (not just reading)
├─► Focus on weakest areas first
├─► Build projects, not just tutorials
└─► Reassess in 2-4 weeks, not days
```
