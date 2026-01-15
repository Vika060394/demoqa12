from pages.alerts import Alerts
import time

def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert alert_page.timer_alertButton.exist()
    alert_page.timer_alertButton.click()
    time.sleep(7)
    assert alert_page.alert()
    alert_page.alert().accept()
