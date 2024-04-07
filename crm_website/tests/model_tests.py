from django.test import TestCase
from crm_website.models.customer_model import Customer

class CustomerTestCase(TestCase):
    def test_something(self):
        Customer.objects.create(first_name='Test')
        Customer.objects.create(last_name='Test2')
        
        obj = Customer.objects.get(first_name='Test')
        obj2 = Customer.objects.get(last_name='Test2')
        
        self.assertEqual(obj.first_name, 'Test')
        self.assertEqual(obj2.last_name, 'Test2')