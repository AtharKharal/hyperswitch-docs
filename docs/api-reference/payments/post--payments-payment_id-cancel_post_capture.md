# Payments - Cancel Post Capture

**Endpoint:** `POST /payments/{payment_id}/cancel_post_capture`

A Payment could can be cancelled when it is in one of these statuses: `succeeded`, `partially_captured`, `partially_captured_and_capturable`.

**Operation ID:** `Cancel a Payment Post Capture`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/{payment_id}/cancel_post_capture&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `cancellation_reason` | string | NO | The reason for the payment cancel |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments/{{payment_id}}/cancel_post_capture" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "cancellation_reason": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/{payment_id}/cancel_post_capture"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "cancellation_reason": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/{payment_id}/cancel_post_capture";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "cancellation_reason": "example"
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
