# Technical Stack

## Overview

This document outlines the technology stack for the Cloud Certification Prep Platform MVP. The stack is designed for rapid local development with a focus on simplicity and developer experience.

## Development Philosophy

- **Local-first:** MVP runs entirely on local development environment
- **Simplicity:** Choose proven, well-documented technologies
- **Type Safety:** Leverage TypeScript and Pydantic for end-to-end type safety
- **Modern Tooling:** Use latest stable versions with good DX

---

## Frontend

### Core Framework
- **[Nuxt.js 3](https://nuxt.com/)** - Vue.js meta-framework with SSR/SSG capabilities
- **TypeScript** - Type-safe JavaScript for improved developer experience

### Key Frontend Dependencies
- **`nuxt`** - Framework
- **`vue`** - Core library
- **`pinia`** - State management
- **`axios`** - HTTP client
- **`@pinia/nuxt`** - Pinia Nuxt module
- **`chart.js`** or **`echarts`** - For progress dashboard charts
- **`date-fns`** - Date/time utilities for timer

### State Management
- **[Pinia](https://pinia.vuejs.org/)** - Official Vue/Nuxt state management
  - TypeScript-first with excellent type inference
  - Modular stores (auth, user, exam, questions, progress)
  - DevTools integration for debugging
  - SSR support out of the box

### UI Components & Styling
- **Custom CSS** - Built from scratch for full control
  - CSS variables for design tokens (colors, spacing, typography)
  - Scoped component styles with Vue SFC `<style scoped>`
  - Consistent design system documented in styleguide
  - BEM or similar methodology for class naming consistency
  - No external component libraries

### API Client
- **[Axios](https://axios-http.com/)** - HTTP client for API requests
  - Interceptors for auth token injection
  - Request/response transformation
  - Error handling middleware
  - TypeScript support with typed responses

---

## Backend

### Core Framework
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern Python web framework with automatic API docs
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation using Python type hints
- **[SQLModel](https://sqlmodel.tiangolo.com/)** - SQL databases with Python type hints (combines SQLAlchemy + Pydantic)

### Package Management
- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer and resolver

### Key Backend Dependencies
- **`fastapi`** - Web framework
- **`uvicorn`** - ASGI server
- **`sqlmodel`** - ORM and validation
- **`pydantic`** - Data validation
- **`psycopg2-binary`** - PostgreSQL adapter
- **`alembic`** - Database migrations
- **`python-jose[cryptography]`** - JWT tokens
- **`google-auth`** - Google OAuth
- **`boto3`** - AWS SDK (S3, Bedrock)
- **`langgraph`** - Agent framework
- **`langchain-aws`** - AWS Bedrock integration
- **`playwright`** - Web scraping

### Authentication
- **Google OAuth 2.0** - SSO with work Gmail accounts
- **Implementation:** Custom implementation using `google-auth` library
  - Full control over auth flow
  - JWT tokens for session management
  - Role-based access control (user/admin)

### Session Management
- **PostgreSQL-based sessions** - Store refresh tokens and session data in database
  - Simpler setup (no additional services)
  - Ability to revoke sessions
  - Session history tracking

---

## Database

### Primary Database
- **[PostgreSQL](https://www.postgresql.org/)** - Relational database for all application data
  - User profiles and authentication
  - Certification definitions and topics
  - Question bank
  - User progress and analytics
  - Bookmarks and ratings

### ORM
- **SQLModel** - Type-safe database queries with Pydantic integration

---

## AI & Agents

### LLM Provider
- **[AWS Bedrock](https://aws.amazon.com/bedrock/)** with **Claude** models
  - Question generation from scraped templates
  - AI chat for explaining incorrect answers
  - Study recommendations generation

### Agent Framework
- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Framework for building stateful AI agents
  - Question generation workflows
  - Adaptive difficulty algorithms
  - Personalized study path generation

### Embeddings
- **AWS Bedrock Titan Embeddings** - For question similarity and semantic search
  - Native integration with Bedrock
  - Consistent AWS ecosystem
  - Used for detecting duplicate questions and content similarity

---

## Content Generation

### Web Scraping
- **[Playwright](https://playwright.dev/python/)** - Browser automation for scraping JavaScript-heavy sites
  - Handles modern exam prep websites with dynamic content
  - Can capture screenshots of questions with images
  - Reliable rendering of complex page structures
  - Fallback to BeautifulSoup for simple static pages if needed

---

## Development Environment

### Local Setup
- **Docker Compose** - Containerized development environment
  - PostgreSQL database container
  - Backend (FastAPI) container with hot reload
  - Frontend (Nuxt) container with HMR
  - Consistent environment across all developers
  - Easy setup with single `docker-compose up` command

### Version Control
- **Git** - Source control
- **GitHub/GitLab** - Repository hosting (assumed)

---

## Testing

### Approach
- **Minimal testing** - Focus on critical paths only
  - Authentication flow
  - Question generation and validation
  - Exam scoring logic
  - Database operations

### Backend Testing
- **[pytest](https://docs.pytest.org/)** - Python testing framework
- **[pytest-asyncio](https://pytest-asyncio.readthedocs.io/)** - Async test support
- **[httpx](https://www.python-httpx.org/)** - For testing FastAPI endpoints

### Frontend Testing
- **[Vitest](https://vitest.dev/)** - Fast Vite-native test framework
- **[@vue/test-utils](https://test-utils.vuejs.org/)** - Official Vue testing utilities
- **[happy-dom](https://github.com/capricorn86/happy-dom)** - Lightweight DOM implementation

---

## Real-time Features

### Exam Timer
- **Client-side JavaScript timer** - Browser-based countdown
  - Simple setInterval/setTimeout implementation
  - No server connection required
  - Auto-submit exam when timer expires
  - Warning notifications at key intervals (5 min, 1 min remaining)

---

## File Storage

### Question Assets (Images/Diagrams)
- **[AWS S3](https://aws.amazon.com/s3/)** - Object storage for question images and assets
  - Scalable and cost-effective
  - Direct integration with AWS Bedrock (same ecosystem)
  - Pre-signed URLs for secure access
  - CDN-ready for future CloudFront integration
  - Use `boto3` Python SDK for S3 operations

---

## Deployment (Post-MVP)

### Planned Platform
- **AWS (Amazon Web Services)** - Primary deployment target
  - **Frontend:** S3 + CloudFront or Amplify Hosting
  - **Backend:** ECS (Fargate) or App Runner
  - **Database:** RDS PostgreSQL
  - **Assets:** S3 (already in use)
  - **AI:** Bedrock (already in use)
  - **Secrets:** AWS Secrets Manager or Parameter Store

---

## Development Tools

### Code Quality
- **Ruff** - Fast Python linter and formatter
- **ESLint** - JavaScript/TypeScript linter
- **Prettier** - Code formatter for frontend

### API Documentation
- **FastAPI automatic OpenAPI/Swagger** - Built-in interactive API docs

### Database Migrations
- **Alembic** - Database migration tool (works with SQLModel/SQLAlchemy)

---

## Project Structure (Proposed)

```
devo-cert-prep/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── models/       # SQLModel database models
│   │   ├── schemas/      # Pydantic request/response schemas
│   │   ├── services/     # Business logic
│   │   ├── agents/       # LangGraph agent implementations
│   │   └── core/         # Config, auth, dependencies
│   ├── pyproject.toml    # uv project configuration
│   └── alembic/          # Database migrations
├── frontend/
│   ├── pages/            # Nuxt pages (routes)
│   ├── components/       # Vue components
│   ├── composables/      # Composable functions
│   ├── layouts/          # Page layouts
│   └── nuxt.config.ts    # Nuxt configuration
├── docs/                 # Project documentation
└── docker-compose.yml    # Local development setup (if using Docker)
```

---

## Next Steps

1. Answer remaining tech stack questions
2. Set up project structure
3. Initialize backend with FastAPI + SQLModel
4. Initialize frontend with Nuxt.js + TypeScript
5. Set up local PostgreSQL database
6. Configure AWS Bedrock credentials
7. Implement basic authentication flow
