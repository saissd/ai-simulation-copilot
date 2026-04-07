# AI Simulation Insight Copilot

A full-stack application that combines scientific visualization with AI-assisted interpretation to make simulation data more accessible and actionable.

This project parses VTK-based simulation datasets, extracts scalar fields such as pressure and temperature, and provides both structured summaries and an interactive copilot interface for querying simulation behavior.

---

## 🚀 Demo Video
https://drive.google.com/file/d/14F-6wqyTCOwjL06A06qni1PUpMeHkJkb/view?usp=sharing

---

## 🎯 Key Features
- VTK simulation data parsing (PyVista-based workflow)
- Scalar field extraction (pressure, temperature)
- AI-style insight generation with fallback logic
- Copilot interface for natural language querying
- Interactive 3D visualization using Three.js
- FastAPI backend with lightweight frontend UI

---

## 🧠 Why This Project
This project is designed to align with roles involving:
- Scientific visualization (ParaView-style workflows)
- Simulation data inspection and analysis
- AI-assisted engineering tools
- Data-to-insight pipelines

It demonstrates the ability to:
- Work with structured scientific data formats (VTK)
- Build full-stack applications
- Integrate visualization with intelligent reasoning layers

---

## 🛠️ Tech Stack
- Backend: FastAPI, Python  
- Visualization: PyVista, Three.js  
- Frontend: HTML, CSS, JavaScript  
- AI Layer: Rule-based (optional OpenAI integration)  

---

## 📂 Project Structure
ai-simulation-copilot/
├── backend/
│   ├── app.py
│   ├── data/
│   │   └── sample_simulation.vtk
│   └── services/
│       ├── ai_explainer.py
│       └── vtk_parser.py
├── frontend/
│   └── static/
│       ├── app.js
│       ├── index.html
│       └── styles.css
├── .env.example
├── requirements.txt
└── README.md

---

## ⚙️ How to Run

### 1. Create virtual environment

Windows:
python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

---

### 2. Install dependencies
pip install -r requirements.txt

---

### 3. (Optional) Add OpenAI API Key
Copy `.env.example` → `.env` and add:
OPENAI_API_KEY=your_key_here

If skipped, the app still works using a local fallback.

---

### 4. Run the app
uvicorn backend.app:app --reload

Open:
http://127.0.0.1:8000

---

## 🔌 API Endpoints
- GET /health → health check  
- GET /api/summary → simulation summary + insight  
- POST /api/chat → copilot Q&A  
- GET /api/mesh → 3D visualization data  

---

## 💬 Example Queries
- Where is the highest pressure?  
- Are there any hotspots in this simulation?  
- What does the temperature distribution indicate?  

---

## 🧩 Future Improvements
- Scalar-based color mapping in 3D visualization  
- Hotspot detection using actual max-value computation  
- Support for additional formats (CSV, VTU)  
- Upload and multi-file handling  
- Export reports (PDF / JSON)

---

## 🧠 Interview Talking Point

Built a full-stack system that parses VTK simulation data, extracts scalar fields, and combines 3D visualization with an AI copilot to interpret simulation behavior in natural language.

---

## 📌 Repo Description (short)
AI-powered visualization and interpretation of scientific simulation data using VTK, FastAPI, and Three.js.
