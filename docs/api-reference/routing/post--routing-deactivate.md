# Routing - Deactivate

**Endpoint:** `POST /routing/deactivate`

Deactivates a routing config

**Operation ID:** `Deactivate a routing config`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/routing/deactivate&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `name` | string | NO | Unique name of the routing configuration.

This identifier is used to reference the routing config internally.

Example:
```json
"default_card_routing"
``` |
| `description` | string | NO | Optional human-readable description of the routing configuration.

Example:
```json
"Primary routing strategy for card payments in India"
``` |
| `algorithm` | string | NO |  |
| `profile_id` | string | NO | Profile ID associated with this routing configuration.

Routing configs can be scoped per business profile.

Example:
```json
"profile_123"
``` |
| `transaction_type` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/routing/deactivate" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "name": "example",
  "description": "example",
  "algorithm": "example",
  "profile_id": "example",
  "transaction_type": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/routing/deactivate"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "name": "example",
  "description": "example",
  "algorithm": "example",
  "profile_id": "example",
  "transaction_type": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/routing/deactivate";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "name": "example",
  "description": "example",
  "algorithm": "example",
  "profile_id": "example",
  "transaction_type": "example"
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
