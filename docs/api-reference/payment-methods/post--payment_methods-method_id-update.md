# Payment Method - Update

**Endpoint:** `POST /payment_methods/{method_id}/update`

Update an existing payment method of a customer.
This API is useful for use cases such as updating the card number for expired cards to prevent discontinuity in recurring payments.

**Operation ID:** `Update a Payment method`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payment_methods/{method_id}/update&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `card` | string | NO |  |
| `wallet` | string | NO |  |
| `client_secret` | string | NO | This is a 15 minute expiry token which shall be used from the client to authenticate and perform sessions from the SDK |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payment_methods/{{method_id}}/update" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "card": "example",
  "wallet": "example",
  "client_secret": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payment_methods/{method_id}/update"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "card": "example",
  "wallet": "example",
  "client_secret": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payment_methods/{method_id}/update";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "card": "example",
  "wallet": "example",
  "client_secret": "example"
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
