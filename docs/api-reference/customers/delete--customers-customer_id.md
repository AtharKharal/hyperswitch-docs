# Customers - Delete

**Endpoint:** `DELETE /customers/{customer_id}`

Delete a customer record.

**Operation ID:** `Delete a Customer`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/customers/{customer_id}&method=DELETE" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X DELETE "https://sandbox.hyperswitch.io/customers/{{customer_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/customers/{customer_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.delete(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/customers/{customer_id}";
const options = {
  method: "DELETE",
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
