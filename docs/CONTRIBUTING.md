# Contributing Guide

## How to Contribute

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help makes the plugin better.

### Types of Contributions

1. **Content Improvements**
   - Add new agents or skills
   - Enhance existing content
   - Add code examples
   - Improve documentation

2. **Bug Fixes**
   - Report issues via GitHub
   - Submit fixes via pull requests
   - Verify fixes work

3. **Feature Additions**
   - New commands
   - Enhanced hooks
   - Better integrations
   - Improved workflows

4. **Documentation**
   - README improvements
   - Architecture documentation
   - Best practices guides
   - Code examples

### Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/custom-plugin-cloudflare.git
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Follow the existing structure
   - Maintain quality standards
   - Add documentation
   - Include examples

4. **Test Your Changes**
   - Verify agent-skill-command alignment
   - Test workflows end-to-end
   - Validate JSON schemas
   - Check documentation links

5. **Submit a Pull Request**
   - Clear description of changes
   - Reference relevant issues
   - Include test results
   - Follow commit message format

### Code Style & Standards

#### Markdown Files
- Use clear, concise language
- Include examples
- Link to relevant sections
- Update table of contents

#### JSON Files
- Validate JSON syntax
- Use consistent formatting
- Document all fields
- Include comments where needed

#### Agent Files Format
```markdown
---
description: [What this agent specializes in]
capabilities: ["capability1", "capability2"]
---

# Agent Name

[Detailed content with examples]
```

#### Skill Files Format
```markdown
---
name: skill-id
description: [Quick description of skill]
---

# Skill Name

[Content with code examples]
```

### Testing Checklist

Before submitting a PR, verify:

- [ ] Agent-skill alignment is correct
- [ ] All links work properly
- [ ] Code examples are accurate
- [ ] JSON is valid and formatted
- [ ] Documentation is complete
- [ ] Hooks reference existing agents/skills
- [ ] No broken markdown links
- [ ] Plugin.json is valid
- [ ] CHANGELOG is updated

### Commit Message Format

```
feat: Add new [feature] capability
fix: Resolve [issue] in [component]
docs: Improve documentation for [section]
refactor: Reorganize [component] structure
```

### Review Process

1. Automated checks run (JSON validation, etc.)
2. Community review of changes
3. Maintainer approval
4. Merge to main branch
5. Release planning

### Community Standards

- Be respectful and inclusive
- Provide constructive feedback
- Help others when possible
- Follow project guidelines
- Respect copyright and licenses

### Questions?

- Open an issue on GitHub
- Check existing issues first
- Provide detailed context
- Include examples/code

---

**Contribution Guide:** 1.0.0 | **Updated:** 2024-11-18
