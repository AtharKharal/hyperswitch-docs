# Refunds - Create

**Endpoint:** `POST /refunds`

Creates a refund against an already processed payment. In case of some processors, you can even opt to refund only a partial amount multiple times until the original charge amount has been refunded

**Operation ID:** `Create a Refund`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/refunds&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Try It Now

<div class="api-playground" data-endpoint="/refunds" data-method="POST">
  <div class="playground-form">
    <div class="form-group">
      <label>API Key</label>
      <input type="password" name="api-key" placeholder="sk_test_..." />
    </div>
    <div class="form-group">
      <label>Payment ID</label>
      <input type="text" name="payment_id" placeholder="pay_abc123" />
    </div>
    <div class="form-group">
      <label>Amount</label>
      <input type="number" name="amount" placeholder="1000" />
    </div>
    <div class="form-group">
      <label>Reason</label>
      <input type="text" name="reason" placeholder="requested_by_customer" />
    </div>
    <button type="button" class="execute-btn">Execute Request</button>
  </div>
  <div class="response-section" style="display:none;">
    <label>Response</label>
    <pre class="response-output"></pre>
  </div>
</div>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `payment_id` | string | YES | The payment id against which refund is to be initiated |
| `refund_id` | string | NO | Unique Identifier for the Refund. This is to ensure idempotency for multiple partial refunds initiated against the same payment. If this is not passed by the merchant, this field shall be auto generated and provided in the API response. It is recommended to generate uuid(v4) as the refund_id. |
| `merchant_id` | string | NO | The identifier for the Merchant Account |
| `amount` | integer | NO | Total amount for which the refund is to be initiated. Amount for the payment in lowest denomination of the currency. (i.e) in cents for USD denomination, in paisa for INR denomination etc., If not provided, this will default to the full payment amount |
| `reason` | string | NO | Reason for the refund. Often useful for displaying to users and your customer support executive. In case the payment went through Stripe, this field needs to be passed with one of these enums: `duplicate`, `fraudulent`, or `requested_by_customer` |
| `refund_type` | string | NO |  |
| `metadata` | object | NO | You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long. Metadata is useful for storing additional, structured information on an object. |
| `merchant_connector_details` | string | NO |  |
| `split_refunds` | string | NO |  |
| `all_keys_required` | boolean | NO | If true, returns stringified connector raw response body |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/refunds" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "payment_id": "example",
  "refund_id": "example",
  "merchant_id": "example",
  "amount": 1000,
  "reason": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/refunds"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "payment_id": "example",
  "refund_id": "example",
  "merchant_id": "example",
  "amount": 1000,
  "reason": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/refunds";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "payment_id": "example",
  "refund_id": "example",
  "merchant_id": "example",
  "amount": 1000,
  "reason": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"refund_id":"ref_xyz789","payment_id":"pay_abc123xyz","amount":6540,"currency":"USD","status":"succeeded"}
```

---

*Last updated: 2026-04-19*
