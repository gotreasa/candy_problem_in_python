from modules import candy_problem


def describe_dummy_kata():
    def should_print_title(capsys):
        """🧪 expect the dummy kata prints the title"""
        candy_problem.print_the_title()
        out, _err = capsys.readouterr()
        assert "😊 Welcome to Dummy Kata" in out
