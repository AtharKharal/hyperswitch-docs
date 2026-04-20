# Refunds - Retrieve

**Endpoint:** `GET /refunds/{refund_id}`

Retrieves a Refund. This may be used to get the status of a previously initiated refund

**Operation ID:** `Retrieve a Refund`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/refunds/{refund_id}&method=GET" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X GET "https://sandbox.hyperswitch.io/refunds/{{refund_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/refunds/{refund_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.get(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/refunds/{refund_id}";
const options = {
  method: "GET",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"refund_id":"ref_xyz789","payment_id":"pay_abc123xyz","amount":6540,"currency":"USD","status":"succeeded"}
```

---

*Last updated: 2026-04-19*
