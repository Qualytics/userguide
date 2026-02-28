# Agentic API

The Qualytics Agentic API brings the same conversational AI capabilities available through [MCP](./mcp.md) directly into your applications and workflows. Using your own LLM API key, you can integrate natural language data quality management into custom tools, scripts, automation pipelines, and internal platforms.

## Overview

While the MCP integration is designed for interactive AI assistants like Claude Desktop, the Agentic API enables you to:

- Build custom applications that leverage natural language for data quality tasks
- Integrate AI-powered data quality into existing automation workflows
- Create internal tools and chatbots that interact with your data infrastructure
- Use your preferred LLM provider and manage your own API costs

The Agentic API provides the same capabilities as MCP—datastore exploration, data transformations, quality check creation, and anomaly investigation—accessible through standard REST endpoints.

## Authentication

All Agentic API endpoints require authentication using your Qualytics Personal API Token (PAT) or a designated service account token.

Include the token in the `Authorization` header:

```
Authorization: Bearer YOUR_QUALYTICS_API_TOKEN
```

For instructions on generating a token, see [Tokens](../../tokens/overview-of-tokens.md).

## LLM Configuration

Before using the Agentic API, you must configure your LLM provider credentials. This allows Qualytics to use your API key when making calls to the language model.

### Supported Providers

The Agentic API supports 22+ LLM providers. For the full list, see [Supported LLM Providers](./mcp-quickstart.md#supported-llm-providers) in the Agent Q Quickstart guide.

Common providers include:

- **OpenAI** — GPT-4o, GPT-4, o1, o3
- **Anthropic** — Claude Sonnet, Claude Opus, Claude Haiku
- **Google Gemini** — Gemini 2.0 Flash, Gemini 2.5 Pro
- **Amazon Bedrock** — Claude, Titan, and other models via AWS
- **Google Vertex AI** — Gemini models via GCP
- **Groq** — Llama, Mixtral (low-latency inference)
- **Mistral** — Mistral Large, Codestral
- **DeepSeek** — DeepSeek-V3, DeepSeek-R1
- **Ollama** — Self-hosted open-source models (requires custom base URL)

!!! tip
    Use the `GET /api/agent/supported-models` endpoint to dynamically retrieve the current list of supported providers and their available models.

### Managing LLM Configuration

LLM configuration is managed through the Qualytics UI, just like any other integration:

1. Navigate to **Settings** > **Integrations** in your Qualytics instance
2. Click **Connect** next to **LLM Configuration**
3. Select your **Provider**, **Model**, and enter your **API Key**
4. Optionally provide a **Base URL** if required by your provider
5. Click **Save** to complete the configuration

For detailed setup instructions with screenshots, see [Agent Q Quickstart — LLM Setup](./mcp-quickstart.md#before-you-start-llm-setup-required).

## Capabilities

### Chat with Agent

The chat endpoint provides a streaming conversational interface for exploring and managing your data quality infrastructure. This is the most flexible endpoint, allowing free-form natural language interactions with real-time streaming responses.

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/chat" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "What tables are in our sales_db datastore and what quality checks do we have on them?"}
    ]
  }'
```

The response is delivered as a Server-Sent Events (SSE) stream following the Vercel AI Data Stream Protocol. Each event contains either text content, tool execution progress, or error information.

**Multi-turn Conversations:**

Include previous messages to maintain conversation context. Pass the `session_id` returned in the `X-Chat-Session-Id` response header to continue an existing conversation:

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/chat?session_id=42" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "What tables are in our sales_db datastore?"},
      {"role": "assistant", "content": "I found 12 tables in the sales_db datastore..."},
      {"role": "user", "content": "Set up quality checks on the orders table"}
    ]
  }'
```

**Use Cases:**

- **Interactive Exploration**: Build chatbots or conversational interfaces that let users explore data assets naturally
- **Multi-step Workflows**: Handle complex requests that require understanding context and making multiple decisions
- **General Assistance**: Answer questions about data quality status, anomaly patterns, or check configurations

**Example Prompts:**

