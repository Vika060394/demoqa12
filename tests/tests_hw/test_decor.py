from pages.demoqa import DemoQa
import pytest

@pytest.mark.skip
def test_decor_3(browser):
    demo = DemoQa(browser)

    demo.visit()
    assert demo.h5.check_count_elements(6)

    for element in demo.h5.find_elements():
        assert element.text != ''