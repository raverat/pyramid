import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views.default import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'myproj')

    def test_notfound_view(self):
        from .views.notfound import notfound_view
        request = testing.DummyRequest()
        info = notfound_view(request)
        self.assertEqual(info, {})

