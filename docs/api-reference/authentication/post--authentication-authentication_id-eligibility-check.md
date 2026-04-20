# Authentication - POST Eligibility Check

**Endpoint:** `POST /authentication/{authentication_id}/eligibility-check`



**Operation ID:** `Submit Eligibility for an Authentication`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/authentication/{authentication_id}/eligibility-check&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `client_secret` | string | NO | Optional secret value used to identify and authorize the client making the request.
This can help ensure that the payment session is secure and valid. |
| `eligibility_check_data` | string | YES |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/authentication/{{authentication_id}}/eligibility-check" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "client_secret": "example",
  "eligibility_check_data": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/eligibility-check"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "client_secret": "example",
  "eligibility_check_data": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/eligibility-check";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "client_secret": "example",
  "eligibility_check_data": "example"
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
