import boto3
import json

prompt_data = """
Create a JsON which lists two vulnerabilities. One with an ssh port open to the internet and one with a expired certificate. 
They are found on ip 123.12.1.123.
Respond with pure JSON. The JSON object should be compatible with the TypeScript type Response from the following:
interface Response {
Pentestresults: {
// Relevant finding from pentest:
observations: string;
// Description of finding:
description: string;
// estimated CVSS:
score: string;
// Short markdown-style bullet list that conveys the mitigation plan
plan: string;
// Summary of thoughts, to say to user
speak: string;
};
"""

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