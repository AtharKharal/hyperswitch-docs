# Payments - Post Session Tokens

**Endpoint:** `POST /payments/{payment_id}/post_session_tokens`



**Operation ID:** `Create Post Session Tokens for a Payment`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/{payment_id}/post_session_tokens&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `client_secret` | string | NO | It's a token used for client side verification. |
| `payment_method_type` | string | YES |  |
| `payment_method` | string | YES |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments/{{payment_id}}/post_session_tokens" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "client_secret": "example",
  "payment_method_type": "example",
  "payment_method": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/{payment_id}/post_session_tokens"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "client_secret": "example",
  "payment_method_type": "example",
  "payment_method": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/{payment_id}/post_session_tokens";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "client_secret": "example",
  "payment_method_type": "example",
  "payment_method": "example"
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
