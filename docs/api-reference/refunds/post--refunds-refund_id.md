# Refunds - Update

**Endpoint:** `POST /refunds/{refund_id}`

Updates the properties of a Refund object. This API can be used to attach a reason for the refund or metadata fields

**Operation ID:** `Update a Refund`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/refunds/{refund_id}&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `reason` | string | NO | An arbitrary string attached to the object. Often useful for displaying to users and your customer support executive |
| `metadata` | object | NO | You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long. Metadata is useful for storing additional, structured information on an object. |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/refunds/{{refund_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "reason": "example",
  "metadata": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/refunds/{refund_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "reason": "example",
  "metadata": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/refunds/{refund_id}";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "reason": "example",
  "metadata": "example"
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
