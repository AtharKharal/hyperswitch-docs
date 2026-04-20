# Subscription - Create and Confirm

**Endpoint:** `POST /subscriptions`

Creates and confirms a subscription in a single request.

**Operation ID:** `Create and Confirm Subscription`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/subscriptions&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `plan_id` | string | NO | Identifier for the associated plan_id. |
| `item_price_id` | string | YES | Identifier for the associated item_price_id for the subscription. |
| `coupon_code` | string | NO | Identifier for the coupon code for the subscription. |
| `customer_id` | string | YES |  |
| `billing` | string | NO |  |
| `shipping` | string | NO |  |
| `payment_details` | string | YES |  |
| `merchant_reference_id` | string | NO | Merchant specific Unique identifier. |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/subscriptions" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "plan_id": "example",
  "item_price_id": "example",
  "coupon_code": "example",
  "customer_id": "example",
  "billing": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/subscriptions"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "plan_id": "example",
  "item_price_id": "example",
  "coupon_code": "example",
  "customer_id": "example",
  "billing": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/subscriptions";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "plan_id": "example",
  "item_price_id": "example",
  "coupon_code": "example",
  "customer_id": "example",
  "billing": "example"
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
