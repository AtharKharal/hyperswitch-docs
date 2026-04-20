# Architecture Overview

## System Design

Hyperswitch is built as a payment orchestration layer that sits between your application and multiple payment processors.

## Core Components

### 1. API Gateway
The entry point for all payment operations:
- Accepts API requests
- Routes to appropriate connectors
- Returns standardized responses

### 2. Router Engine
Intelligent payment routing:
- Rules-based routing
- Load balancing
- Automatic failover

### 3. Connector Layer
Abstraction over payment processors:
- Stripe, PayPal, Adyen, etc.
- Normalized API
- Error handling

### 4. Analytics Engine
Real-time metrics:
- Success rates
- Processing times
- Cost optimization

## Data Flow

```
App → API Gateway → Router → Connector → Processor
                         ↓
                    Analytics
```

## Key Principles

### 1. Unified API
One integration for 50+ processors. The same request format works regardless of processor.

### 2. Smart Routing
Automatic optimization based on:
- Success rates per connector
- Authorization rates
- Processing fees
- Customer location

### 3. Failover
If one processor fails, automatically try alternatives.

### 4. Observability
Full visibility into payment flows:
- Webhook notifications
- Dashboard analytics
- API logs

## Security

- All data encrypted in transit (TLS 1.3)
- API keys never exposed
- Webhook signature verification
- PCI compliance via tokenization

## Playground

Test in the [Hyperswitch Playground](https://sandbox.hyperswitch.io/playground).

## Related

- [API Reference](../api-reference/index)
- [Payment Flows](payment-flows)