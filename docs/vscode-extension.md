# Developer Tools - IDE Integration

## Overview

Hyperswitch provides real-time semantic intelligence directly in your IDE through VS Code extension, LSP (Language Server Protocol), and MCP (Model Context Protocol).

## Available Tools

### VS Code Extension
Real-time API documentation and code completions in your editor.

### LSP (Language Server Protocol)
Hover tooltips for HyperSwitch API parameters, response types, and error codes.

### MCP (Model Context Protocol)
Query HyperSwitch documentation as executable tools for AI agents.

[Learn More →](developer-tools)

## Features

### 1. Real-time Documentation
Hover over any Hyperswitch API call to see:
- Endpoint description
- Parameter documentation
- Response schemas
- Examples

### 2. Code Autocompletion
Intelligent completions for:
- API endpoints
- Request parameters
- Response handling

### 3. API Explorer
Side panel with:
- Interactive API explorer
- Request builder
- Response viewer

### 4. Semantic Search
Search across:
- All endpoints
- Documentation
- Code examples

## Installation

```bash
code --install-extension hyperswitch.hyperswitch-vscode
```

Or search for "Hyperswitch" in the VS Code Extensions panel.

## Usage

### View Endpoint Info
```javascript
// Hover over any Hyperswitch API call
import { payments } from '@hyperswitch/sdk';

const payment = await payments.create({
  amount: 5000,
  currency: 'USD'
}); // Hover shows: Creates a payment intent...

// Hover shows full documentation:
// Creates a new payment intent
// Parameters: amount (required), currency (required)...
```

### Use API Explorer

1. Open command palette (`Ctrl+Shift+P`)
2. Type "Hyperswitch: Open Explorer"
3. Browse endpoints
4. Click to insert code

### Interactive Testing

```bash
# In the extension's API Explorer:
# 1. Select endpoint
# 2. Fill parameters  
# 3. Click "Send Request"
# 4. View response
```

## Configuration

Add to your `.vscode/settings.json`:

```json
{
  "hyperswitch.apiKey": "sk_live_...",
  "hyperswitch.sandbox": true,
  "hyperswitch.showInlineDocs": true
}
```

## Playground Integration

Each endpoint includes a link to the Hyperswitch Playground for live testing.

## Related

- [API Reference](api-reference/index)
- [Hyperswitch Dashboard](https://app.hyperswitch.io)