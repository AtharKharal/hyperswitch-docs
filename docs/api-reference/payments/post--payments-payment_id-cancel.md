# Payments - Cancel

**Endpoint:** `POST /payments/{payment_id}/cancel`

A Payment could can be cancelled when it is in one of these statuses: `requires_payment_method`, `requires_capture`, `requires_confirmation`, `requires_customer_action`.

**Operation ID:** `Cancel a Payment`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/{payment_id}/cancel&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `cancellation_reason` | string | NO | The reason for the payment cancel |
| `merchant_connector_details` | string | NO |  |
| `all_keys_required` | boolean | NO | If enabled, provides whole connector response |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments/{{payment_id}}/cancel" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "cancellation_reason": "example",
  "merchant_connector_details": "example",
  "all_keys_required": false
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/{payment_id}/cancel"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "cancellation_reason": "example",
  "merchant_connector_details": "example",
  "all_keys_required": false
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/{payment_id}/cancel";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "cancellation_reason": "example",
  "merchant_connector_details": "example",
  "all_keys_required": false
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
