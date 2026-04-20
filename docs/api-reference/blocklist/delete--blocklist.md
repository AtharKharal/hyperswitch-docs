# 

**Endpoint:** `DELETE /blocklist`



**Operation ID:** `Unblock a Fingerprint`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/blocklist&method=DELETE" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X DELETE "https://sandbox.hyperswitch.io/blocklist" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/blocklist"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.delete(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/blocklist";
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
