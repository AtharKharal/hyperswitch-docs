# Payments - Session token

**Endpoint:** `POST /payments/session_tokens`

Creates a session object or a session token for wallets like Apple Pay, Google Pay, etc. These tokens are used by Hyperswitch's SDK to initiate these wallets' SDK.

**Operation ID:** `Create Session tokens for a Payment`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/session_tokens&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `payment_id` | string | YES | The identifier for the payment |
| `client_secret` | string | NO | This is a token which expires after 15 minutes, used from the client to authenticate and create sessions from the SDK |
| `wallets` | array | YES | The list of the supported wallets |
| `merchant_connector_details` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments/session_tokens" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "payment_id": "example",
  "client_secret": "example",
  "wallets": "example",
  "merchant_connector_details": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/session_tokens"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "payment_id": "example",
  "client_secret": "example",
  "wallets": "example",
  "merchant_connector_details": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/session_tokens";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "payment_id": "example",
  "client_secret": "example",
  "wallets": "example",
  "merchant_connector_details": "example"
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
