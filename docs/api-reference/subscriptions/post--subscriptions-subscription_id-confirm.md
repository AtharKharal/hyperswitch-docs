# Subscription - Confirm

**Endpoint:** `POST /subscriptions/{subscription_id}/confirm`

Confirms a previously created subscription.

**Operation ID:** `Confirm Subscription`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/subscriptions/{subscription_id}/confirm&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `client_secret` | string | NO | This is a token which expires after 15 minutes, used from the client to authenticate and create sessions from the SDK |
| `payment_details` | string | YES |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/subscriptions/{{subscription_id}}/confirm" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "client_secret": "example",
  "payment_details": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/confirm"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "client_secret": "example",
  "payment_details": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/confirm";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "client_secret": "example",
  "payment_details": "example"
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
