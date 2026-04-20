# Routing - Feedback

**Endpoint:** `POST /routing/feedback`

Update gateway scores for dynamic routing

**Operation ID:** `Update gateway scores`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/routing/feedback&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `merchantId` | string | YES | Profile ID of the merchant |
| `gateway` | string | YES | Payment Gateway identifier |
| `status` | string | YES |  |
| `paymentId` | string | YES | Payment ID associated with the transaction |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/routing/feedback" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "merchantId": "example",
  "gateway": "example",
  "status": "example",
  "paymentId": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/routing/feedback"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "merchantId": "example",
  "gateway": "example",
  "status": "example",
  "paymentId": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/routing/feedback";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "merchantId": "example",
  "gateway": "example",
  "status": "example",
  "paymentId": "example"
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