- *"Show me the schema for the customer_orders table in our PostgreSQL datastore"*
- *"What anomalies were detected in the last 24 hours?"*
- *"Which quality checks are failing most frequently across all our datastores?"*
- *"Help me understand why the order_total check keeps failing"*

### Execute Prompt

For simpler, single-turn interactions where you need a direct response without conversational context:

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/prompt" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "List all containers in the analytics_warehouse datastore"
  }'
```

**Use Cases:**

- **Scripted Queries**: Get specific information programmatically without maintaining conversation state
- **Quick Lookups**: Retrieve datastore metadata, check statuses, or anomaly counts
- **Report Generation**: Generate summaries or descriptions for automated reporting

### Transform Dataset

Create computed assets—tables, files, or cross-datastore joins—through natural language descriptions:

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/transform-dataset" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -H "Content-Type: application/json" \
  -G \
  --data-urlencode "asset_name=daily_revenue_by_category" \
  --data-urlencode "source_description=transactions table in sales_db" \
  --data-urlencode "transformation_criteria=Aggregate daily revenue by product category, including only completed orders from the last 90 days"
```

**Use Cases:**

- **Automated Data Preparation**: Integrate dataset creation into ETL pipelines or data workflows
- **Self-Service Analytics**: Let business users create derived datasets without writing SQL
- **Cross-System Integration**: Build unified views across databases and data lakes programmatically

**Example Descriptions:**

- *"Join the customers table from our Snowflake warehouse with the support_tickets table from PostgreSQL on customer_id, filtering to only active customers"*
- *"Create a computed file from our S3 landing zone that filters out test records and standardizes the date format"*
- *"Build a daily summary table that calculates average order value and order count by region"*

### Generate Quality Check

Create data quality checks by describing the business rule or validation requirement:

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/generate-quality-check" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -G \
  --data-urlencode "datastore_name=sales_db" \
  --data-urlencode "container_name=customers" \
  --data-urlencode "expectation=Ensure the email field is never null and matches a valid email format"
```

**Use Cases:**

- **Bulk Check Creation**: Programmatically establish quality checks across multiple datasets
- **Rule Migration**: Translate business rules from documentation into executable quality checks
- **Compliance Automation**: Set up regulatory validation checks based on policy descriptions
- **Data Contract Implementation**: Automatically create checks from data contract specifications

**Example Descriptions:**

- *"The order_total in the orders table should always be positive and less than 1,000,000"*
- *"ship_date must be after order_date for all records in the shipments table"*
- *"The status field should only contain 'pending', 'processing', 'shipped', or 'delivered'"*
- *"customer_id in transactions must exist in the customers table"*

### Investigate Anomaly

Get detailed, contextual explanations of data quality issues:

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/investigate-anomaly" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -G \
  --data-urlencode "anomaly_identifier=12345"
```

**Use Cases:**

- **Automated Alerting**: Enrich alert notifications with AI-generated context and impact analysis
- **Incident Reports**: Generate human-readable explanations for data quality incidents
- **Triage Automation**: Programmatically assess anomaly severity and suggest remediation steps
- **Stakeholder Updates**: Create plain-language summaries for business audiences

**What You Get:**

- Clear explanation of what data quality rule was violated
- Context about the affected dataset and fields
- Count and pattern of affected records
- Potential business impact
- Suggested investigation or remediation steps

### Analyze Trends

Analyze data quality trends over time for a specific data asset:

