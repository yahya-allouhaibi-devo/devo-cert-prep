# Cloud Certification Prep Platform

## Project Overview

An internal web application for IT consultants to prepare for cloud certifications (AWS, Azure, GCP, Snowflake) through AI-powered practice questions and realistic exam simulations.

**Goal:** Build a simple, functional MVP that runs locally before considering deployment.

## Important: Tech Stack Reference

**⚠️ Before installing any packages or dependencies, always check `docs/tech-stack.md` first.**

The tech stack document contains the complete list of approved technologies, libraries, and specific versions. If a technology or package is specified in that file, use exactly what's documented there. Do not install alternatives or additional libraries without consulting the tech stack document first.

## Tech Stack

### Frontend
- **Nuxt.js 3** with TypeScript
- **Pinia** for state management
- **Axios** for API calls
- **Custom CSS** (no component libraries) - Use CSS variables, scoped styles, BEM methodology

### Backend
- **FastAPI** with Pydantic and SQLModel
- **UV** for package management
- **PostgreSQL** for database
- **Custom Google OAuth** implementation with JWT tokens
- **PostgreSQL-based** session management

### AI & Content
- **AWS Bedrock** with Claude models (question generation, AI chat)
- **LangGraph** for agent workflows
- **Playwright** for web scraping exam prep sites
- **AWS Bedrock Titan Embeddings** for question similarity

### Infrastructure
- **Docker Compose** for local development
- **AWS S3** for question images/assets
- **boto3** for AWS operations

### Testing
- **Minimal testing** (auth, question generation, exam scoring)
- Backend: pytest, pytest-asyncio, httpx
- Frontend: Vitest, @vue/test-utils, happy-dom

## Key Features (MVP)

### 1. Authentication & User Management
- Google SSO with work Gmail
- Two roles: Individual user and Admin
- User selects one active certification path

### 2. Practice Modes
- **General Practice:** Untimed, adaptive weighting based on weak areas
- **Topic-Specific Practice:** Focused on individual exam domains
- Immediate feedback, AI chat for explanations, bookmark/flag questions

### 3. Exam Simulator
- Realistic timed exams matching real certification conditions
- No pause/resume (complete in one sitting)
- Post-exam analytics: score breakdown by topic, question review, study recommendations
- Client-side JavaScript timer with auto-submit

### 4. Progress Dashboard
- Overall statistics and accuracy rates
- Performance breakdown by topic with charts
- Exam simulator history and trends
- Bookmarked questions library
- Readiness indicator

### 5. Admin Dashboard
- Create/manage certifications (provider, name, exam parameters)
- Define exam domains/topics with weights
- Question management (review flagged, edit, approve AI-generated)
- User management (view users, promote to admin)
- View aggregate platform statistics

### 6. Question Generation System
- Web scraping (Playwright) for exam prep templates
- AI generation via AWS Bedrock Claude
- User rating and issue reporting
- Quality control feedback loop

## Project Structure

```
devo-cert-prep/
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI routes
│   │   ├── models/       # SQLModel database models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── services/     # Business logic
│   │   ├── agents/       # LangGraph agents
│   │   └── core/         # Config, auth, dependencies
│   ├── pyproject.toml
│   └── alembic/          # Database migrations
├── frontend/
│   ├── pages/            # Nuxt pages
│   ├── components/       # Vue components
│   ├── composables/      # Composable functions
│   ├── stores/           # Pinia stores
│   └── nuxt.config.ts
├── docs/
└── docker-compose.yml
```

## Development Guidelines

### Code Style
- **Backend:** Follow FastAPI best practices, type hints everywhere, Ruff for linting
- **Frontend:** TypeScript strict mode, ESLint + Prettier, consistent CSS naming (BEM)

### Database
- Use SQLModel for models (combines SQLAlchemy + Pydantic)
- Alembic for migrations
- Store: users, certifications, topics, questions, user_progress, sessions, bookmarks

### Authentication Flow
- Google OAuth 2.0 → JWT access/refresh tokens
- Store sessions in PostgreSQL
- Role-based access (user/admin)
- Admin assignment via email whitelist or manual promotion

### AI Integration
- LangGraph for stateful agent workflows
- Claude via Bedrock for question generation and chat
- Embeddings for duplicate detection
- S3 for storing scraped/generated question images

### Frontend Patterns
- Pinia stores: auth, user, exam, questions, progress
- Axios interceptors for auth token injection
- CSS variables for design system consistency
- Client-side timer for exams (setInterval)

### Key Constraints
- Internal use only (no commercial)
- Privacy-focused (user data private, admins see only aggregate stats)
- Local-first MVP (deployment is post-MVP)
- Simple over complex (avoid over-engineering)

## Important Notes

- **No pause/resume in exam mode** - Must complete in one sitting
- **Adaptive questioning** - System weights questions toward weak areas
- **Question quality** - User ratings feed back into system
- **Single active cert** - Users study one certification at a time
- **Admin control** - Admins create certifications that users can choose from

## AWS Services Required

- **Bedrock:** Claude models + Titan Embeddings
- **S3:** Question assets storage
- **Credentials:** Configure AWS credentials locally for development

