# Relay - Create

**Endpoint:** `POST /relay`

Creates a relay request.

**Operation ID:** `Relay Request`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/relay&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `connector_resource_id` | string | YES | The identifier that is associated to a resource at the connector reference to which the relay request is being made |
| `connector_id` | string | YES | Identifier of the connector ( merchant connector account ) which was chosen to make the payment |
| `type` | string | YES |  |
| `data` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/relay" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "connector_resource_id": "example",
  "connector_id": "example",
  "type": "example",
  "data": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/relay"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "connector_resource_id": "example",
  "connector_id": "example",
  "type": "example",
  "data": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/relay";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "connector_resource_id": "example",
  "connector_id": "example",
  "type": "example",
  "data": "example"
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
