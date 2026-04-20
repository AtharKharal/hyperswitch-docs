# PaymentMethods - Create

**Endpoint:** `POST /payment_methods`

Creates and stores a payment method against a customer.
In case of cards, this API should be used only by PCI compliant merchants.

**Operation ID:** `Create a Payment Method`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payment_methods&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `payment_method` | string | YES |  |
| `payment_method_type` | string | NO |  |
| `payment_method_issuer` | string | NO | The name of the bank/ provider issuing the payment method to the end user |
| `payment_method_issuer_code` | string | NO |  |
| `card` | string | NO |  |
| `metadata` | object | NO | You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long. Metadata is useful for storing additional, structured information on an object. |
| `customer_id` | string | NO | The unique identifier of the customer. |
| `card_network` | string | NO | The card network |
| `bank_transfer` | string | NO |  |
| `bank_transfer_data` | string | NO |  |
| `wallet` | string | NO |  |
| `client_secret` | string | NO | For Client based calls, SDK will use the client_secret
in order to call /payment_methods
Client secret will be generated whenever a new
payment method is created |
| `payment_method_data` | string | NO |  |
| `billing` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payment_methods" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "payment_method": "example",
  "payment_method_type": "example",
  "payment_method_issuer": "example",
  "payment_method_issuer_code": "example",
  "card": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payment_methods"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "payment_method": "example",
  "payment_method_type": "example",
  "payment_method_issuer": "example",
  "payment_method_issuer_code": "example",
  "card": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payment_methods";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "payment_method": "example",
  "payment_method_type": "example",
  "payment_method_issuer": "example",
  "payment_method_issuer_code": "example",
  "card": "example"
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
