# Profile Acquirer - Update

**Endpoint:** `POST /profile_acquirers/{profile_id}/{profile_acquirer_id}`

Update a Profile Acquirer for accessing our APIs from your servers.

**Operation ID:** `Update a Profile Acquirer`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/profile_acquirers/{profile_id}/{profile_acquirer_id}&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `acquirer_assigned_merchant_id` | string | NO |  |
| `merchant_name` | string | NO |  |
| `network` | string | NO |  |
| `acquirer_bin` | string | NO |  |
| `acquirer_ica` | string | NO |  |
| `acquirer_fraud_rate` | number | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/profile_acquirers/{{profile_id}}/{{profile_acquirer_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "acquirer_assigned_merchant_id": "example",
  "merchant_name": "example",
  "network": "example",
  "acquirer_bin": "example",
  "acquirer_ica": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/profile_acquirers/{profile_id}/{profile_acquirer_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "acquirer_assigned_merchant_id": "example",
  "merchant_name": "example",
  "network": "example",
  "acquirer_bin": "example",
  "acquirer_ica": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/profile_acquirers/{profile_id}/{profile_acquirer_id}";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "acquirer_assigned_merchant_id": "example",
  "merchant_name": "example",
  "network": "example",
  "acquirer_bin": "example",
  "acquirer_ica": "example"
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
