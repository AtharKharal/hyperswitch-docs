# API Key - Create

**Endpoint:** `POST /api_keys/{merchant_id}`

Create a new API Key for accessing our APIs from your servers. The plaintext API Key will be
displayed only once on creation, so ensure you store it securely.

**Operation ID:** `Create an API Key`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/api_keys/{merchant_id}&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `name` | string | YES | A unique name for the API Key to help you identify it. |
| `description` | string | NO | A description to provide more context about the API Key. |
| `expiration` | string | YES |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/api_keys/{{merchant_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "name": "example",
  "description": "example",
  "expiration": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/api_keys/{merchant_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "name": "example",
  "description": "example",
  "expiration": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/api_keys/{merchant_id}";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "name": "example",
  "description": "example",
  "expiration": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"key_id":"key_abc123","name":"Production Key"}
```

---

*Last updated: 2026-04-19*
