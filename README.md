# log-parser

Template for a robust, production-ready Python CLI utility that reads a raw
access log file, extracts key metrics (IP addresses, HTTP status codes, response
sizes), and outputs a structured Markdown report summary.

> This is intentionally **structure only** (no implementation).

## Suggested project layout

```text
log-parser/
├── pyproject.toml
├── README.md
├── src/
│   └── log_parser/
│       ├── __init__.py
│       ├── cli.py
│       ├── parser.py
│       ├── metrics.py
│       ├── report.py
│       ├── models.py
│       └── errors.py
├── tests/
│   ├── test_cli.py
│   ├── test_parser.py
│   ├── test_metrics.py
│   └── test_report.py
└── examples/
    ├── sample_access.log
    └── expected_report.md
```

## Module responsibilities (template)

- `cli.py`: argument parsing, input/output paths, flags, exit codes.
- `parser.py`: parse raw access log lines into structured records.
- `metrics.py`: aggregate IP counts, status code distribution, response-size stats.
- `report.py`: render Markdown summary from computed metrics.
- `models.py`: dataclasses / typed models for records and report payload.
- `errors.py`: domain-specific exceptions and error mapping for CLI output.

## CLI surface (template)

```bash
log-parser summarize \
  --input /path/to/access.log \
  --output /path/to/report.md \
  --top-ips 10
```

### Recommended flags

- `--input`: required path to raw log file.
- `--output`: optional path for Markdown output (defaults to stdout).
- `--top-ips`: max number of IPs in the “Top IPs” section.
- `--strict`: fail on malformed lines (otherwise skip + count errors).
- `--timezone`: normalize timestamps for report consistency.

## Markdown report shape (template)

```markdown
# Access Log Summary

## Metadata
- Source file: ...
- Total lines: ...
- Parsed lines: ...
- Skipped lines: ...
- Generated at: ...

## Top IP Addresses
| IP Address | Requests |
|---|---:|
| ... | ... |

## HTTP Status Codes
| Status | Count | Percent |
|---:|---:|---:|
| 200 | ... | ... |

## Response Size Metrics
- Total bytes: ...
- Average bytes: ...
- Median bytes: ...
- P95 bytes: ...

## Notes
- Parsing assumptions: ...
- Validation warnings: ...
```

## Non-functional requirements for the template

- Type hints across public APIs.
- Deterministic output ordering for stable tests.
- Clear error messages and non-zero exit codes on failures.
- Unit tests per module and CLI integration tests.
- Logging hooks for troubleshooting (without leaking sensitive data).
