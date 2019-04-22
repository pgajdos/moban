import os

from nose.tools import eq_

from moban.copy import ContentForwardEngine


class TestCopyEncoding:
    def setUp(self):
        template_path = os.path.join("tests", "fixtures")
        self.engine = ContentForwardEngine([template_path])

    def test_encoding_of_template(self):
        template_content = self.engine.get_template("coala_color.svg")
        with open("tests/fixtures/coala_color.svg", "r") as expected:
            expected = expected.read()
        eq_(expected, template_content.decode("utf-8").replace("\r", ""))
