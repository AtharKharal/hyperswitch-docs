# Subscription - Cancel Subscription

**Endpoint:** `POST /subscriptions/{subscription_id}/cancel`

Cancel the subscription

**Operation ID:** `Cancel Subscription`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/subscriptions/{subscription_id}/cancel&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `cancel_option` | string | NO |  |
| `cancel_at` | string | NO | Optional date when the subscription should be cancelled (if not provided, cancels immediately) |
| `unbilled_charges_option` | string | NO |  |
| `credit_option_for_current_term_charges` | string | NO |  |
| `account_receivables_handling` | string | NO |  |
| `refundable_credits_handling` | string | NO |  |
| `cancel_reason_code` | string | NO | Reason code for canceling the subscription |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/subscriptions/{{subscription_id}}/cancel" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "cancel_option": "example",
  "cancel_at": "example",
  "unbilled_charges_option": "example",
  "credit_option_for_current_term_charges": "example",
  "account_receivables_handling": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/cancel"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "cancel_option": "example",
  "cancel_at": "example",
  "unbilled_charges_option": "example",
  "credit_option_for_current_term_charges": "example",
  "account_receivables_handling": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/cancel";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "cancel_option": "example",
  "cancel_at": "example",
  "unbilled_charges_option": "example",
  "credit_option_for_current_term_charges": "example",
  "account_receivables_handling": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"subscription_id":"sub_xyz123","status":"active"}
```

---

*Last updated: 2026-04-19*
