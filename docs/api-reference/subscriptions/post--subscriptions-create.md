# Subscription - Create

**Endpoint:** `POST /subscriptions/create`

Creates a subscription that requires separate confirmation.

**Operation ID:** `Create Subscription`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/subscriptions/create&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `merchant_reference_id` | string | NO | Merchant specific Unique identifier. |
| `item_price_id` | string | YES | Identifier for the associated item_price_id for the subscription. |
| `plan_id` | string | NO | Identifier for the subscription plan. |
| `coupon_code` | string | NO | Optional coupon code applied to the subscription. |
| `customer_id` | string | YES |  |
| `payment_details` | string | YES |  |
| `billing` | string | NO |  |
| `shipping` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/subscriptions/create" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "merchant_reference_id": "example",
  "item_price_id": "example",
  "plan_id": "example",
  "coupon_code": "example",
  "customer_id": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/subscriptions/create"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "merchant_reference_id": "example",
  "item_price_id": "example",
  "plan_id": "example",
  "coupon_code": "example",
  "customer_id": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/subscriptions/create";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "merchant_reference_id": "example",
  "item_price_id": "example",
  "plan_id": "example",
  "coupon_code": "example",
  "customer_id": "example"
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
