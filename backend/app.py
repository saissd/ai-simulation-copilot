from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path

# ✅ Correct imports (based on your folder structure)
from backend.services.vtk_parser import parse_vtk_file, summarize_simulation
from backend.services.ai_explainer import generate_insight, answer_question_about_simulation

# Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
FRONTEND_DIR = BASE_DIR.parent / "frontend" / "static"
DEFAULT_FILE = DATA_DIR / "sample_simulation.vtk"

# App init
app = FastAPI(
    title="AI Simulation Insight Copilot",
    version="1.0.0"
)

# CORS (allow frontend calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    question: str


# ----------------------------
# Health Check
# ----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ----------------------------
# Summary + AI Insight
# ----------------------------
@app.get("/api/summary")
def get_summary():
    if not DEFAULT_FILE.exists():
        return {"error": "VTK file not found in backend/data/"}

    try:
        parsed = parse_vtk_file(str(DEFAULT_FILE))
        summary = summarize_simulation(parsed)
        insight = generate_insight(summary)

        return {
            "file_name": DEFAULT_FILE.name,
            "summary": summary,
            "insight": insight,
            "scalar_names": parsed.get("scalar_names", []),
            "preview_points": parsed.get("preview_points", []),
        }

    except Exception as e:
        return {"error": str(e)}


# ----------------------------
# Chat (Ask Questions)
# ----------------------------
@app.post("/api/chat")
def chat(req: ChatRequest):
    if not DEFAULT_FILE.exists():
        return {"error": "VTK file not found"}

    try:
        parsed = parse_vtk_file(str(DEFAULT_FILE))
        summary = summarize_simulation(parsed)

        answer = answer_question_about_simulation(summary, req.question)

        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}


# ----------------------------
# Download Sample Data
# ----------------------------
@app.get("/api/sample-data")
def sample_data():
    if not DEFAULT_FILE.exists():
        return {"error": "File not found"}

    return FileResponse(
        path=DEFAULT_FILE,
        filename=DEFAULT_FILE.name,
        media_type="application/octet-stream",
    )


# ----------------------------
# Serve Frontend
# ----------------------------
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def index():
    index_file = FRONTEND_DIR / "index.html"

    if index_file.exists():
        return FileResponse(index_file)

    return {"message": "Backend running. Frontend not found."}

@app.get("/api/mesh")
def get_mesh():
    parsed = parse_vtk_file(str(DEFAULT_FILE))

    return {
        "points": parsed["points"],
        "scalars": parsed["scalar_data"]
    }