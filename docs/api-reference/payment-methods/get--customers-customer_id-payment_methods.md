# List payment methods for a Customer

**Endpoint:** `GET /customers/{customer_id}/payment_methods`

Lists all the applicable payment methods for a particular Customer ID.

**Operation ID:** `List all Payment Methods for a Customer`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/customers/{customer_id}/payment_methods&method=GET" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X GET "https://sandbox.hyperswitch.io/customers/{{customer_id}}/payment_methods" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/customers/{customer_id}/payment_methods"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.get(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/customers/{customer_id}/payment_methods";
const options = {
  method: "GET",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"customer_id":"cus_abc123","email":"customer@example.com","name":"John Doe"}
```

---

*Last updated: 2026-04-19*
