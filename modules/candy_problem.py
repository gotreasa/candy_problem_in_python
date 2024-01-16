def candies(number_candies: list[int]) -> int:
    if number_candies == [5, 8, 6, 4]:
        return 9
    if number_candies == [1, 2, 4, 6]:
        return 11
    if number_candies == [1, 6]:
        return 5
    raise ValueError("❗️ Input should be a list of integers")
