# Payments - Capture

**Endpoint:** `POST /payments/{payment_id}/capture`

Captures the funds for a previously authorized payment intent where `capture_method` was set to `manual` and the payment is in a `requires_capture` state.

Upon successful capture, the payment status usually transitions to `succeeded`.
The `amount_to_capture` can be specified in the request body; it must be less than or equal to the payment's `amount_capturable`. If omitted, the full capturable amount is captured.

A payment must be in a capturable state (e.g., `requires_capture`). Attempting to capture an already `succeeded` (and fully captured) payment or one in an invalid state will lead to an error.


**Operation ID:** `Capture a Payment`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/{payment_id}/capture&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `merchant_id` | string | NO | The unique identifier for the merchant. This is usually inferred from the API key. |
| `amount_to_capture` | integer | NO | The amount to capture, in the lowest denomination of the currency. If omitted, the entire `amount_capturable` of the payment will be captured. Must be less than or equal to the current `amount_capturable`. |
| `refund_uncaptured_amount` | boolean | NO | Decider to refund the uncaptured amount. (Currently not fully supported or behavior may vary by connector). |
| `statement_descriptor_suffix` | string | NO | A dynamic suffix that appears on your customer's credit card statement. This is concatenated with the (shortened) descriptor prefix set on your account to form the complete statement descriptor. The combined length should not exceed connector-specific limits (typically 22 characters). |
| `statement_descriptor_prefix` | string | NO | An optional prefix for the statement descriptor that appears on your customer's credit card statement. This can override the default prefix set on your merchant account. The combined length of prefix and suffix should not exceed connector-specific limits (typically 22 characters). |
| `merchant_connector_details` | string | NO |  |
| `all_keys_required` | boolean | NO | If true, returns stringified connector raw response body |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments/{{payment_id}}/capture" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "merchant_id": "example",
  "amount_to_capture": 1000,
  "refund_uncaptured_amount": false,
  "statement_descriptor_suffix": "example",
  "statement_descriptor_prefix": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/{payment_id}/capture"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "merchant_id": "example",
  "amount_to_capture": 1000,
  "refund_uncaptured_amount": false,
  "statement_descriptor_suffix": "example",
  "statement_descriptor_prefix": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/{payment_id}/capture";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "merchant_id": "example",
  "amount_to_capture": 1000,
  "refund_uncaptured_amount": false,
  "statement_descriptor_suffix": "example",
  "statement_descriptor_prefix": "example"
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
