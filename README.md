# Cloud Certification Prep Platform

An internal web application for IT consultants to prepare for cloud certifications (AWS, Azure, GCP, Snowflake) through AI-powered practice questions and realistic exam simulations.

## Project Structure

```
devo-cert-prep/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── models/      # SQLModel database models
│   │   ├── schemas/     # Pydantic schemas
│   │   ├── services/    # Business logic
│   │   ├── agents/      # LangGraph agents
│   │   └── core/        # Config, auth, dependencies
│   ├── alembic/         # Database migrations
│   ├── main.py          # FastAPI application entry point
│   └── pyproject.toml   # Python dependencies
├── frontend/            # Nuxt.js frontend
│   ├── pages/          # Nuxt pages (routes)
│   ├── components/     # Vue components
│   ├── composables/    # Composable functions
│   ├── layouts/        # Page layouts
│   ├── stores/         # Pinia stores
│   └── assets/         # CSS, images, etc.
├── docs/               # Project documentation
└── docker-compose.yml  # Local development setup
```

## Tech Stack

### Frontend
- **Nuxt.js 3** with TypeScript
- **Pinia** for state management
- **Axios** for API calls
- **Chart.js** for data visualization
- Custom CSS (no component libraries)

### Backend
- **FastAPI** with Pydantic and SQLModel
- **UV** for package management
- **PostgreSQL** for database
- **AWS Bedrock** (Claude models for AI features)
- **LangGraph** for agent workflows
- **Playwright** for web scraping

## Prerequisites

- **Python 3.13+** (with UV package manager)
- **Node.js 18+** (with npm)
- **Docker & Docker Compose** (for local PostgreSQL)
- **AWS Account** (for Bedrock access)

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd devo-cert-prep
```

### 2. Set Up Backend

```bash
# Navigate to backend directory
cd backend

# Copy environment variables template
cp .env.example .env

# Edit .env and add your credentials
# - Database credentials
# - AWS credentials
# - Google OAuth credentials
# - JWT secret key

# Install dependencies (UV will use existing .venv if present)
uv sync

# Run database migrations (once PostgreSQL is running)
# alembic upgrade head
```

### 3. Set Up Frontend

```bash
# Navigate to frontend directory
cd frontend

# Copy environment variables template
cp .env.example .env

# Install dependencies
npm install
```

### 4. Start Services with Docker Compose

```bash
# From project root, start PostgreSQL, backend, and frontend
docker-compose up

# Or run services individually:
# PostgreSQL only
docker-compose up db

# Backend only (after DB is running)
docker-compose up backend

# Frontend only
docker-compose up frontend
```

### 5. Run Services Locally (Alternative to Docker)

If you prefer to run services directly on your machine:

**Start PostgreSQL:**
```bash
docker-compose up db
# Or use a local PostgreSQL installation
```

**Start Backend:**
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Start Frontend:**
```bash
cd frontend
npm run dev
```

## Accessing the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs (Swagger UI)
- **Alternative API Docs:** http://localhost:8000/redoc (ReDoc)

## Environment Variables

### Backend (.env)

Key environment variables for the backend:

- `DATABASE_URL`: PostgreSQL connection string
- `AWS_REGION`: AWS region for Bedrock
- `AWS_ACCESS_KEY_ID`: AWS credentials
- `AWS_SECRET_ACCESS_KEY`: AWS credentials
- `GOOGLE_CLIENT_ID`: Google OAuth client ID
- `GOOGLE_CLIENT_SECRET`: Google OAuth client secret
- `JWT_SECRET_KEY`: Secret key for JWT tokens
- `S3_BUCKET_NAME`: S3 bucket for question assets
- `ADMIN_EMAILS`: Comma-separated list of admin emails

### Frontend (.env)

Key environment variables for the frontend:

- `NUXT_PUBLIC_API_BASE_URL`: Backend API URL (default: http://localhost:8000)
- `NUXT_PUBLIC_GOOGLE_CLIENT_ID`: Google OAuth client ID

## Development Guidelines

### Backend Development

- Use **type hints** everywhere
- Follow **FastAPI best practices**
- Use **SQLModel** for database models
- Use **Alembic** for database migrations
- Run **Ruff** for linting and formatting

### Frontend Development

- Use **TypeScript strict mode**
- Follow **BEM methodology** for CSS class naming
- Use **scoped styles** in Vue components
- Use **Pinia stores** for state management
- Run **ESLint** and **Prettier** for code quality

### Code Style

**Backend:**
```bash
cd backend
ruff check .
ruff format .
```

**Frontend:**
```bash
cd frontend
npm run lint
npm run format
```

## Testing

**Backend:**
```bash
cd backend
pytest
```

**Frontend:**
```bash
cd frontend
npm run test
```

## Database Migrations

Create a new migration:
```bash
cd backend
alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback migration:
```bash
alembic downgrade -1
```

## Key Features (MVP)

1. **Authentication:** Google SSO with JWT tokens
2. **Practice Modes:** General and topic-specific practice
3. **Exam Simulator:** Timed exams with realistic conditions
4. **Progress Dashboard:** Statistics and performance tracking
5. **Admin Dashboard:** Certification and question management
6. **AI Question Generation:** Using AWS Bedrock Claude models

## Project Documentation

- [Project Brief](docs/project-brief.md) - Detailed project overview and requirements
- [Tech Stack](docs/tech-stack.md) - Complete technical stack documentation
- [Claude Instructions](CLAUDE.md) - AI assistant guidelines for development

## License

Internal use only - Not for commercial distribution.

## Support

For questions or issues, please contact the development team.
