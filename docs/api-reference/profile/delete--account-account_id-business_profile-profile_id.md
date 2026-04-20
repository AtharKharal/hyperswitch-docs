# Profile - Delete

**Endpoint:** `DELETE /account/{account_id}/business_profile/{profile_id}`

Delete the *profile*

**Operation ID:** `Delete the Profile`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/business_profile/{profile_id}&method=DELETE" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X DELETE "https://sandbox.hyperswitch.io/account/{{account_id}}/business_profile/{{profile_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.delete(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}";
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
