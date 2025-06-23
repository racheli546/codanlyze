
# 🧠 CodeGuard – Python Code Analysis API

CodeGuard is a backend project developed in Python using FastAPI,  
designed to analyze Python code and return visual reports and quality alerts.

The system performs static analysis using AST, identifies code issues,  
and generates visual feedback via matplotlib.

---

## 🚀 Project Overview

- 🔧 **Language**: Python  
- 🌐 **Framework**: FastAPI  
- 🧠 **Code Analysis**: `ast`  
- 📊 **Visualization**: `matplotlib`

---

## 📬 API Endpoints

| Endpoint    | Method | Description                            |
|-------------|--------|----------------------------------------|
| `/analyze`  | POST   | Returns code visualizations (PNG)      |
| `/alerts`   | POST   | Returns a list of issues in the code   |

---

## 🧪 Code Quality Checks

The analysis includes checks such as:
- Function too long (>20 lines)
- File too long (>200 lines)
- Unused variables
- Missing docstrings
- (Optional) Non-English variable names

---

## 📊 Graphs Generated

- Histogram of function lengths  
- Pie chart of issue types  
- Bar chart: issues per file  
- Optional: line chart of issue trends  

---

## 🛠️ Running Locally

### Requirements
- Python 3.9+
- `fastapi`, `uvicorn`, `matplotlib`

### Installation

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## ✍️ Author

Developed by Rachel Segal  
GitHub: [racheli546](https://github.com/racheli546)
