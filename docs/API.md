# API Reference

## Commands API

### `/learn`
**Purpose:** Start personalized learning journey

**Parameters:**
```
Optional: [role-name]  # Specific role to learn
```

**Response:**
```
Personalized roadmap:
├─ Goal: [User's learning goal]
├─ Duration: [Timeline to proficiency]
├─ Agent: [Matched specialist agent]
├─ Stack: [Recommended tech stack]
├─ Projects: [Portfolio project ideas]
└─ Next Steps: [Immediate actions]
```

**Examples:**
```
/learn                           # Interactive wizard
/learn backend-developer         # Specific path
/learn machine-learning-engineer # ML specialization
```

---

### `/browse`
**Purpose:** Explore all 65+ developer roadmaps

**Parameters:**
```
Optional: [category|role|keyword]  # Filter results
```

**Response:**
```
Available roadmaps:
├─ Total: 65+
├─ By Category: [Categories listed]
├─ By Level: [Beginner/Intermediate/Advanced]
├─ Selected Roadmap:
│  ├─ Overview
│  ├─ Skills Required
│  ├─ Timeline
│  ├─ Tools & Tech
│  └─ Career Prospects
```

**Examples:**
```
/browse                   # All roadmaps
/browse backend          # Backend-related paths
/browse kubernetes       # Specific technology
/browse data-science     # Career specialization
```

---

### `/assess`
**Purpose:** Evaluate skills and track progress

**Parameters:**
```
Optional: [skill|role|category]  # Specific assessment
```

**Response:**
```
Assessment Results:
├─ Current Score: [0-100]
├─ Category Breakdown:
│  ├─ [Category]: [Score]
│  ├─ [Category]: [Score]
│  └─ ...
├─ Identified Weaknesses: [Areas to improve]
├─ Strengths: [Strong areas]
├─ Improvement Timeline: [Estimated time]
└─ Recommended Actions: [Next steps]
```

**Examples:**
```
/assess                        # Full assessment
/assess backend-development   # Role-specific
/assess python               # Language assessment
/assess progress             # View progress tracking
```

---

### `/projects`
**Purpose:** Discover portfolio project ideas

**Parameters:**
```
Optional: [level|category|skill]  # Filter projects
```

**Response:**
```
Project Recommendations:
├─ Current Level: [Beginner/Intermediate/Advanced]
├─ Project Ideas:
│  ├─ Project 1: [Name]
│  │  ├─ Duration: [Timeline]
│  │  ├─ Skills: [Required skills]
│  │  ├─ Tech Stack: [Technologies]
│  │  └─ Value: [Portfolio impact]
│  └─ ...
├─ Learning Outcomes: [What you'll learn]
└─ Next Level: [After completing projects]
```

**Examples:**
```
/projects                    # All project ideas
/projects beginner          # Beginner-friendly
/projects react             # Tech-specific
/projects full-stack        # Role-specific
```

---

## Agent API

### Agent Interface
```markdown
---
id: agent-id
name: Agent Name
description: What this agent specializes in
capabilities: ["capability1", "capability2"]
expertise: ["skill1", "skill2"]
---

# Agent Name
[Markdown content with guidance]
```

### Agent Selection
```
Plugin automatically selects agent based on:
├─ User goal from /learn
├─ Keyword matching in /browse
├─ Assessment results from /assess
└─ Project selection from /projects
```

### Agent Switching
```
User can switch between agents for:
├─ Different aspects of same goal
├─ Deeper expertise in sub-domain
├─ Cross-domain learning
└─ Specialized guidance
```

---

## Skill API

### Skill Format
```markdown
---
name: skill-id              # Max 64 chars, lowercase, hyphens
description: [Detailed]    # Max 1024 chars
---

# Skill Name
[Content with examples]
```

### Skill Triggers
```
Automatically loaded when user mentions:
├─ Keywords (python, react, kubernetes)
├─ Concepts (frontend, backend, devops)
├─ Tools (docker, terraform, azure)
└─ Goals (learn, master, improve)
```

### Skill Levels
```
- Beginner (0-25%): Just starting
- Intermediate (25-75%): Building skills
- Advanced (75-100%): Expert level
```

### Skill Prerequisites
```json
{
  "id": "skill-id",
  "prerequisites": [
    "prerequisite-skill-1",
    "prerequisite-skill-2"
  ]
}
```

---

## Hook API

### Hook Structure
```json
{
  "name": "hook-name",
  "trigger": "event-type",
  "triggerValue": "specific-value",
  "actions": [
    {
      "type": "action-type",
      "parameters": {}
    }
  ],
  "enabled": true
}
```

### Hook Types

**Session Hooks:**
```json
{
  "name": "learning-session",
  "trigger": "command",
  "triggerValue": "/learn",
  "actions": [...]
}
```

**Progress Hooks:**
```json
{
  "name": "progress-tracking",
  "trigger": "scheduled",
  "frequency": "weekly",
  "actions": [...]
}
```

**Milestone Hooks:**
```json
{
  "name": "achievement-celebration",
  "trigger": "milestone",
  "triggerValue": "skill-mastery",
  "actions": [...]
}
```

---

## JSON Schema

### plugin.json Structure
```json
{
  "name": "plugin-id",
  "displayName": "Display Name",
  "version": "1.0.0",
  "description": "Plugin description",
  "agents": [...],
  "commands": [...],
  "skills": [...],
  "hooks": {...},
  "statistics": {...}
}
```

### Validation Rules
```
✅ name: lowercase, hyphens, 3-64 chars
✅ version: semantic versioning (major.minor.patch)
✅ agents: array of agent objects with required fields
✅ skills: array of skill objects with triggers
✅ hooks: valid hook definitions
```

---

## Error Handling

### Common Issues

| Error | Cause | Solution |
|-------|-------|----------|
| Agent not found | Invalid ID | Check agent ID in plugin.json |
| Skill mismatch | Trigger not defined | Add skill trigger keywords |
| Hook not firing | Incorrect trigger | Verify trigger type and value |
| JSON invalid | Syntax error | Validate with JSON linter |

---

## Rate Limiting

Not applicable - all processing is local to Claude Code environment.

## Caching

```
Content caching:
├─ Agent definitions: Cache on load
├─ Skill content: Cache on first access
├─ Roadmaps: Cache locally
└─ Examples: Cache for session duration
```

## Versioning

```
API versioning follows plugin versioning:
├─ 1.0.x: Backward compatible updates
├─ 1.x.0: New features, backward compatible
├─ 2.0.0: Breaking changes
```

---

**API Version:** 1.0.0 | **Updated:** 2024-11-18
