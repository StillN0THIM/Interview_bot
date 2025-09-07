"""
Session Management Module for Interview Preparation Bot

Dependencies:
pip install pandas python-dotenv fpdf
"""

import os
import json
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Optional PDF
try:
    from fpdf import FPDF
    FPDF_AVAILABLE = True
except ImportError:
    FPDF_AVAILABLE = False

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Directory for sessions
os.makedirs("sessions", exist_ok=True)


# ---------------- Session Storage ----------------
def save_session_json(user_id, session_data):
    """Save session data to per-user JSON history file."""
    path = os.path.join("sessions", f"{user_id}.json")
    existing = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            existing = json.load(f)
    existing.append(session_data)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    return path


def save_session_df_csv(df, filename="session_records.csv"):
    """Append session DataFrame to global CSV file."""
    if os.path.exists(filename):
        df.to_csv(filename, mode="a", header=False, index=False)
    else:
        df.to_csv(filename, index=False)
    return filename


# ---------------- PDF Export ----------------
def pdf_from_session(session_summary, filename="report.pdf"):
    """Export session summary to PDF (if fpdf installed)."""
    if not FPDF_AVAILABLE:
        raise RuntimeError("fpdf not installed. Run: pip install fpdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Interview Bot Report", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"User: {session_summary['user_id']}", ln=True)
    pdf.cell(0, 8, f"Role: {session_summary['role']} | Mode: {session_summary['mode']}", ln=True)
    pdf.cell(0, 8, f"Date: {session_summary['timestamp']}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Questions & Feedback", ln=True)
    pdf.set_font("Arial", "", 11)

    for rec in session_summary["qa_records"]:
        pdf.multi_cell(0, 6, f"Q: {rec['question']}")
        pdf.multi_cell(0, 6, f"A: {rec['answer']}")
        pdf.multi_cell(0, 6, f"Score: {rec.get('score','-')} | Feedback: {rec.get('feedback','-')}")
        pdf.ln(2)

    pdf.ln(4)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Summary", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6, session_summary.get("summary", "-"))

    pdf.output(filename)
    return filename


# ---------------- Helper: Build Summary ----------------
def build_session_summary(user_id, role, mode, qa_records):
    """Summarize a session for export."""
    total, count = 0, 0
    for r in qa_records:
        if r.get("score") is not None:
            total += r["score"]
            count += 1
    avg_score = round(total / count, 1) if count else None

    summary = {
        "user_id": user_id,
        "role": role,
        "mode": mode,
        "timestamp": datetime.now().isoformat(),
        "avg_score": avg_score,
        "qa_records": qa_records,
        "summary": f"Average Score: {avg_score}/10" if avg_score else "No answers scored.",
    }
    return summary


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    # Example dummy data
    qa_records = [
        {"question": "What is Python?", "answer": "A programming language.", "score": 8, "feedback": "Good answer."},
        {"question": "Explain OOP.", "answer": "Encapsulation, Inheritance, etc.", "score": 7, "feedback": "Add real examples."},
    ]

    summary = build_session_summary("user123", "Software Engineer", "Technical", qa_records)

    # Save JSON history
    save_session_json("user123", summary)

    # Save CSV
    df = pd.DataFrame(summary["qa_records"])
    df["user_id"] = summary["user_id"]
    save_session_df_csv(df)

    # Export PDF
    if FPDF_AVAILABLE:
        pdf_from_session(summary, "sample_report.pdf")

    print("Session tracking complete!")
