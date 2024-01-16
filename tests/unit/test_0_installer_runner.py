import pytest
from modules import candy_problem


def describe_candies():
    def should_error_when_not_list_of_numbers():
        """🧪 should error when a list of numbers is not received"""
        with pytest.raises(ValueError, match="❗️ Input should be a list of integers"):
            candy_problem.candies("blah")

    def should_give_out_9_candies_for_5_8_6_4():
        """🧪 should give out 9 when the list of children candies are (5, 8, 6, 4)"""
        assert candy_problem.candies([5, 8, 6, 4]) == 9

    def should_give_out_11_candies_for_1_2_4_6():
        """🧪 should give out 11 when the list of children candies are (1, 2, 4, 6)"""
        assert candy_problem.candies([1, 2, 4, 6]) == 11

    def should_give_out_5_candies_for_1_6():
        """🧪 should give out 5 when the list of children candies are (1, 6)"""
        assert candy_problem.candies([1, 6]) == 5
