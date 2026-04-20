# 3DS Decision - Execute

**Endpoint:** `POST /three_ds_decision/execute`



**Operation ID:** `Execute 3DS Decision Rule`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/three_ds_decision/execute&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `routing_id` | string | YES | The ID of the routing algorithm to be executed. |
| `payment` | string | YES |  |
| `payment_method` | string | NO |  |
| `customer_device` | string | NO |  |
| `issuer` | string | NO |  |
| `acquirer` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/three_ds_decision/execute" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "routing_id": "example",
  "payment": "example",
  "payment_method": "example",
  "customer_device": "example",
  "issuer": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/three_ds_decision/execute"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "routing_id": "example",
  "payment": "example",
  "payment_method": "example",
  "customer_device": "example",
  "issuer": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/three_ds_decision/execute";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "routing_id": "example",
  "payment": "example",
  "payment_method": "example",
  "customer_device": "example",
  "issuer": "example"
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
