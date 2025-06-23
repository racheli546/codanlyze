
# 🧠 CodeGuard – Python Code Analysis System (CI via wit push)

**CodeGuard** is a backend system developed as part of a version control tool (Wit),  
designed to run automated code analysis every time a user performs `wit push`.

This project simulates a simplified Continuous Integration (CI) flow for Python projects,  
focusing on maintaining code quality and providing developers with visual and actionable feedback.

---

## 🚀 Project Overview

- 🔧 **Language**: Python  
- 🌐 **Server**: FastAPI  
- 🧠 **Code Analysis**: `ast` (Abstract Syntax Tree)  
- 📊 **Visualization**: `matplotlib`

Every time a user runs `wit push`, the system:
- Performs static analysis on the pushed Python files
- Detects common issues
- Returns detailed reports and visual graphs

---

## 📦 Folder Structure

```
/server
  ├── main.py
  ├── analysis.py
  ├── visualization.py
  └── models.py
```

---

## 📬 API Endpoints

| Endpoint    | Method | Description                           |
|-------------|--------|---------------------------------------|
| `/analyze`  | POST   | Accepts Python files and returns graphs (PNG) |
| `/alerts`   | POST   | Accepts Python files and returns list of issues |

---

## 🧪 Code Quality Checks

The analysis includes the following validations:

- ❗ Function length > 20 lines  
- ❗ File length > 200 lines  
- ❗ Unused variables  
- ❗ Missing docstrings  
- ⚠️ (Bonus) Variables with non-English names (e.g., Hebrew)

---

## 📊 Generated Graphs

- 📈 Histogram: Function length distribution  
- 🥧 Pie chart: Issue types  
- 📊 Bar chart: Issues per file  
- 🪄 (Optional) Line graph: Issue trends over time  

Graphs are returned as PNG files after each analysis.

---

## 🛠️ Running the Server Locally

### Requirements
- Python 3.9+
- `fastapi`, `uvicorn`, `matplotlib`

### Installation

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The server will run by default on:  
`http://localhost:8000`

---

## 📌 Bonus
 
- Easily extendable for additional code quality rules and visualizations

---

## ✍️ Author

Developed by Rachel Segal 
GitHub: (https://github.com/racheli546)
