# Wallet

A simple FastAPI-based wallet/expense tracker demonstration.

## Overview

This project provides a small API for:
- user login
- adding expenses
- retrieving added expenses

The app uses token-based auth with `HTTPBearer` and stores expenses in memory.

## Requirements

- Python 3.10+
- `fastapi`
- `uvicorn`
- `pydantic`

## Installation

Install dependencies:

   ```powershell
   pip install fastapi uvicorn
   ```

## Run the app

Start the server with:

```powershell
py -m uvicorn test:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Notes

- This project uses in-memory storage. Data is lost when the server restarts.
- The login credentials and token are hardcoded for demonstration only.

## Testing
- This project supports automated API test execution using Newman.
- Independent Tests and E2E Tests should be executed separately due to shared in-memory test data state.

Run Independent Tests:

```powershell
newman run "postman/Wallet API Test.postman_collection.json" --folder "Independent Tests"
```

Run E2E Tests:

```powershell
newman run "postman/Wallet API Test.postman_collection.json" --folder "E2E Tests"
```