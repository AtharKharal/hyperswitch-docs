# Merchant Account - Delete

**Endpoint:** `DELETE /accounts/{account_id}`

Delete a *merchant* account

**Operation ID:** `Delete a Merchant Account`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/accounts/{account_id}&method=DELETE" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X DELETE "https://sandbox.hyperswitch.io/accounts/{{account_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/accounts/{account_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.delete(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/accounts/{account_id}";
const options = {
  method: "DELETE",
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
