# Mandates - Revoke Mandate

**Endpoint:** `POST /mandates/revoke/{mandate_id}`

Revokes a mandate created using the Payments/Create API

**Operation ID:** `Revoke a Mandate`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/mandates/revoke/{mandate_id}&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/mandates/revoke/{{mandate_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/mandates/revoke/{mandate_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.post(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/mandates/revoke/{mandate_id}";
const options = {
  method: "POST",
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
