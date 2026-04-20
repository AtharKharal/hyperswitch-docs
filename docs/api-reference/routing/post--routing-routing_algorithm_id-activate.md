# Routing - Activate config

**Endpoint:** `POST /routing/{routing_algorithm_id}/activate`

Activate a routing config

**Operation ID:** `Activate a routing config`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/routing/{routing_algorithm_id}/activate&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/routing/{{routing_algorithm_id}}/activate" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/routing/{routing_algorithm_id}/activate"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.post(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/routing/{routing_algorithm_id}/activate";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"id":"obj_xyz","status":"success"}
```

---

*Last updated: 2026-04-19*
