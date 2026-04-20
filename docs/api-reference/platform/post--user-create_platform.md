# Platform - Create

**Endpoint:** `POST /user/create_platform`

Create a new platform account

**Operation ID:** `Create a Platform Account`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/user/create_platform&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `organization_name` | string | YES |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/user/create_platform" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "organization_name": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/user/create_platform"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "organization_name": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/user/create_platform";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "organization_name": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"id":"obj_xyz","status":"success"}
```

---

*Last updated: 2026-04-19*
