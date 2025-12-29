# Core Development Guide

> Frontend, Backend, Full Stack

## Frontend (React + Vite)

```bash
npm create vite@latest my-app -- --template react-ts
```

## Backend (Node + Fastify)

```typescript
import Fastify from 'fastify';

const app = Fastify();

app.get('/api/hello', async () => {
  return { message: 'Hello!' };
});

app.listen({ port: 3000 });
```

## Full Stack on Cloudflare

- Frontend: Cloudflare Pages
- Backend: Cloudflare Workers
- Database: D1

---

*Cloudflare Plugin - Core Development Skill*
