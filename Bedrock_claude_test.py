import boto3
import json
import compile_prompt

prompt_data = compile_prompt.get_prompt()

bedrock = boto3.client(service_name="bedrock-runtime")
payload = {
    "prompt": f"\n\nHuman:{prompt_data}\n\nAssistant:",
    "max_tokens_to_sample": 512,
    "temperature": 0.8,
    "top_p": 0.8,
}

body = json.dumps(payload)
model_id = "anthropic.claude-v2"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("completion")
print(response_text)