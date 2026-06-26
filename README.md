# trialport Backend Engineering Assessment

This is trialport's backend engineering assessment. The goal is to build a reliable data import workflow for clinical trial studies using Django, Django Admin, Celery, Postgres, Redis, and Docker.

You are expected to use AI tools to help with the coding portion of this assessment. We care about clean, maintainable code, but our larger signal is how you engineer the solution: how you handle unreliable dependencies, make tradeoffs, measure progress, and explain your decisions.

There is no time limit. Spend the amount of time you think is appropriate and submit the GitHub link to your completed fork when you are done.

## Scenario

You will receive a CSV file by email. The CSV contains one column:

```csv
NCT Number
NCT00000001
```

Each value is an NCT ID that should be fetched from the supplied CT.gov sample API:

```text
GET {CTGOV_API_BASE_URL}/api/v2/studies/{nct_id}
```

The default local setting points at the assessment API host:

```text
CTGOV_API_BASE_URL=http://sample-api.trialport.com
```

The sample API intentionally behaves like an unreliable external service. Some requests may fail, some may hang, and you may run into other issues while querying it. Treat it as a third-party API you do not control.

## Your Task

Build a fault-tolerant study import workflow.

At minimum, your solution should:

- Accept the provided CSV through the Django app.
- Create an upload/import task for the CSV.
- Run the data sync outside the request cycle.
- Fetch study data from the CT.gov sample API.
- Upsert existing `Study` records by NCT ID so duplicate runs update old records.
- Store useful queryable study fields, including NCT ID, title, status, conditions, study type, summary, and sponsor primary key.
- Provide a visible indication of upload/import progress.
- Provide useful visibility into what happened during an import, especially when rows fail or records are updated.
- Handle partial failures without causing the entire import to collapse.
- Include clear instructions for how to run and test your solution locally.

Celery is already included and is the recommended path. You may use a different durable background execution system, such as Temporal, if it runs locally in Docker and you document the tradeoffs clearly.

## Starter Code

The project includes:

- Django, Django Admin, Django REST Framework, Postgres, Redis, Celery, Celery Beat, Flower, and Docker Compose.
- Basic `Study` and `UploadTask` models.
- Django Admin registration for the study/import models.
- A placeholder Celery task for the importer.
- A management command to create a local admin user.
- Celery result storage configured through Postgres.

The importer itself is intentionally incomplete. You should decide how to parse the CSV, enqueue work, retry failures, store progress, track import outcomes, and expose errors.

The provided models are intentionally minimal. You are expected to change the schema as your design requires. Add tracking, logging, storage, progress fields, row-level outcomes, raw payload storage, or other persistence if those choices help you build a reliable and understandable import workflow.

## Local Setup

Prerequisites:

- Docker Engine
- Docker Compose
- `just`

Build and start the stack:

```bash
just build
just up
```

Run migrations:

```bash
just manage migrate
```

Create the local admin user:

```bash
just manage seed_test_user
```

Default credentials:

```text
Email: admin@example.com
Password: password123
```

Open Django Admin:

```text
http://localhost:8000/admin/
```

View logs:

```bash
just logs
just logs django
just logs celeryworker
```

Run tests:

```bash
just pytest
```

Stop the stack:

```bash
just down
```

Reset local Docker volumes:

```bash
just prune
```

This is useful if your local database gets into a bad state and you want to rebuild from a clean set of Docker volumes.

## Configuration

The CT.gov sample API base URL is configured with:

```text
CTGOV_API_BASE_URL=http://sample-api.trialport.com
```

You may override this in `.envs/.local/.django`.

## Submission

Fork this repository, complete the assessment in your fork, and send us the GitHub URL when you are done.

Please include enough documentation for us to run your solution locally. If you make assumptions or intentionally leave tradeoffs unresolved, document them.

## Optional Security Exploration

The supplied fake CT.gov API host is in scope for optional exploration, including standard testing tools. Do not test, scan, or attack any other trialport, pRxEngage, AWS, employee, customer, or production systems.

If you find anything interesting on the fake API host, include a short note about what you found, how you found it, and how you would report or remediate it in a real environment.

## What We Evaluate

### Basic

- Project runs locally in Docker.
- Admin user can be created.
- CSV upload task can be created.
- Import runs outside the request cycle.
- Studies are fetched and upserted.

### Strong

- Handles 404s, 500s, timeouts, and other unexpected API behavior without failing the whole job.
- Implements retries with sane backoff and timeouts.
- Tracks progress and status clearly.
- Produces useful logs or errors for failed rows.
- Uses concurrency safely without duplicate or race-prone writes.

### Excellent

- Clean architecture with testable importer services and tasks.
- Idempotent repeated runs.
- Good database constraints and indexes.
- Useful admin or query experience.
- Meaningful tests for success, partial failure, retries, and upserts.
- Performance scales to the full CSV.

### Bonus

- Thoughtful handling of unclear or impossible requirements.
- Candidate proactively documents assumptions and tradeoffs.
- Useful observability around retries, failures, and throughput.
- Clear performance reasoning for large imports.
