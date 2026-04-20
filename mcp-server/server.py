#!/usr/bin/env python3
"""
HyperSwitch MCP Server
Exposes HyperSwitch documentation as queryable tools for AI agents
"""
import json
import asyncio
from typing import Any, Optional
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"
BASE_URL = "https://sandbox.hyperswitch.io"


def create_payment_tool(params: dict) -> dict:
    """Generate cURL/Python/JS code for creating a payment"""
    template = {
        "curl": f'''curl -X POST "{BASE_URL}/payments" \\
  -H "Content-Type: application/json" \\
  -H "api-key: YOUR_API_KEY" \\
  -d '{json.dumps({"amount": params.get("amount"), "currency": params.get("currency")}, indent=2)}' ''',
        "python": f'''import requests

url = "{BASE_URL}/payments"
headers = {{
    "Content-Type": "application/json",
    "api-key": "YOUR_API_KEY"
}}
payload = {json.dumps(params, indent=4)}

response = requests.post(url, json=payload, headers=headers)
print(response.json())'''.replace("{", "{{").replace("}", "}}"),
        "javascript": f'''const axios = require("axios");

const response = await axios.post("{BASE_URL}/payments", {{
  amount: {params.get("amount")},
  currency: "{params.get("currency")}"
}}, {{
  headers: {{ "api-key": "YOUR_API_KEY" }}
}});'''
    }
    return template


def get_customer_tool(customer_id: str) -> dict:
    """Generate code for retrieving a customer"""
    return {
        "curl": f'curl -X GET "{BASE_URL}/customers/{customer_id}" -H "api-key: YOUR_API_KEY"',
        "python": f'''import requests
response = requests.get(
    "{BASE_URL}/customers/{customer_id}",
    headers={{"api-key": "YOUR_API_KEY"}}
)
print(response.json())''',
        "javascript": f'''const customer = await axios.get(
  "{BASE_URL}/customers/{customer_id}",
  {{headers: {{"api-key": "YOUR_API_KEY"}}}}
);'''
    }


def create_customer_tool(params: dict) -> dict:
    """Generate code for creating a customer"""
    return {
        "curl": f'''curl -X POST "{BASE_URL}/customers" \\
  -H "Content-Type: application/json" \\
  -H "api-key: YOUR_API_KEY" \\
  -d '{json.dumps({"email": params.get("email"), "name": params.get("name", ""), "phone": params.get("phone", "")}, indent=2)}' ''',
        "python": f'''import requests
response = requests.post(
    "{BASE_URL}/customers",
    json={json.dumps(params, indent=4)},
    headers={{"api-key": "YOUR_API_KEY"}}
)''',
        "javascript": f'''const customer = await axios.post(
  "{BASE_URL}/customers",
  {json.dumps(params, indent=4)},
  {{headers: {{"api-key": "YOUR_API_KEY"}}}}
);'''
    }


def process_refund_tool(params: dict) -> dict:
    """Generate code for processing a refund"""
    return {
        "curl": f'''curl -X POST "{BASE_URL}/refs" \\
  -H "Content-Type: application/json" \\
  -H "api-key: YOUR_API_KEY" \\
  -d '{json.dumps(params, indent=2)}' ''',
        "python": f'''import requests
response = requests.post(
    "{BASE_URL}/refunds",
    json={json.dumps(params, indent=4)},
    headers={{"api-key": "YOUR_API_KEY"}}
)''',
        "javascript": f'''const refund = await axios.post(
  "{BASE_URL}/refunds",
  {json.dumps(params, indent=4)},
  {{headers: {{"api-key": "YOUR_API_KEY"}}}}
);'''
    }


def configure_routing_tool(params: dict) -> dict:
    """Generate code for configuring smart routing"""
    body = {
        "name": params.get("profile_name", "Default Routing"),
        "rules": [
            {
                "name": f"Route via {connector}",
                "action": {"type": "route_to", "connector": connector},
                "priority": idx + 1
            }
            for idx, connector in enumerate(params.get("connectors", []))
        ]
    }
    return {
        "curl": f'''curl -X POST "{BASE_URL}/routing" \\
  -H "Content-Type: application/json" \\
  -H "api-key: YOUR_API_KEY" \\
  -d '{json.dumps(body, indent=2)}' '''
    }


def verify_webhook_tool(params: dict) -> dict:
    """Generate code for webhook verification"""
    return {
        "python": '''import hmac
import hashlib

def verify_webhook(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, expected)

# Usage:
# payload = request.body
# signature = request.headers["x-hyperswitch-signature"]
# is_valid = verify_webhook(payload, signature, "whsec_your_secret")''',
        "javascript": '''const crypto = require("crypto");

function verifyWebhook(payload, signature, secret) {
  const expected = crypto
    .createHmac("sha256", secret)
    .update(payload)
    .digest("hex");
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expected)
  );
}

// Usage:
// const isValid = verifyWebhook(payload, signature, "whsec_your_secret");'''
    }


async def handle_tool_call(tool_name: str, params: dict) -> dict:
    """Handle MCP tool calls"""
    handlers = {
        "create_payment": create_payment_tool,
        "get_customer": lambda p: get_customer_tool(p.get("customer_id", "")),
        "create_customer": create_customer_tool,
        "process_refund": process_refund_tool,
        "configure_routing": configure_routing_tool,
        "verify_webhook": verify_webhook_tool,
    }
    
    handler = handlers.get(tool_name)
    if handler:
        return {"success": True, "code": handler(params)}
    return {"success": False, "error": f"Unknown tool: {tool_name}"}


async def handle_resource(uri: str) -> dict:
    """Handle MCP resource requests"""
    docs_map = {
        "docs://tutorials/quickstart": "tutorials/quickstart.md",
        "docs::api-reference/payments": "api-reference/payments/post--payments.md",
        "docs::api-reference/customers": "api-reference/customers/post--customers.md",
        "docs::api-reference/refunds": "api-reference/refunds/post--refunds.md",
        "docs::explanation/authentication": "explanation/authentication.md",
    }
    
    doc_file = docs_map.get(uri)
    if doc_file:
        path = DOCS_DIR / doc_file
        if path.exists():
            return {"success": True, "content": path.read_text(encoding="utf-8")}
    
    return {"success": False, "error": f"Resource not found: {uri}"}


def main():
    """MCP server entry point"""
    print("HyperSwitch MCP Server starting...")
    print(f"Serving docs from: {DOCS_DIR}")
    print("Available tools: create_payment, get_customer, create_customer, process_refund, configure_routing, verify_webhook")
    print("Available resources: docs::tutorials/quickstart, docs::api-reference/*")
    
    while True:
        try:
            line = input("\n> ")
            if not line.strip():
                continue
            
            msg = json.loads(line)
            method = msg.get("method")
            params = msg.get("params", {})
            
            if method == "tools/call":
                result = asyncio.run(handle_tool_call(params.get("tool"), params.get("arguments", {})))
                print(json.dumps(result))
            elif method == "resources/read":
                result = asyncio.run(handle_resource(params.get("uri")))
                print(json.dumps(result))
            else:
                print(json.dumps({"error": f"Unknown method: {method}"}))
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(json.dumps({"error": str(e)}))


if __name__ == "__main__":
    main()