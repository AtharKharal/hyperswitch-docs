# Profile Acquirer - Create

**Endpoint:** `POST /profile_acquirers`

Create a new Profile Acquirer for accessing our APIs from your servers.

**Operation ID:** `Create a Profile Acquirer`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/profile_acquirers&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `acquirer_assigned_merchant_id` | string | YES | The merchant id assigned by the acquirer |
| `merchant_name` | string | YES | merchant name |
| `network` | string | YES | Network provider |
| `acquirer_bin` | string | YES | Acquirer bin |
| `acquirer_ica` | string | NO | Acquirer ica provided by acquirer |
| `acquirer_fraud_rate` | number | YES | Fraud rate for the particular acquirer configuration |
| `profile_id` | string | YES | Parent profile id to link the acquirer account with |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/profile_acquirers" \
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

url = "https://sandbox.hyperswitch.io/profile_acquirers"
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
const url = "https://sandbox.hyperswitch.io/profile_acquirers";
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
