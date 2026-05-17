from fastapi import FastAPI
from search import search

app = FastAPI()

# ---------------- HEALTH CHECK ----------------
@app.get("/health")
def health():
    return {"status": "ok"}

# ---------------- CHAT ENDPOINT ----------------
@app.post("/chat")
def chat(payload: dict):

    messages = payload["messages"]

    # take last user message
    user_input = messages[-1]["content"]

    # search SHL catalog
    results = search(user_input, k=5)

    recommendations = []

    for r in results:
        recommendations.append({
            "name": r["name"],
            "url": r["url"]
        })

    return {
        "reply": "Here are relevant SHL assessments based on your request.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }
