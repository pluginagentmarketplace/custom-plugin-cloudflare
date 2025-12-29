# Cloudflare Development Guide

> Cloudflare Plugin - Cloud Infrastructure Skill
> Workers, Pages, R2, D1

## Overview

Guide for building on Cloudflare's edge platform.

## Cloudflare Workers

### Basic Worker

```typescript
// src/index.ts
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === "/api/hello") {
      return Response.json({ message: "Hello from the edge!" });
    }

    return new Response("Not found", { status: 404 });
  },
};
```

### wrangler.toml

```toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"

[[r2_buckets]]
binding = "ASSETS"
bucket_name = "my-assets"

[[d1_databases]]
binding = "DB"
database_name = "my-database"
database_id = "xxx"
```

## Cloudflare Pages

### Deploy Next.js

```bash
# Install adapter
npm install @cloudflare/next-on-pages

# Build
npx @cloudflare/next-on-pages

# Deploy
npx wrangler pages deploy .vercel/output/static
```

## R2 Storage

```typescript
// Upload file
await env.ASSETS.put("file.txt", "Hello, R2!");

// Get file
const object = await env.ASSETS.get("file.txt");
```

## D1 Database

```typescript
// Query
const { results } = await env.DB.prepare(
  "SELECT * FROM users WHERE id = ?"
).bind(userId).all();
```

---

*Cloudflare Plugin - Cloud Infrastructure Skill*
