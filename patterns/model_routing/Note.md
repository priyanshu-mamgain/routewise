# Model-routing decision pattern (#model-routing)

What it does: Strands Decider 2B scores how complex a request is. Simple requests go to a cheap
Bedrock model, complex ones to a strong model. Scores in the uncertain band (0.45 to 0.55)
escalate to the strong model, so a low-confidence call never degrades answer quality.

How to use:
1. Run the decider server: `strands-decider serve StrandsAgents/strands-decider-2B-hobson-v21 --port 8000`
2. Copy this folder into your agent and call `pick_model(user_text)` before your model call.
3. Map "cheap" and "strong" to your own Bedrock model IDs.
4. Tune LOW and HIGH on your own labeled examples.