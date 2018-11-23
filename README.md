# Actuator Commit Healthcheck

This is a utility docker image that waits for your spring boot app to be **UP** and running on a specific **commit**.

Run with

```bash
docker run -e URL=https://service COMMIT=abc123 forgerock/actuator-commit-healthcheck
```

This works by calling the `actuator/health` and `actuator/info` endpoints.

| Env      | Description                                  | Default |
|----------|----------------------------------------------|---------|
| URL      | Scheme and hostname e.g. https://app         | Not set |
| COMMIT   | The git commit you expect                    | Not set |
| TIMEOUT  | The amount of time to wait per retry         | 1       |
| RETRIES  | Number of times to retry                     | 60      |
| USERNAME | User if app is protected with basic auth     | Not set |
| PASSWORD | Password if app is protected with basic auth | Not set |