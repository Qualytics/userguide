# Team Membership Strategy

Service accounts can be added to teams to control and limit their access to specific datastores
and containers across the platform.

## How Team Membership Works

- **Public team:** Every service account is automatically part of the Public team.
- **Additional teams:** You can assign a service account to one or more teams based on the
  access it needs.
- **Access control:** A service account can access only the datastores and containers that
  belong to the teams it is a member of.

## Team Assignment Examples

**Example 1: Data Catalog Integration**

```json
{
  "name": "Alation Data Catalog Sync",
  "role": "Manager",
  "teams": [
    "Data Engineering",
    "Analytics",
    "Finance Data"
  ]
}
```

This service account will have access to:

- Public team resources (automatic)
- Data Engineering team's datastores
- Analytics team's datastores
- Finance Data team's datastores

**Example 2: Data Pipeline Automation**

```json
{
  "name": "Pipeline Automation",
  "role": "Editor",
  "teams": [
    "Data Engineering"
  ]
}
```

This service account can:

- Trigger profiling and scanning operations on Data Engineering team's datastores
- Create and modify containers in Data Engineering team's scope
