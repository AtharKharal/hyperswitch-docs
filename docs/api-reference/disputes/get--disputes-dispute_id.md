# Disputes - Retrieve Dispute

**Endpoint:** `GET /disputes/{dispute_id}`

Retrieves a dispute

**Operation ID:** `Retrieve a Dispute`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/disputes/{dispute_id}&method=GET" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X GET "https://sandbox.hyperswitch.io/disputes/{{dispute_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/disputes/{dispute_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.get(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/disputes/{dispute_id}";
const options = {
  method: "GET",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"dispute_id":"disp_xyz789","status":"needs_response"}
```

---

*Last updated: 2026-04-19*
