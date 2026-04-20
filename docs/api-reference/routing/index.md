# Routing

Reference documentation for routing API endpoints.

## Endpoints

### [POST /routing](post--routing)

Routing - Create

### [GET /routing](get--routing)

Routing - List

### [POST /routing/{routing_algorithm_id}/activate](post--routing-routing_algorithm_id-activate)

Routing - Activate config

### [GET /routing/{routing_algorithm_id}](get--routing-routing_algorithm_id)

Routing - Retrieve

### [POST /routing/deactivate](post--routing-deactivate)

Routing - Deactivate

### [POST /routing/default](post--routing-default)

Routing - Update Default Config

### [GET /routing/default](get--routing-default)

Routing - Retrieve Default Config

### [GET /routing/active](get--routing-active)

Routing - Retrieve Config

### [GET /routing/default/profile](get--routing-default-profile)

Routing - Retrieve Default For Profile

### [POST /routing/default/profile/{profile_id}](post--routing-default-profile-profile_id)

Routing - Update Default For Profile

### [PATCH /account/{account_id}/business_profile/{profile_id}/dynamic_routing/success_based/config/{algorithm_id}](patch--account-account_id-business_profile-profile_id-dynamic_routing-success_based-config-algorithm_id)

Routing - Update success based dynamic routing config for profile

### [POST /account/{account_id}/business_profile/{profile_id}/dynamic_routing/success_based/toggle](post--account-account_id-business_profile-profile_id-dynamic_routing-success_based-toggle)

Routing - Toggle success based dynamic routing for profile

### [POST /account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/toggle](post--account-account_id-business_profile-profile_id-dynamic_routing-elimination-toggle)

Routing - Toggle elimination routing for profile

### [POST /account/{account_id}/business_profile/{profile_id}/dynamic_routing/success_based/create](post--account-account_id-business_profile-profile_id-dynamic_routing-success_based-create)

Routing - Auth Rate Based

### [POST /account/{account_id}/business_profile/{profile_id}/dynamic_routing/elimination/create](post--account-account_id-business_profile-profile_id-dynamic_routing-elimination-create)

Routing - Elimination

### [POST /account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/toggle](post--account-account_id-business_profile-profile_id-dynamic_routing-contracts-toggle)

Routing - Toggle Contract routing for profile

### [PATCH /account/{account_id}/business_profile/{profile_id}/dynamic_routing/contracts/config/{algorithm_id}](patch--account-account_id-business_profile-profile_id-dynamic_routing-contracts-config-algorithm_id)

Routing - Update contract based dynamic routing config for profile

### [POST /routing/evaluate](post--routing-evaluate)

Routing - Evaluate

### [POST /routing/feedback](post--routing-feedback)

Routing - Feedback

### [POST /routing/rule/evaluate](post--routing-rule-evaluate)

Routing - Rule Evaluate


## Playground

Test these endpoints in the [Hyperswitch Playground](https://sandbox.hyperswitch.io/playground?category=routing).
