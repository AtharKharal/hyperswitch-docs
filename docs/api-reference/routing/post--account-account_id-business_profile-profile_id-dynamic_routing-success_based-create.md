# Routing - Auth Rate Based

**Endpoint:** `POST /account/{account_id}/business_profile/{profile_id}/dynamic_routing/success_based/create`

Create a success based dynamic routing algorithm

**Operation ID:** `Create success based dynamic routing algorithm`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/business_profile/{profile_id}/dynamic_routing/success_based/create&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `params` | array | NO |  |
| `config` | string | NO |  |
| `decision_engine_configs` | string | YES |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/account/{{account_id}}/business_profile/{{profile_id}}/dynamic_routing/success_based/create" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "params": "example",
  "config": "example",
  "decision_engine_configs": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/success_based/create"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "params": "example",
  "config": "example",
  "decision_engine_configs": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/success_based/create";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "params": "example",
  "config": "example",
  "decision_engine_configs": "example"
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
