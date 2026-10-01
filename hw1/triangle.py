def classify_triangle(a: int, b: int, c: int) -> str:
    """依三邊長回傳三角形種類：invalid / equilateral / isosceles / scalene。"""
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "invalid"
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"
