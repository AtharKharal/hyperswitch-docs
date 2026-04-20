# Payments - Incremental Authorization

**Endpoint:** `POST /payments/{payment_id}/incremental_authorization`

Authorized amount for a payment can be incremented if it is in status: requires_capture

**Operation ID:** `Increment authorized amount for a Payment`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/{payment_id}/incremental_authorization&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `amount` | integer | YES | The total amount including previously authorized amount and additional amount |
| `reason` | string | NO | Reason for incremental authorization |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments/{{payment_id}}/incremental_authorization" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "amount": 1000,
  "reason": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/{payment_id}/incremental_authorization"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "amount": 1000,
  "reason": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/{payment_id}/incremental_authorization";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "amount": 1000,
  "reason": "example"
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
