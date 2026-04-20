# API Key - Retrieve

**Endpoint:** `GET /api_keys/{merchant_id}/{key_id}`

Retrieve information about the specified API Key.

**Operation ID:** `Retrieve an API Key`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/api_keys/{merchant_id}/{key_id}&method=GET" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X GET "https://sandbox.hyperswitch.io/api_keys/{{merchant_id}}/{{key_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/api_keys/{merchant_id}/{key_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.get(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/api_keys/{merchant_id}/{key_id}";
const options = {
  method: "GET",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"key_id":"key_abc123","name":"Production Key"}
```

---

*Last updated: 2026-04-19*
