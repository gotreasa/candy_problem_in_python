import pytest
from modules import candy_problem


def describe_candies():
    def should_error_when_not_list_of_numbers():
        """🧪 should error when a list of numbers is not received"""
        with pytest.raises(ValueError, match="❗️ Input should be a list of integers"):
            candy_problem.candies("blah")
