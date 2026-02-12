def analyze_numbers(numbers: list[int]) -> dict:
    if not numbers:
        raise ValueError("List cannot be empty")

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers)
    }
