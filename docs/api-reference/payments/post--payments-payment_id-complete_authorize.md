# Payments - Complete Authorize

**Endpoint:** `POST /payments/{payment_id}/complete_authorize`



**Operation ID:** `Complete Authorize a Payment`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/{payment_id}/complete_authorize&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `shipping` | string | NO |  |
| `client_secret` | string | NO | Client Secret |
| `threeds_method_comp_ind` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments/{{payment_id}}/complete_authorize" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "shipping": "example",
  "client_secret": "example",
  "threeds_method_comp_ind": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/{payment_id}/complete_authorize"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "shipping": "example",
  "client_secret": "example",
  "threeds_method_comp_ind": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/{payment_id}/complete_authorize";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "shipping": "example",
  "client_secret": "example",
  "threeds_method_comp_ind": "example"
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
