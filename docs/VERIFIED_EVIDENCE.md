# Verified evidence and claim boundary

The Azure Data Factory resources were inspected in read-only mode on July 22, 2026. No Azure resource was edited, published or executed during this review.

## Evidence inventory

| Evidence | What it verifies | What it does not verify |
|---|---|---|
| `01-movies-mapping-pipeline.png` | An ADF pipeline contains a Data Flow activity | Successful execution, runtime duration or production schedule |
| `02-mapping-data-flow.png` | The visual graph contains `Movies`, `YearExtraction`, `MoviesCount`, `MoviesClean` and `MoviesByYear` | Row-level output values or scale performance |
| `transformations/dataflow-script.txt` | Published source projection, derive expressions, aggregation, sink file names and partition settings | Linked-service authentication or storage provisioning |
| `transformations/dataflow-specification.md` | Pipeline activity type and reviewed Data Flow configuration | Production SLA or recommended compute sizing |
| `tests/test_sample_contract.py` | The public fixture produces the documented sample counts | Azure runtime behavior or cloud integration |

## Reviewed resource relationships

```text
MoviesMappingFlow pipeline
`-- Data flow1 activity (ExecuteDataFlow)
    `-- dataflow1
        |-- InputCsv -> Movies
        |-- YearExtraction -> OutputCsv / movies-clean.csv
        `-- MoviesCount -> OutputCsv / MoviesByYear.csv
```

## Public-data policy

- The sample movie records are illustrative and contain no personal information.
- Connection strings, credentials, linked-service details and storage paths are excluded.
- Subscription and tenant identifiers visible during verification are not included in this repository.
- Screenshots are used only to demonstrate the ADF design surface.

## Claims intentionally not made

- No production-scale or performance benchmark.
- No monitored successful-run claim from the included screenshots.
- No claim that the current expression handles malformed or missing year suffixes.
- No claim that one output partition is appropriate for large workloads.
