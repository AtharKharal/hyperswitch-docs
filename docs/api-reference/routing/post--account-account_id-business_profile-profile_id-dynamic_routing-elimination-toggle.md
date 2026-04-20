# Routing - Toggle elimination routing for profile

**Endpoint:** `POST /account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/toggle`

Create a elimination based dynamic routing algorithm

**Operation ID:** `Toggle elimination routing algorithm`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/toggle&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/account/{{account_id}}/business_profile/{{profile_id}}/dynamic_routing/elimination/toggle" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/toggle"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.post(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/toggle";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"id":"obj_xyz","status":"success"}
```

---

*Last updated: 2026-04-19*
