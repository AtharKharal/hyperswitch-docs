# Payments - List

**Endpoint:** `GET /payments/list`

To list the *payments*

**Operation ID:** `List all Payments`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments/list&method=GET" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X GET "https://sandbox.hyperswitch.io/payments/list" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments/list"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.get(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments/list";
const options = {
  method: "GET",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"payment_id":"pay_abc123xyz","status":"requires_payment_method","client_secret":"pi_secret_xyz","amount":6540,"currency":"USD"}
```

---

*Last updated: 2026-04-19*
