# Routing - Elimination

**Endpoint:** `POST /account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/create`

Create a elimination based dynamic routing algorithm

**Operation ID:** `Create elimination routing algorithm`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/create&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `params` | array | NO |  |
| `elimination_analyser_config` | string | NO |  |
| `decision_engine_configs` | string | YES |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/account/{{account_id}}/business_profile/{{profile_id}}/dynamic_routing/elimination/create" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "params": "example",
  "elimination_analyser_config": "example",
  "decision_engine_configs": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/create"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "params": "example",
  "elimination_analyser_config": "example",
  "decision_engine_configs": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/create";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "params": "example",
  "elimination_analyser_config": "example",
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
