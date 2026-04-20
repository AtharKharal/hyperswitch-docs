# Subscription - Pause Subscription

**Endpoint:** `POST /subscriptions/{subscription_id}/pause`

Pause the subscription

**Operation ID:** `Pause Subscription`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/subscriptions/{subscription_id}/pause&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `pause_option` | string | NO |  |
| `pause_at` | string | NO | Optional date when the subscription should be paused (if not provided, pauses immediately) |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/subscriptions/{{subscription_id}}/pause" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "pause_option": "example",
  "pause_at": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/pause"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "pause_option": "example",
  "pause_at": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/pause";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "pause_option": "example",
  "pause_at": "example"
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
