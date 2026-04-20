# Payments - Submit Eligibility Data

**Endpoint:** `POST /payments/{payment_id}/eligibility`



**Operation ID:** `Submit Eligibility data for a Payment`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/{payment_id}/eligibility&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `client_secret` | string | YES | Token used for client side verification |
| `payment_method_type` | string | YES |  |
| `payment_method_subtype` | string | NO |  |
| `payment_method_data` | string | YES |  |
| `browser_info` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments/{{payment_id}}/eligibility" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "client_secret": "example",
  "payment_method_type": "example",
  "payment_method_subtype": "example",
  "payment_method_data": "example",
  "browser_info": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/{payment_id}/eligibility"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "client_secret": "example",
  "payment_method_type": "example",
  "payment_method_subtype": "example",
  "payment_method_data": "example",
  "browser_info": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/{payment_id}/eligibility";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "client_secret": "example",
  "payment_method_type": "example",
  "payment_method_subtype": "example",
  "payment_method_data": "example",
  "browser_info": "example"
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
