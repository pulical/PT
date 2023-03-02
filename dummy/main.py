# test_example.py
import pytest

class TestMathFunctions:
    """
    Test various math functions
    """

    def test_addition(self):
        """
        Test addition
        """
        assert 2 + 2 == 4

    def test_subtraction(self):
        """
        Test subtraction
        """
        assert 4 - 2 == 2

    @pytest.mark.parametrize("a, b, expected_result", [(2, 3, 5), (5, 7, 12)], ids=["test_addition_1", "test_addition_2"])
    def test_addition_parametrize(self, a, b, expected_result):
        """
        Test addition using parameterization
        """
        assert a + b == expected_result

    @pytest.mark.parametrize("a, b, expected_result", [(5, 3, 2), (7, 4, 3)], ids=["test_subtraction_1", "test_subtraction_2"])
    def test_subtraction_parametrize(self, a, b, expected_result):
        """
        Test subtraction using parameterization
        """
        assert a - b == expected_result

    def test_division(self):
        """
        Test division
        """
        with pytest.raises(ZeroDivisionError):
            1 / 0

    def test_multiplication(self):
        """
        Test multiplication
        """
        assert 3 * 4 == 12

    def test_modulo(self):
        """
        Test modulo
        """
        assert 5 % 2 == 1

class TestMiscFunctions:
    """
    Test various miscellaneous functions
    """

    def test_string(self):
        """
        Test string comparison
        """
        assert "hello" == "hello"

    def test_boolean(self):
        """
        Test boolean comparison
        """
        assert True != False

    def test_list(self):
        """
        Test list comparison
        """
        assert [1, 2, 3] == [1, 2, 3]

    def test_dictionary(self):
        """
        Test dictionary comparison
        """
        assert {"key1": "value1", "key2": "value2"} == {"key1": "value1", "key2": "value2"}

# This fixture will configure the HTML report
@pytest.fixture(scope="session")
def html_report_title():
    return "My HTML report"

# This fixture will generate the HTML report
@pytest.fixture(scope="session")
def html_report(pytestconfig, html_report_title):
  #  from pytest_html.reporter import HTMLReport
    from pytest_html import extras

    # Create a HTML report object with a custom title
    report = HTMLReport(pytestconfig)
    report.title = html_report_title

    # Add environment information to the report
    extras.append_metadata(report, "Python version", pytestconfig._metadata['Python'])
    extras.append_metadata(report, "Platform", pytestconfig._metadata['Platform'])
    extras.append_metadata(report, "Browser", pytestconfig._metadata['Browser'])

    yield report

    # Generate the report once all tests have completed
    report.generate_report()