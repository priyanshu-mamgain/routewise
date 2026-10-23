# RouteWise

Uses Strands Decider 2B to route each question to a cheap or strong Amazon Bedrock model.
Low-confidence decisions escalate to the strong model.

Reusable pattern: `patterns/model_routing/` (see NOTE.md).

Run: `strands-decider serve StrandsAgents/strands-decider-2B-hobson-v21 --port 8000`, then `python router.py`.
Bedrock setup: set AWS_BEARER_TOKEN_BEDROCK, AWS_REGION, CHEAP_MODEL_ID, STRONG_MODEL_ID.