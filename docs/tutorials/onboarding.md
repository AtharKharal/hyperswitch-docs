# Onboarding Path

Follow this structured learning path to integrate Hyperswitch into your application.

## Learning Path

```mermaid
%%{init: {'theme': 'dark'}}%%
flowchart LR
    A[Quick Start] --> B[Connectors]
    B --> C[Customers]
    C --> D[Refunds]
    D --> E[Routing]
    E --> F[Webhooks]
    
    style A fill:#6366f1,color:#fff
    style B fill:#8b5cf6,color:#fff
    style C fill:#a855f7,color:#fff
    style D fill:#d946ef,color:#fff
    style E fill:#ec4899,color:#fff
    style F fill:#f43f5e,color:#fff
```

## Stage 1: Foundation

| Step | Tutorial | Description |
|------|----------|-------------|
| 1 | [Quick Start](quickstart) | Create your first payment |
| 2 | [Connectors](connectors) | Configure payment processors |

## Stage 2: Core Entities

| Step | Tutorial | Description |
|------|----------|-------------|
| 3 | [Customers](customers) | Manage customer profiles |
| 4 | [Process Refunds](process-refunds) | Handle refund operations |

## Stage 3: Advanced

| Step | Tutorial | Description |
|------|----------|-------------|
| 5 | [Smart Routing](routing) | Optimize payment routing |
| 6 | [Webhooks](webhooks) | Real-time event handling |

## Success Criteria

Complete each stage before proceeding:

- **Stage 1**: Payment created in sandbox environment
- **Stage 2**: Customer created and payment refunded
- **Stage 3**: Routing configured and webhook received

## Alternative Paths

After completing Stage 1, you may diverge based on your needs:

- **Security-focused**: Continue to [3D Secure](three-d-secure)
- **Operational**: Continue to [Process Refunds](process-refunds)
- **Scalability**: Continue to [Smart Routing](routing)
