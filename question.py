# The typed question and option set for the model-routing decision.
QUESTION_ID = "is_complex"
QUESTION_TYPE = "noul"   # yes/no score between 0 and 1
INSTRUCTIONS = (
    "Does answering this need deep multi-step reasoning "
    "or a long detailed explanation?"
)
# score <= LOW  -> cheap model
# score >= HIGH -> strong model
# in between    -> low confidence, escalate to strong model
LOW, HIGH = 0.45, 0.55