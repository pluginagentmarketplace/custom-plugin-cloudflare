# System Design Guide for Cloudflare

## Edge-First Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLOUDFLARE EDGE                       │
├─────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Workers │  │  Pages  │  │   WAF   │  │  Cache  │    │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘    │
│       │            │            │            │          │
│  ┌────▼────────────▼────────────▼────────────▼────┐    │
│  │              Durable Objects                    │    │
│  │         (Stateful Edge Computing)              │    │
│  └────┬───────────────────────────────────────────┘    │
│       │                                                 │
│  ┌────▼────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │
│  │   KV    │  │   D1    │  │   R2    │  │ Queues  │   │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Full-Stack Edge Pattern

```typescript
// wrangler.toml
// name = "fullstack-app"
// [[ d1_databases ]]
// binding = "DB"
// database_name = "app-db"
// [[ kv_namespaces ]]
// binding = "CACHE"

export default {
  async fetch(request: Request, env: Env) {
    const url = new URL(request.url);

    // API routes
    if (url.pathname.startsWith('/api/')) {
      return handleAPI(request, env);
    }

    // Static assets from R2/KV
    return env.ASSETS.fetch(request);
  }
};

async function handleAPI(request: Request, env: Env) {
  // Check cache first
  const cached = await env.CACHE.get(request.url);
  if (cached) return new Response(cached);

  // Query D1
  const data = await env.DB.prepare("SELECT * FROM items").all();

  // Cache result
  await env.CACHE.put(request.url, JSON.stringify(data), { expirationTtl: 300 });

  return Response.json(data);
}
```

## Scaling Patterns

| Pattern | Use Case | Services |
|---------|----------|----------|
| **Cache-First** | Read-heavy APIs | KV + Workers |
| **Stateful Edge** | Real-time apps | Durable Objects |
| **Queue Processing** | Background jobs | Queues + Workers |
| **Global Database** | CRUD apps | D1 + Workers |
| **Object Storage** | Media/files | R2 + Workers |

## Security Architecture

```typescript
// Zero Trust with Cloudflare Access
export default {
  async fetch(request: Request, env: Env) {
    // Verify JWT from Cloudflare Access
    const jwt = request.headers.get('Cf-Access-Jwt-Assertion');
    if (!jwt) {
      return new Response('Unauthorized', { status: 401 });
    }

    // Proceed with authenticated request
    return handleRequest(request, env);
  }
};
```

---

*Cloudflare Plugin - System Design Skill*
