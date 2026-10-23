import httpx
from question import QUESTION_ID, QUESTION_TYPE, INSTRUCTIONS, LOW, HIGH

def pick_model(text, decider_url="http://localhost:8000/v1/systemone"):
    """Put this in front of any agent: returns 'cheap' or 'strong' plus the score."""
    body = {"state": text, "questions": {QUESTION_ID: {"type": QUESTION_TYPE, "instructions": INSTRUCTIONS}}}
    r = httpx.post(decider_url, json=body, timeout=60)
    r.raise_for_status()
    p = r.json()["answers"][QUESTION_ID]["noul"]
    if p <= LOW:
        return "cheap", p, "confident: simple"
    if p >= HIGH:
        return "strong", p, "confident: complex"
    return "strong", p, "low confidence, escalated"