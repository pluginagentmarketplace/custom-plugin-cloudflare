# Languages Guide for Cloudflare

## TypeScript (Primary)

```typescript
// Workers TypeScript Template
interface Env {
  KV: KVNamespace;
  DB: D1Database;
  AI: Ai;
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === "/api/data") {
      const data = await env.KV.get("key");
      return Response.json({ data });
    }

    return new Response("Hello from TypeScript!");
  }
};
```

## Rust → WASM

```rust
// High-performance edge computing
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn hash_data(input: &str) -> String {
    use sha2::{Sha256, Digest};
    let mut hasher = Sha256::new();
    hasher.update(input.as_bytes());
    format!("{:x}", hasher.finalize())
}
```

## Python (Pyodide)

```python
# Python on Cloudflare Workers
async def on_fetch(request, env):
    import numpy as np
    result = np.mean([1, 2, 3, 4, 5])
    return Response(f"Mean: {result}")
```

## Best Practices

- Use TypeScript for type safety
- Rust for CPU-intensive operations
- Keep bundle sizes small (<1MB)

---

*Cloudflare Plugin - Languages Skill*
