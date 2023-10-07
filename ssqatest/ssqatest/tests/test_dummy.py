import pytest
 
@pytest.mark.usefixtures('init_driver')
class TestDummy():
 
    def test_dummy(self):
        print("I'm a dummy test line 1")
        self.driver.get("https://youtube.com")
        import pdb; pdb.set_trace()