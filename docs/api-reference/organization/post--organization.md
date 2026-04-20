# Organization - Create

**Endpoint:** `POST /organization`

Create a new organization

**Operation ID:** `Create an Organization`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/organization&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `organization_name` | string | YES | Name of the organization |
| `organization_details` | object | NO | Details about the organization |
| `metadata` | object | NO | Metadata is useful for storing additional, unstructured information on an object. |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/organization" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "organization_name": "example",
  "organization_details": "example",
  "metadata": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/organization"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "organization_name": "example",
  "organization_details": "example",
  "metadata": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/organization";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "organization_name": "example",
  "organization_details": "example",
  "metadata": "example"
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
