# Gsm - Get

**Endpoint:** `POST /gsm/get`

Retrieves a Gsm Rule

**Operation ID:** `Retrieve Gsm Rule`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/gsm/get&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `connector` | string | YES |  |
| `flow` | string | YES | The flow in which the code and message occurred for a connector |
| `sub_flow` | string | YES | The sub_flow in which the code and message occurred  for a connector |
| `code` | string | YES | code received from the connector |
| `message` | string | YES | message received from the connector |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/gsm/get" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "connector": "example",
  "flow": "example",
  "sub_flow": "example",
  "code": "example",
  "message": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/gsm/get"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "connector": "example",
  "flow": "example",
  "sub_flow": "example",
  "code": "example",
  "message": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/gsm/get";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "connector": "example",
  "flow": "example",
  "sub_flow": "example",
  "code": "example",
  "message": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"id":"obj_xyz","status":"success"}
```

---

*Last updated: 2026-04-19*
