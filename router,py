import httpx

DECIDER_URL = "http://localhost:8000/v1/systemone"

QUESTION = (
    "Does answering this need deep multi-step reasoning "
    "or a long detailed explanation?"
)

def decide(text: str) -> dict:
    body = {
        "state": text,
        "questions": {"is_complex": {"type": "noul", "instructions": QUESTION}},
    }
    r = httpx.post(DECIDER_URL, json=body, timeout=60)
    r.raise_for_status()
    data = r.json()
    p = data["answers"]["is_complex"]["noul"]   # 0..1, 1 = complex
    return {"p_complex": p, "decider_ms": data.get("latency_ms")}

def route(text: str, low=0.30, high=0.70) -> dict:
    d = decide(text)
    p = d["p_complex"]
    if p <= low:
        tier, reason = "cheap", "confident: simple"
    elif p >= high:
        tier, reason = "strong", "confident: complex"
    else:
        tier, reason = "strong", "low confidence, escalated"
    return {**d, "tier": tier, "reason": reason}

if __name__ == "__main__":
    for t in ["What is a stack?",
              "Explain how deadlock detection works and compare it with prevention.",
              "recursion kya hota hai?"]:
        print(t, "->", route(t))