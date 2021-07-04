from unittest import TestCase

from org.app.app import whatevz


class AnyTestCase(TestCase):
    def test_thing(self) -> None:
        self.assertTrue(whatevz())
