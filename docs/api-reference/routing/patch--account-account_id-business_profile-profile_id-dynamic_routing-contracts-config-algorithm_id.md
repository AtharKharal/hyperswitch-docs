# Routing - Update contract based dynamic routing config for profile

**Endpoint:** `PATCH /account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/config/{algorithm_id}`

Update contract based dynamic routing algorithm

**Operation ID:** `Update contract based dynamic routing configs`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/config/{algorithm_id}&method=PATCH" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `config` | string | NO |  |
| `label_info` | array | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X PATCH "https://sandbox.hyperswitch.io/account/{{account_id}}/business_profile/{{profile_id}}/dynamic_routing/contracts/config/{{algorithm_id}}" \
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

url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/config/{algorithm_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "config": "example",
  "label_info": "example"
}
response = requests.patch(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/config/{algorithm_id}";
const options = {
  method: "PATCH",
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
