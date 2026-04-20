# Subscription - Update

**Endpoint:** `PUT /subscriptions/{subscription_id}/update`

Updates an existing subscription.

**Operation ID:** `Update Subscription`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/subscriptions/{subscription_id}/update&method=PUT" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `plan_id` | string | YES | Identifier for the associated plan_id. |
| `item_price_id` | string | YES | Identifier for the associated item_price_id for the subscription. |

## Code Examples

=== "cURL"

```bash
curl -X PUT "https://sandbox.hyperswitch.io/subscriptions/{{subscription_id}}/update" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "plan_id": "example",
  "item_price_id": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/update"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "plan_id": "example",
  "item_price_id": "example"
}
response = requests.put(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/update";
const options = {
  method: "PUT",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "plan_id": "example",
  "item_price_id": "example"
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
