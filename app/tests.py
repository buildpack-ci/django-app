from django.test import TestCase

# Create your tests here.
class NopTestCase(TestCase):
    def test_true(self):
        self.assertTrue(1)
