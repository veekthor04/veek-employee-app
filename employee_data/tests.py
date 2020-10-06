from django.test import TestCase
from .models import Data

# Create your tests here.
class EmployeeDataTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        # Create an employee data
        test_data = Data.objects.create(
            firstName="test_firstName", lastName="test_lastname", 
            employeeId=1234, city="test_city")
        test_data.save()

    def test_data_content(self):

        data = Data.objects.get(id=1)
        firstName = f'{data.firstName}'
        lastName = f'{data.lastName}'
        employeeId = f'{data.employeeId}'
        city = f'{data.city}'
        self.assertEqual(firstName, "test_firstName")
        self.assertEqual(lastName, "test_lastname")
        self.assertEqual(employeeId, "1234")
        self.assertEqual(city, "test_city")