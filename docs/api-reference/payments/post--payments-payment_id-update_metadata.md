# Payments - Update Metadata

**Endpoint:** `POST /payments/{payment_id}/update_metadata`



**Operation ID:** `Update Metadata for a Payment`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/{payment_id}/update_metadata&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `metadata` | object | YES | Metadata is useful for storing additional, unstructured information on an object. |
| `feature_metadata` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments/{{payment_id}}/update_metadata" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "metadata": "example",
  "feature_metadata": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/{payment_id}/update_metadata"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "metadata": "example",
  "feature_metadata": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/{payment_id}/update_metadata";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "metadata": "example",
  "feature_metadata": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"payment_id":"pay_abc123xyz","status":"requires_payment_method","client_secret":"pi_secret_xyz","amount":6540,"currency":"USD"}
```

---

*Last updated: 2026-04-19*
