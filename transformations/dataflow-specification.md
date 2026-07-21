# Especificación del Mapping Data Flow

## Source: InputCsv

- Formato: Delimited Text
- Header: true
- Delimitador: coma
- Columnas principales:
  - `movieId`
  - `title`
  - `genres`

## Derived Column: YearExtraction

Nueva columna:

```text
year = toInteger(trim(right(title, 6), '()'))
```

## Sink 1: MoviesClean

Columnas:

- `movieId`
- `title`
- `genres`
- `year`

## Aggregate: MoviesCount

- Group by: `year`
- Aggregate:
  - `movie_count = count()`

## Sink 2: MoviesByYear

Columnas:

- `year`
- `movie_count`
