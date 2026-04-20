# Routing - Evaluate

**Endpoint:** `POST /routing/evaluate`

Evaluate routing rules

**Operation ID:** `Evaluate routing rules`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/routing/evaluate&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `paymentInfo` | string | YES |  |
| `merchantId` | string | YES | Profile ID of the merchant |
| `eligibleGatewayList` | array | NO | List of eligible gateways for routing consideration |
| `rankingAlgorithm` | string | NO |  |
| `eliminationEnabled` | boolean | NO | Whether elimination logic is enabled for filtering gateways |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/routing/evaluate" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "paymentInfo": "example",
  "merchantId": "example",
  "eligibleGatewayList": "example",
  "rankingAlgorithm": "example",
  "eliminationEnabled": false
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/routing/evaluate"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "paymentInfo": "example",
  "merchantId": "example",
  "eligibleGatewayList": "example",
  "rankingAlgorithm": "example",
  "eliminationEnabled": false
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/routing/evaluate";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "paymentInfo": "example",
  "merchantId": "example",
  "eligibleGatewayList": "example",
  "rankingAlgorithm": "example",
  "eliminationEnabled": false
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
