# Organization - Update

**Endpoint:** `PUT /organization/{id}`

Create a new organization for .

**Operation ID:** `Update an Organization`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/organization/{id}&method=PUT" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `organization_name` | string | NO | Name of the organization |
| `organization_details` | object | NO | Details about the organization |
| `metadata` | object | NO | Metadata is useful for storing additional, unstructured information on an object. |
| `platform_merchant_id` | string | YES | Platform merchant id is unique distiguisher for special merchant in the platform org |

## Code Examples

=== "cURL"

```bash
curl -X PUT "https://sandbox.hyperswitch.io/organization/{{id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "organization_name": "example",
  "organization_details": "example",
  "metadata": "example",
  "platform_merchant_id": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/organization/{id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "organization_name": "example",
  "organization_details": "example",
  "metadata": "example",
  "platform_merchant_id": "example"
}
response = requests.put(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/organization/{id}";
const options = {
  method: "PUT",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "organization_name": "example",
  "organization_details": "example",
  "metadata": "example",
  "platform_merchant_id": "example"
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
