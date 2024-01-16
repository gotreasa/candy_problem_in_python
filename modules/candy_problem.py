def is_one_or_no_child(number_of_children: list[int]) -> bool:
    if len(number_of_children) <= 1:
        return True
    return False


def candies(number_candies: list[int]) -> int:
    if any(not isinstance(child_candies, int) for child_candies in number_candies):
        raise ValueError("❗️ Input should be a list of integers")
    if is_one_or_no_child(number_candies):
        return -1
    required_candies = max(number_candies)
    result = 0
    for child_number in number_candies:
        result += required_candies - child_number
    return result
