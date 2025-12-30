---
# ═══════════════════════════════════════════════════════════════════════════
# SKILL: Data Engineering
# Version: 2.0.0 | Updated: 2025-01
# ═══════════════════════════════════════════════════════════════════════════
name: data-engineering
description: Data engineering, machine learning, AI, and MLOps. From data pipelines to production ML systems and LLM applications.

# ACTIVATION TRIGGERS
triggers:
  - data engineering
  - machine learning
  - ml
  - ai
  - mlops
  - spark
  - airflow
  - llm
  - rag
  - langchain

# SKILL PARAMETERS
parameters:
  role:
    type: string
    enum: [data-engineer, ml-engineer, ai-engineer]
    required: true
  experience:
    type: string
    enum: [beginner, intermediate, advanced]
    required: false
    default: beginner

# OUTPUT SPECIFICATION
outputs:
  learning_path:
    type: array
  tech_stack:
    type: object
  projects:
    type: array

# RELIABILITY
retry:
  max_attempts: 3
  backoff: exponential

# OBSERVABILITY
observability:
  log_level: info
  metrics: [path_completion_rate]

level: advanced
prerequisites:
  - programming-basics
  - python-advanced
---

# Data Engineering Skill

## Quick Reference

| Role | Focus | Timeline | Entry From |
|------|-------|----------|------------|
| **Data Engineer** | Pipelines, Infra | 12-24 mo | Backend Dev |
| **ML Engineer** | Models, Features | 12-24 mo | Data Scientist |
| **AI Engineer** | LLMs, Agents | 6-12 mo | Any Developer |

---

## Learning Paths

### Data Engineer
```
[1] SQL Mastery (4-6 wk)
 │  └─ Window functions, CTEs, optimization
 │
 ▼
[2] Python for Data (4-6 wk)
 │  └─ Pandas, file formats, scripting
 │
 ▼
[3] ETL/ELT Pipelines (6-8 wk)
 │  └─ Extract, transform, load patterns
 │
 ▼
[4] Big Data: Spark (8-12 wk)
 │  └─ PySpark, DataFrames, partitioning
 │
 ▼
[5] Data Warehouse (4-6 wk)
 │  └─ Star schema, dbt, Snowflake/BQ
 │
 ▼
[6] Orchestration (4-6 wk)
    └─ Airflow/Prefect, scheduling, monitoring
```

**2025 Stack:** Python + Spark + Airflow + dbt + Snowflake/BigQuery

---

### ML Engineer
```
[1] Python + NumPy (4-6 wk)
 │
 ▼
[2] Math Foundations (6-8 wk)
 │  └─ Linear algebra, calculus, statistics
 │
 ▼
[3] Classical ML (8-12 wk)
 │  └─ scikit-learn, XGBoost, evaluation
 │
 ▼
[4] Deep Learning (8-12 wk)
 │  └─ PyTorch, CNNs, Transformers
 │
 ▼
[5] MLOps (6-8 wk)
    └─ MLflow, model serving, monitoring
```

**2025 Stack:** Python + PyTorch + scikit-learn + MLflow + W&B

---

### AI Engineer (2025 Hot Path)
```
[1] LLM Fundamentals (2-3 wk)
 │  └─ Tokens, embeddings, context windows
 │
 ▼
[2] Prompt Engineering (2-3 wk)
 │  └─ Few-shot, CoT, structured output
 │
 ▼
[3] RAG Systems (3-4 wk)
 │  └─ Embeddings, vector DBs, retrieval
 │
 ▼
[4] AI Agents (4-6 wk)
 │  └─ Tool calling, agent loops, memory
 │
 ▼
[5] Production Deploy (ongoing)
    └─ Evaluation, guardrails, monitoring
```

**2025 Stack:** Python + LangChain/LlamaIndex + OpenAI/Anthropic + ChromaDB

---

## 2025 Tool Matrix

### Data Processing
| Tool | Scale | Use Case |
|------|-------|----------|
| **Pandas** | <10GB | Prototyping, small data |
| **Polars** | <100GB | Fast local processing |
| **Spark** | >100GB | Distributed processing |
| **dbt** | Any | Transformations, testing |

### ML Frameworks
| Framework | Best For | Complexity |
|-----------|----------|------------|
| **scikit-learn** | Classical ML | Low |
| **XGBoost** | Tabular data | Low |
| **PyTorch** | Research, flexibility | Medium |
| **TensorFlow** | Production, mobile | Medium |

### LLM/AI Tools
| Tool | Use Case |
|------|----------|
| **LangChain** | LLM orchestration |
| **LlamaIndex** | RAG systems |
| **Claude/OpenAI** | LLM APIs |
| **ChromaDB** | Vector storage |

---

## Algorithm Reference

### Classical ML
| Type | Algorithms |
|------|------------|
| Regression | Linear, Ridge, Lasso, ElasticNet |
| Classification | Logistic, SVM, Decision Tree |
| Ensemble | Random Forest, XGBoost, LightGBM |
| Clustering | K-Means, DBSCAN, Hierarchical |

### Deep Learning
| Architecture | Use Case |
|--------------|----------|
| **CNN** | Images, vision |
| **RNN/LSTM** | Sequences |
| **Transformer** | NLP, LLMs |
| **Diffusion** | Image generation |

---

## AI Agent Architecture (2025)

```
┌─────────────────────────────────────────┐
│            AGENTIC LOOP                  │
├─────────────────────────────────────────┤
│  PERCEIVE → REASON → ACT → REFLECT      │
│      │         │       │       │        │
│      │         │       │       └─► Loop │
│      │         │       └─► Execute tools│
│      │         └─► LLM decides action   │
│      └─► Gather context, observations   │
└─────────────────────────────────────────┘

Design Patterns (Anthropic 2025):
• Prompt Chaining - Sequential fixed steps
• Routing - Classify and dispatch
• Parallelization - Concurrent subtasks
• Orchestrator-Workers - Central delegation
• Evaluator-Optimizer - Generate + critique
```

---

## Troubleshooting

```
Which path to choose?
├─► Love building infrastructure? → Data Engineer
├─► Love algorithms/math? → ML Engineer
├─► Want fastest AI entry? → AI Engineer
└─► Uncertain? → Start with Python + SQL

Model not performing well?
├─► Data quality issues? → Clean data first
├─► Feature engineering? → Create better features
├─► Wrong algorithm? → Try different models
├─► Overfitting? → More data, regularization
└─► Hyperparameters? → Grid/random search

LLM giving bad answers?
├─► Prompt too vague? → Be more specific
├─► Missing context? → Add relevant info
├─► Hallucinating? → Use RAG, verify facts
└─► Wrong tool? → Improve tool descriptions
```

---

## Common Failure Modes

| Symptom | Root Cause | Recovery |
|---------|------------|----------|
| Model fails in prod | Data drift | Monitor distributions |
| Pipeline always late | Unoptimized queries | Profile, partition |
| RAG finds wrong docs | Bad chunking | Tune chunk size, overlap |
| Agent loops forever | No exit condition | Add max iterations |

---

## Portfolio Projects

### Data Engineering
1. ETL Pipeline (Airflow + dbt)
2. Real-time Streaming (Kafka + Spark)
3. Data Warehouse Design

### ML Engineering
1. Classification Model (scikit-learn)
2. Deep Learning Model (PyTorch)
3. ML Pipeline (MLflow)

### AI Engineering
1. RAG Chatbot (LangChain + ChromaDB)
2. AI Agent with Tools
3. Multi-Agent System

---

## Next Actions

Specify your target role for a detailed learning plan.
