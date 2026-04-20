# Merchant Account - KV Status

**Endpoint:** `POST /accounts/{account_id}/kv`

Toggle KV mode for the Merchant Account

**Operation ID:** `Enable/Disable KV for a Merchant Account`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/accounts/{account_id}/kv&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `kv_enabled` | boolean | YES | Status of KV for the specific merchant |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/accounts/{{account_id}}/kv" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "kv_enabled": false
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/accounts/{account_id}/kv"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "kv_enabled": false
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/accounts/{account_id}/kv";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "kv_enabled": false
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
