def candies(number_candies: list[int]) -> int:
    if any(not isinstance(child_candies, int) for child_candies in number_candies):
        raise ValueError("❗️ Input should be a list of integers")
    if len(number_candies) <= 1:
        return -1
    required_candies = max(number_candies)
    result = 0
    for child_number in number_candies:
        result += required_candies - child_number
    return result
