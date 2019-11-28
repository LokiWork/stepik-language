import time

def test_button_is_displayed(browser):
	time.sleep(30)
	button = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
	assert button.is_displayed(), "Button is not displayed"