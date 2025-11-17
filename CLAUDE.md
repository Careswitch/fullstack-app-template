# CLAUDE.md

Fullstack application template with a React frontend and FastAPI backend.

## Development Commands

### Frontend (in `frontend/` directory)

```bash
# Start development server (runs on port 5174)
bun run dev

# Build for production (runs TypeScript compiler then Vite build)
bun run build

# Lint code
bun run lint

# Add new dependencies
bun add <dependency>
```

### Backend (in `backend/` directory)

```bash
# Start FastAPI development server with auto-reload (runs on port 8000)
uv run --with fastapi --with uvicorn --with pymssql uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Tech Stack

### Frontend

- **Framework**: React 19.2 with TypeScript
- **Build Tool**: Vite 7.2
- **Styling**: Tailwind CSS 4.1 (using @tailwindcss/vite plugin)
- **Routing**: React Router DOM v7
- **State Management**: TanStack Query (React Query) v5
- **Icons**: Lucide React
- **Package Manager**: Bun

### Backend

- **Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **Database Driver**: PyMSSQL (for SQL Server)
- **Package Manager**: uv

## Project Architecture

### Directory Structure

```
fullstack-app-template/
├── frontend/          # React frontend application
│   ├── src/
│   │   ├── pages/     # Top-level route components
│   │   ├── components/# Reusable UI components
│   │   ├── App.tsx    # Root component with providers and routing
│   │   └── main.tsx   # Application entry point
│   └── package.json
└── backend/           # FastAPI backend application
    └── main.py        # FastAPI application entry point
```

### Frontend Application Structure

The frontend uses a provider-based architecture with multiple context layers:

1. **QueryClientProvider** (outermost) - Manages server state and caching via TanStack Query
2. **BrowserRouter** - Handles client-side routing
3. **Routes** - Defines route mappings to page components

This structure is defined in `frontend/src/App.tsx` and mounted in `frontend/src/main.tsx` with React StrictMode.

### Backend Application Structure

The backend is a simple FastAPI application:

- `backend/main.py` - FastAPI application with routes
- Uses `uv` for dependency management and running the application

### Styling Approach

The frontend project uses Tailwind CSS 4.1 with:

- Custom theme configuration in `frontend/src/index.css` using the `@theme` directive
- Primary color defined as `--color-primary: #000000`
- System-based dark mode support (prefers-color-scheme)
- Component-level dark mode variants (e.g., `dark:bg-neutral-900`)

Components should use Tailwind utility classes with dark mode variants for theming.

### Component Patterns

Components follow these conventions:

- TypeScript interfaces for props (e.g., `ButtonProps`)
- Default export of the component function
- Variant-based styling with conditional class application
- Support for dark mode via `dark:` prefixes

### Frontend Routing

Routes are defined in `frontend/src/App.tsx` using React Router v7. Add new routes as `<Route>` elements within the `<Routes>` component.

### Backend API

The FastAPI backend exposes REST endpoints:

- `GET /` - Root endpoint returning a greeting
- `GET /health` - Health check endpoint

Add new API routes by defining them in `backend/main.py` using FastAPI decorators.

## Workflow

- After a series of frontend code changes, **always** run lint and build to ensure the code is working as expected.
