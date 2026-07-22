import csv
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "movies_sample.csv"
EXPECTED_PATH = ROOT / "data" / "expected_movies_by_year.csv"


def transform_title(title: str) -> tuple[str, int]:
    """Mirror the published ADF expressions for the public fixture."""
    suffix = title[-6:]
    year = int(suffix.strip("()"))
    cleaned_title = title[:-6]
    return cleaned_title, year


class TestMovieSampleContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with INPUT_PATH.open(encoding="utf-8", newline="") as source_file:
            cls.rows = list(csv.DictReader(source_file))

        with EXPECTED_PATH.open(encoding="utf-8", newline="") as expected_file:
            cls.expected_counts = {
                int(row["titleExtraction"]): int(row["MoviesCount"])
                for row in csv.DictReader(expected_file)
            }

    def test_input_schema_and_row_count(self) -> None:
        self.assertEqual(set(self.rows[0]), {"movieId", "title", "genres"})
        self.assertEqual(len(self.rows), 4)

    def test_all_titles_follow_the_published_year_contract(self) -> None:
        for row in self.rows:
            cleaned_title, year = transform_title(row["title"])
            self.assertTrue(cleaned_title.strip())
            self.assertGreaterEqual(year, 1900)
            self.assertLessEqual(year, 2100)

    def test_expected_year_aggregation(self) -> None:
        actual_counts = Counter(
            transform_title(row["title"])[1] for row in self.rows
        )
        self.assertEqual(dict(sorted(actual_counts.items())), self.expected_counts)


if __name__ == "__main__":
    unittest.main()
