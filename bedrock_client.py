import os, time, boto3

client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))
CHEAP_MODEL = os.getenv("CHEAP_MODEL_ID")
STRONG_MODEL = os.getenv("STRONG_MODEL_ID")

def ask(model_id: str, question: str) -> dict:
    t0 = time.time()
    out = client.converse(
        modelId=model_id,
        messages=[{"role": "user", "content": [{"text": question}]}],
        inferenceConfig={"maxTokens": 512},
    )
    return {
        "text": out["output"]["message"]["content"][0]["text"],
        "input_tokens": out["usage"]["inputTokens"],
        "output_tokens": out["usage"]["outputTokens"],
        "latency_s": round(time.time() - t0, 2),
    }