from session_manager import build_session_summary, save_session_json, save_session_df_csv, pdf_from_session
import pandas as pd

class SessionTracker:
    def __init__(self, user_id, role, mode):
        self.user_id = user_id
        self.role = role
        self.mode = mode
        self.qa_records = []

    def add_record(self, question, answer, score, feedback):
        self.qa_records.append({
            "question": question,
            "answer": answer,
            "score": score,
            "feedback": feedback
        })

    def save_session(self):
        if not self.qa_records:
            print("No session records to save.")
            return

        summary = build_session_summary(self.user_id, self.role, self.mode, self.qa_records)

        save_session_json(self.user_id, summary)

        df = pd.DataFrame(summary["qa_records"])
        df["user_id"] = summary["user_id"]
        save_session_df_csv(df)

        try:
            pdf_from_session(summary, f"{self.user_id}_report.pdf")
        except Exception as e:
            print("PDF export skipped:", e)

        print("\nSession saved successfully!")
