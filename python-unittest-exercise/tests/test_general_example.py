
from unittest.mock import patch

from src.general_example import GeneralExample


class TestGeneralExample:

    def setup_method(self):
        self.example = GeneralExample()

    # Test 1: Flatten dictionary and sort values
    def test_flatten_dictionary(self):
        data = {
            "key1": [3, 2, 1],
            "key2": [42, 55, 10],
            "key3": [0, 22]
        }

        result = self.example.flatten_dictionary(data)

        assert result == [0, 1, 2, 3, 10, 22, 42, 55]

    # Test 2: Remove duplicate values
    def test_flatten_dictionary_duplicates(self):
        data = {
            "key1": [1, 2, 2],
            "key2": [2, 3, 3]
        }

        result = self.example.flatten_dictionary(data)

        assert result == [1, 2, 3]

    # Test 3: Handle an empty dictionary
    def test_flatten_dictionary_empty(self):
        result = self.example.flatten_dictionary({})

        assert result == []

    # Test 4: Fetch employee details using a mocked database
    @patch.object(
        GeneralExample,
        "load_employee_rec_from_database",
        return_value=["emp001", "Sam", "100000"]
    )
    def test_fetch_emp_details(self, mock_database):
        result = self.example.fetch_emp_details()

        assert result == {
            "empId": "emp001",
            "empName": "Sam",
            "empSalary": "100000"
        }

        mock_database.assert_called_once_with()