```bash
curl -X POST "https://your-qualytics.qualytics.io/api/agent/analyze-trends" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN" \
  -G \
  --data-urlencode "datastore_name=sales_db" \
  --data-urlencode "container_name=orders" \
  --data-urlencode "timeframe=month"
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `datastore_name` | Yes | The name of the datastore to analyze |
| `container_name` | No | Specific table or container (omit for datastore-level trends) |
| `field_name` | No | Specific field to focus on |
| `timeframe` | No | Time period to analyze: `week`, `month` (default), `quarter`, or `year` |

**Use Cases:**

- **Quality Reporting**: Generate trend reports for stakeholders and management
- **Improvement Tracking**: Measure the impact of quality initiatives over time
- **Regression Detection**: Identify when quality metrics started declining

### Get Suggestions

Retrieve AI-generated contextual suggestions for the chat interface:

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/agent/suggestions" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

Returns a list of suggested prompts based on the available tools and data sources. Useful for building guided user experiences.

### List Supported Models

Retrieve the list of supported LLM providers and their available models:

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/agent/supported-models" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

Returns provider metadata including display names, available models, whether the provider accepts arbitrary model names, and whether it requires a custom base URL. Use this endpoint to dynamically build provider selection UIs.

### Check LLM Configuration Status

Check whether an LLM provider is configured without retrieving the full configuration:

```bash
curl -X GET "https://your-qualytics.qualytics.io/api/agent/llm-config/status" \
  -H "Authorization: Bearer YOUR_QUALYTICS_TOKEN"
```

Returns `is_configured` (boolean), `model_name` (if configured), and `web_search_enabled` status. This lightweight endpoint is ideal for conditionally rendering UI elements.

## Integration Patterns

### Automated Quality Check Setup

When onboarding a new data source, automatically generate quality checks based on schema analysis:

```python
import requests

QUALYTICS_URL = "https://your-qualytics.qualytics.io"
TOKEN = "your_token"

# Discover the schema
response = requests.post(
    f"{QUALYTICS_URL}/api/agent/prompt",
    headers={"Authorization": f"Bearer {TOKEN}"},
    json={"prompt": "Analyze the customers table in sales_db and suggest appropriate quality checks based on the field types and names"}
)

suggestions = response.json()

# Create checks based on suggestions
for check_description in suggestions["recommended_checks"]:
    requests.post(
        f"{QUALYTICS_URL}/api/agent/generate-quality-check",
        headers={"Authorization": f"Bearer {TOKEN}"},
        json={"description": check_description}
    )
```

### Enriched Anomaly Alerts

Enhance your alerting pipeline with AI-generated context:

```python
def handle_anomaly_alert(anomaly_id):
    # Get AI-generated investigation
    response = requests.post(
        f"{QUALYTICS_URL}/api/agent/investigate-anomaly",
        headers={"Authorization": f"Bearer {TOKEN}"},
        json={"anomaly_id": anomaly_id}
    )

    investigation = response.json()

    # Send enriched alert to Slack/Teams/PagerDuty
    send_alert(
        title=f"Data Quality Issue: {investigation['summary']}",
        description=investigation['explanation'],
        impact=investigation['business_impact'],
        suggested_actions=investigation['recommendations']
    )
```

### Self-Service Data Preparation

Build an internal tool that lets analysts create datasets through natural language:

```python
@app.route("/create-dataset", methods=["POST"])
def create_dataset():
    user_request = request.json["description"]

    response = requests.post(
        f"{QUALYTICS_URL}/api/agent/transform-dataset",
        headers={"Authorization": f"Bearer {TOKEN}"},
        json={"description": user_request}
    )

    result = response.json()
    return {
        "status": "created",
        "dataset_name": result["asset_name"],
        "message": f"Your dataset is now available for profiling and quality scanning"
    }
```

## Best Practices

### Prompt Design

For best results when using the Agentic API:

- **Be specific about datastores and tables**: Include the datastore name and container/table name when referencing data assets
- **Describe business intent**: Explain what you're trying to accomplish, not just the technical operation
- **Include constraints**: Mention filtering criteria, date ranges, or other limitations upfront

### Cost Management

Since you're using your own LLM API key:

- Use the `prompt` endpoint for simple, single-turn queries instead of `chat` when conversation context isn't needed
- Cache responses for frequently-requested information
- Consider rate limiting in your applications to control API costs

### Error Handling

The Agentic API returns structured responses that include:

- Success/failure status
- Generated SQL or configuration (when applicable)
- Validation errors or issues with the request
- Suggestions for how to refine ambiguous requests

Always check response status and handle cases where the AI may need clarification or additional context.
