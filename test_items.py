def test_button_is_displayed(browser):
	button = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
	assert button.is_displayed()