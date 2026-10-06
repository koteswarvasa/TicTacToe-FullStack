
```markdown
g# Tic-Tac-Toe Full Stack Application

A full-stack Tic-Tac-Toe application built using React, FastAPI, Python, and Microsoft SQL Server.

## Project Status

Currently implemented:

- SQL Server database
- APP and AUDIT schemas
- PLAYER table
- GAME table
- GAME_MOVE table
- Centralized AUDIT_LOG table
- SQLAlchemy database connection
- FastAPI backend
- Player registration API
- Duplicate username validation
- Duplicate email validation
- Password hashing using bcrypt
- Audit logging for player registration
- Login API

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript
- React

### Backend
- Python
- FastAPI
- SQLAlchemy
- PyODBC
- bcrypt

### Database
- Microsoft SQL Server

## Project Structure

```text
TicTacToe-FullStack/
│
├── frontend/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── routes/
│   │
│   ├── .env.example
│   └── requirements.txt
│
├── database/
│   └── 01_create_tictactoe_database.sql
│
├── .gitignore
└── README.md
```

## Backend Setup

Create a virtual environment:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r backend\requirements.txt
```

Create:

```text
backend/.env
```

and configure the SQL Server connection.

## Run Backend

From the `backend` directory:

```powershell
uvicorn app.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Security

Environment-specific configuration is stored in `.env` and is excluded from Git.

Passwords are stored using bcrypt hashing and are never stored as plain text.

```

```
