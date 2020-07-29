def test_add_to_basket_button_presense(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    basket_button = browser.find_element_by_css_selector('.btn-primary')
    assert basket_button, 'No "Add to basket" button'
