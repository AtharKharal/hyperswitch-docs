# Profile - Update

**Endpoint:** `POST /account/{account_id}/business_profile/{profile_id}`

Update the *profile*

**Operation ID:** `Update a Profile`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/business_profile/{profile_id}&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `profile_name` | string | NO | The name of profile |
| `return_url` | string | NO | The URL to redirect after the completion of the operation |
| `enable_payment_response_hash` | boolean | NO | A boolean value to indicate if payment response hash needs to be enabled |
| `payment_response_hash_key` | string | NO | Refers to the hash key used for calculating the signature for webhooks and redirect response. If the value is not provided, a value is automatically generated. |
| `redirect_to_merchant_with_http_post` | boolean | NO | A boolean value to indicate if redirect to merchant with http post needs to be enabled |
| `webhook_details` | string | NO |  |
| `metadata` | object | NO | Metadata is useful for storing additional, unstructured information on an object. |
| `routing_algorithm` | object | NO | The routing algorithm to be used for routing payments to desired connectors |
| `intent_fulfillment_time` | integer | NO | Will be used to determine the time till which your payment will be active once the payment session starts |
| `frm_routing_algorithm` | object | NO | The frm routing algorithm to be used for routing payments to desired FRM's |
| `payout_routing_algorithm` | string | NO |  |
| `applepay_verified_domains` | array | NO | Verified Apple Pay domains for a particular profile |
| `session_expiry` | integer | NO | Client Secret Default expiry for all payments created under this profile |
| `payment_link_config` | string | NO |  |
| `authentication_connector_details` | string | NO |  |
| `use_billing_as_payment_method_billing` | boolean | NO | Whether to use the billing details passed when creating the intent as payment method billing |
| `collect_shipping_details_from_wallet_connector` | boolean | NO | A boolean value to indicate if customer shipping details needs to be collected from wallet
connector only if it is required field for connector (Eg. Apple Pay, Google Pay etc) |
| `collect_billing_details_from_wallet_connector` | boolean | NO | A boolean value to indicate if customer billing details needs to be collected from wallet
connector only if it is required field for connector (Eg. Apple Pay, Google Pay etc) |
| `always_collect_shipping_details_from_wallet_connector` | boolean | NO | A boolean value to indicate if customer shipping details needs to be collected from wallet
connector irrespective of connector required fields (Eg. Apple pay, Google pay etc) |
| `always_collect_billing_details_from_wallet_connector` | boolean | NO | A boolean value to indicate if customer billing details needs to be collected from wallet
connector irrespective of connector required fields (Eg. Apple pay, Google pay etc) |
| `is_connector_agnostic_mit_enabled` | boolean | NO | Indicates if the MIT (merchant initiated transaction) payments can be made connector
agnostic, i.e., MITs may be processed through different connector than CIT (customer
initiated transaction) based on the routing rules.
If set to `false`, MIT will go through the same connector as the CIT. |
| `payout_link_config` | string | NO |  |
| `outgoing_webhook_custom_http_headers` | object | NO | These key-value pairs are sent as additional custom headers in the outgoing webhook request. It is recommended not to use more than four key-value pairs. |
| `tax_connector_id` | string | NO | Merchant Connector id to be stored for tax_calculator connector |
| `is_tax_connector_enabled` | boolean | NO | Indicates if tax_calculator connector is enabled or not.
If set to `true` tax_connector_id will be checked. |
| `is_network_tokenization_enabled` | boolean | NO | Indicates if network tokenization is enabled or not. |
| `is_auto_retries_enabled` | boolean | NO | Indicates if is_auto_retries_enabled is enabled or not. |
| `max_auto_retries_enabled` | integer | NO | Maximum number of auto retries allowed for a payment |
| `always_request_extended_authorization` | boolean | NO | Bool indicating if extended authentication must be requested for all payments |
| `is_click_to_pay_enabled` | boolean | NO | Indicates if click to pay is enabled or not. |
| `authentication_product_ids` | object | NO | Product authentication ids |
| `card_testing_guard_config` | string | NO |  |
| `is_clear_pan_retries_enabled` | boolean | NO | Indicates if clear pan retries is enabled or not. |
| `force_3ds_challenge` | boolean | NO | Indicates if 3ds challenge is forced |
| `is_debit_routing_enabled` | boolean | NO | Indicates if debit routing is enabled or not |
| `merchant_business_country` | string | NO |  |
| `is_iframe_redirection_enabled` | boolean | NO | Indicates if the redirection has to open in the iframe |
| `is_pre_network_tokenization_enabled` | boolean | NO | Indicates if pre network tokenization is enabled or not |
| `merchant_category_code` | string | NO |  |
| `merchant_country_code` | string | NO |  |
| `dispute_polling_interval` | integer | NO | Time interval (in hours) for polling the connector to check  for new disputes |
| `is_manual_retry_enabled` | boolean | NO | Indicates if manual retry for payment is enabled or not |
| `always_enable_overcapture` | boolean | NO | Bool indicating if overcapture  must be requested for all payments |
| `is_external_vault_enabled` | string | NO |  |
| `external_vault_connector_details` | string | NO |  |
| `billing_processor_id` | string | NO | Merchant Connector id to be stored for billing_processor connector |
| `is_l2_l3_enabled` | boolean | NO | Flag to enable Level 2 and Level 3 processing data for card transactions |
| `network_tokenization_credentials` | string | NO |  |
| `payment_method_blocking` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/account/{{account_id}}/business_profile/{{profile_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "profile_name": "example",
  "return_url": "example",
  "enable_payment_response_hash": false,
  "payment_response_hash_key": "example",
  "redirect_to_merchant_with_http_post": false
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "profile_name": "example",
  "return_url": "example",
  "enable_payment_response_hash": false,
  "payment_response_hash_key": "example",
  "redirect_to_merchant_with_http_post": false
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/business_profile/{profile_id}";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "profile_name": "example",
  "return_url": "example",
  "enable_payment_response_hash": false,
  "payment_response_hash_key": "example",
  "redirect_to_merchant_with_http_post": false
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
