# Published ADF specification

This document records the Azure Data Factory configuration reviewed in read-only mode on July 22, 2026. It intentionally excludes linked-service configuration, storage paths, credentials and subscription identifiers.

## Pipeline: `MoviesMappingFlow`

- Activity name: `Data flow1`
- Activity type: `ExecuteDataFlow`
- Data Flow reference: `dataflow1`
- Compute type: `General`
- Core count: `8`
- Trace level: `Fine`
- Timeout: `12 hours`
- Retry count: `0`

These are lab configuration values, not a performance or production-sizing recommendation.

## Mapping Data Flow: `dataflow1`

### Source: `Movies`

- Dataset reference: `InputCsv`
- Projected fields:
  - `movieId` as string
  - `title` as string
  - `genres` as string
- Schema drift: allowed
- Schema validation: disabled

### Derived Column: `YearExtraction`

```text
titleExtraction = toInteger(trim(right(title, 6), '()'))
title = toString(left(title, length(title)-6))
```

The transformation derives an integer year and replaces `title` with the title minus its six-character year suffix.

### Aggregate: `MoviesCount`

```text
groupBy(titleExtraction)
MoviesCount = count()
```

### Sink: `MoviesClean`

- Input stream: `YearExtraction`
- Dataset reference: `OutputCsv`
- File name: `movies-clean.csv`
- Partitioning: one hash partition
- Schema drift: allowed
- Schema validation: disabled

### Sink: `MoviesByYear`

- Input stream: `MoviesCount`
- Dataset reference: `OutputCsv`
- File name: `MoviesByYear.csv`
- Partitioning: one hash partition
- Schema drift: allowed
- Schema validation: disabled

## Production-hardening considerations

1. Validate titles before attempting integer conversion.
2. Route malformed records to a rejected-record sink.
3. Apply `trim()` after removing the year suffix.
4. Enforce an explicit schema where the source contract requires it.
5. Add row-count and null controls to both outputs.
6. Select a partition strategy based on output volume instead of forcing one file.

The complete published transformation script is available in [`dataflow-script.txt`](dataflow-script.txt).
