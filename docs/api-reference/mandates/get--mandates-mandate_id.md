# Mandates - Retrieve Mandate

**Endpoint:** `GET /mandates/{mandate_id}`

Retrieves a mandate created using the Payments/Create API

**Operation ID:** `Retrieve a Mandate`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/mandates/{mandate_id}&method=GET" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X GET "https://sandbox.hyperswitch.io/mandates/{{mandate_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/mandates/{mandate_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.get(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/mandates/{mandate_id}";
const options = {
  method: "GET",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"mandate_id":"mand_xyz123","status":"active","customer_id":"cus_abc123"}
```

---

*Last updated: 2026-04-19*
