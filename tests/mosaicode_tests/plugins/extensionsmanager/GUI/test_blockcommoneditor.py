from tests.mosaicode_tests.test_base import TestBase
from mosaicode.plugins.extensionsmanager.GUI.blockcommoneditor \
    import BlockCommonEditor


class TestBlockCommonEditor(TestBase):

    def setUp(self):
        self.widget = BlockCommonEditor(
                        None,
                        self.create_block())

    def test_base(self):
        self.widget = BlockCommonEditor(
                        None,
                        self.create_block())

