# Routing - Toggle Contract routing for profile

**Endpoint:** `POST /account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/toggle`

Create a Contract based dynamic routing algorithm

**Operation ID:** `Toggle contract routing algorithm`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/toggle&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `config` | string | NO |  |
| `label_info` | array | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/account/{{account_id}}/business_profile/{{profile_id}}/dynamic_routing/contracts/toggle" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "config": "example",
  "label_info": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/toggle"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "config": "example",
  "label_info": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/toggle";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "config": "example",
  "label_info": "example"
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
