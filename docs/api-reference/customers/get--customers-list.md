# Customers - List

**Endpoint:** `GET /customers/list`

Lists all the customers for a particular merchant id.

**Operation ID:** `List all Customers for a Merchant`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/customers/list&method=GET" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X GET "https://sandbox.hyperswitch.io/customers/list" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/customers/list"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.get(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/customers/list";
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
