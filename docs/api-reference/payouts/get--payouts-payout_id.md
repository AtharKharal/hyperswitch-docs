# Payouts - Retrieve

**Endpoint:** `GET /payouts/{payout_id}`



**Operation ID:** `Retrieve a Payout`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payouts/{payout_id}&method=GET" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X GET "https://sandbox.hyperswitch.io/payouts/{{payout_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payouts/{payout_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.get(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payouts/{payout_id}";
const options = {
  method: "GET",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"payout_id":"pout_xyz456","status":"pending","amount":50000}
```

---

*Last updated: 2026-04-19*
