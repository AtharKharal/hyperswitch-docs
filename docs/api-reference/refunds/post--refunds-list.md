# Refunds - List

**Endpoint:** `POST /refunds/list`

Lists all the refunds associated with the merchant, or for a specific payment if payment_id is provided

**Operation ID:** `List all Refunds`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/refunds/list&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/refunds/list" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/refunds/list"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.post(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/refunds/list";
const options = {
  method: "POST",
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
