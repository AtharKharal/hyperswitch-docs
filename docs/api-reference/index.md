# API Reference

Welcome to the Hyperswitch API Reference. Our API is organized around REST, with predictable resource-oriented URLs, and uses standard HTTP response codes, authentication, and verbs.

---

## 🛠️ Core Resources

### [Payments](payments/index)
The core of the Hyperswitch API. Create, retrieve, confirm, and capture payments. Supports 17 endpoints.
[Try Payments Playground →](https://sandbox.hyperswitch.io/playground?category=payments){ .md-button .md-button--small }

### [Refunds](refunds/index)
Manage the lifecycle of refunds. Process full or partial refunds across different processors.
[Try Refunds Playground →](https://sandbox.hyperswitch.io/playground?category=refunds){ .md-button .md-button--small }

### [Customers](customers/index)
Store customer information to simplify repeat payments.
[Try Customers Playground →](https://sandbox.hyperswitch.io/playground?category=customers){ .md-button .md-button--small }

### [Payment Methods](payment-methods/index)
Manage saved payment methods for customers. Supports various payment types including cards, bank redirects, and digital wallets.

---

## ⚙️ Configuration & Routing

### [Merchant Account](merchant-account/index)
Manage your merchant account settings, business profiles, and key-value status.

### [Routing](routing/index)
Configure intelligent routing algorithms to optimize for success rates and processing fees across multiple connectors.

### [Payouts](payouts/index)
Manage payout operations to vendors or customers. Supports creation, fulfillment, and status tracking.

---

## 🔐 Authentication & Security

### [API Key](api-key/index)
Manage API keys for programmatic access to the Hyperswitch platform.

### [Authentication](authentication/index)
Handle 3D Secure and other external authentication methods to ensure transaction security.

---

## 📊 More Resources

- [Relay](relay/index) — Simplified cross-border payment relaying.
- [Organization](organization/index) — Manage organizational structures and permissions.
- [Disputes](disputes/index) — Track and respond to payment disputes.
- [Mandates](mandates/index) — Manage recurring payment mandates.
- [GSM](gsm/index) — Gateway Status Mapping for unified error handling.
- [Event](event/index) — Track system events and delivery attempts.
- [Poll](poll/index) — Check the status of asynchronous operations.
- [Platform](platform/index) — Platform-level user and account management.
- [Subscriptions](subscriptions/index) — Manage recurring billing and subscription lifecycles.

---

## Playground

!!! info "Interactive Testing"
    You can test any of these endpoints live in our [Interactive Playground](https://sandbox.hyperswitch.io/playground) without writing any code.

Test any of these endpoints live in our [Interactive Playground](https://sandbox.hyperswitch.io/playground).
