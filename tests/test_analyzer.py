from build_analyzer.analyzer import analyze_numbers
import pytest


def test_analyze_numbers_basic():
    result = analyze_numbers([1, 2, 3])

    assert result["count"] == 3
    assert result["sum"] == 6
    assert result["average"] == 2


def test_analyze_numbers_empty():
    with pytest.raises(ValueError):
        analyze_numbers([])
