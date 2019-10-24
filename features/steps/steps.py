from operator import itemgetter
from behave import given, when, then
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import calendar
import uuid


@given(u'I am on the homepage')
def i_am_on_the_homepage(context):
    context.webdriver.get(context.host)
    context.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'logo')))


@given(u'I am logged out')
def i_am_logged_out(context):
    context.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'login')))


@when(u'I click "Sign in"')
def i_click_sign_in(context):
    element = context.webdriver.find_element_by_class_name('login')
    element.click()


@then(u'I see the "Authentication" page')
def i_see_the_authentication_page(context):
    context.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Authentication')]")))


@when(u'I enter a random email address')
def step_impl(context):
    element = context.webdriver.find_element_by_id('email_create')
    unique_id = uuid.uuid4().hex[:7]
    context.email = f'{unique_id}@example.com'
    element.send_keys(context.email)


@when(u'I click "Create an account"')
def step_impl(context):
    element = context.webdriver.find_element_by_id('SubmitCreate')
    element.click()


@then(u'I see the "Create an account" page')
def step_impl(context):
    context.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Create an account')]")))


@when(u'I Select the "Mr" radio button')
def i_select_the_mr_button(context):
    element = context.webdriver.find_element_by_id('id_gender1')
    element.click()


@when(u'I enter "{name}" into the first name field')
def step_impl(context, name):
    element = context.webdriver.find_element_by_id('customer_firstname')
    element.send_keys(name)


@when(u'I enter "{name}" into the last name field')
def step_impl(context, name):
    element = context.webdriver.find_element_by_id('customer_lastname')
    element.send_keys(name)


@when(u'I enter "{password}" into the password field')
def step_impl(context, password):
    element = context.webdriver.find_element_by_id('passwd')
    element.send_keys(password)


@when(u'I set the dropdown "day" to "{day}"')
def i_set_the_day_dropdown(context, day):
    actual_day = int(day)
    actual_day += 1  # There is a zero element in the list
    element = context.webdriver.find_element_by_xpath(f'//*[@id="days"]/option[{actual_day}]')
    element.click()


@when(u'I set the dropdown "month" to "{month}"')
def i_set_the_dropdown_month_to(context, month):
    position = None
    for counter, month_id in enumerate(calendar.month_name, start=1):
        if month == month_id:
            position = counter
            break
    assert position, "Unable to determine the proper month to select"

    element = context.webdriver.find_element_by_xpath(f'//*[@id="months"]/option[{position}]')
    element.click()  # This could equally have been done by selecting the specific option element via text, as below


@when(u'I set the dropdown "year" to "{year}"')
def i_set_the_dropdown_year_to(context, year):
    element = context.webdriver.find_element_by_xpath(f"//select[@id='years']/option[@value='{year}']")
    element.click()


@when(u'I enter "{name}" for the first name address field')
def i_enter_the_first_name(context, name):
    element = context.webdriver.find_element_by_id('firstname')
    element.send_keys(name)


@when(u'I enter "{name}" for the last name address field')
def i_enter_the_last_name(context, name):
    element = context.webdriver.find_element_by_id('lastname')
    element.send_keys(name)


@when(u'I enter the company "{company}" for the company field')
def i_enter_the_company(context, company):
    element = context.webdriver.find_element_by_id('company')
    element.send_keys(company)


@when(u'I enter "{street}" for the first address field')
def i_enter_the_street(context, street):
    element = context.webdriver.find_element_by_id('address1')
    element.send_keys(street)


@when(u'I enter "{street}" for the second address field')
def i_enter_the_second_street(context, street):
    element = context.webdriver.find_element_by_id('address2')
    element.send_keys(street)


@when(u'I enter the city "{city}" for the city field')
def i_enter_the_city(context, city):
    element = context.webdriver.find_element_by_id('city')
    element.send_keys(city)


@when(u'I select "{state}" for the state field')
def i_select_the_state(context, state):
    element = context.webdriver.find_element_by_xpath(f"//select[@id='id_state']/option[.='{state}']")
    element.click()


@when(u'I enter "{zip_code}" for the Zip code field')
def i_enter_the_zip_code(context, zip_code):
    element = context.webdriver.find_element_by_id('postcode')
    element.send_keys(zip_code)


@when(u'I enter "{number}" for the mobile phone number')
def i_enter_a_phone_number(context, number):
    element = context.webdriver.find_element_by_id('phone_mobile')
    element.send_keys(number)


@when(u'I enter "{alias}" for the alias field')
def i_enter_an_alias(context, alias):
    element = context.webdriver.find_element_by_id('alias')
    element.send_keys(alias)


@when(u'I click the Register button')
def i_click_register(context):
    element = context.webdriver.find_element_by_id('submitAccount')
    element.click()


@then(u'I see the My Account page')
def i_am_on_the_account_page(context):
    context.webdriver.find_element_by_id('my-account')


@when(u'I enter "{email}" into the signup email field')
def i_enter_signup_email(context, email):
    element = context.webdriver.find_element_by_id('email')
    element.send_keys(email)


@when(u'I enter "{password}" into the signup password field')
def i_enter_signup_password(context, password):
    element = context.webdriver.find_element_by_id('passwd')
    element.send_keys(password)


@when(u'I click the "Sign in" button')
def i_click_the_signin_button(context):
    element = context.webdriver.find_element_by_id('SubmitLogin')
    element.click()


@then(u'I see I am logged in as "{name}"')
def i_see_i_am_logged_in(context, name):
    context.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f'//span[contains(text(),"{name}")]')))


@given(u'I am logged in as "Peter Pan"')
def step_impl(context):
    context.execute_steps('''
        Given I am on the homepage
          And I am logged out
         When I click "Sign in"
         Then I see the "Authentication" page
         When I enter "existing@example.com" into the signup email field
          And I enter "40958730497856" into the signup password field
          And I click the "Sign in" button
         Then I see I am logged in as "Peter Pan"
    ''')


@when(u'I add the most expensive dress to the cart')
def step_impl(context):
    elements = context.webdriver.find_elements_by_class_name('product-container')
    prices = []
    for element in elements:
        price = element.find_element_by_class_name('product-price')
        actual_price = price.get_attribute('innerHTML')
        actual_price = actual_price.strip().replace('$', '')  # Get rid of the noise and the currency symbol
        prices.append((actual_price, element))

    prices.sort(key=itemgetter(0))  # Detrmine the highest price dress
    highest_priced_dress = prices[-1]
    context.webdriver.execute_script("return arguments[0].scrollIntoView();", highest_priced_dress[1])
    hover = ActionChains(context.webdriver).move_to_element(highest_priced_dress[1])
    hover.perform()

    highest_priced_dress[1].find_element_by_class_name('button').click()
    context.wait.until(expected_conditions.visibility_of_element_located((By.ID, 'layer_cart')))  # Confirm we can now see the cart
    context.webdriver.find_element_by_class_name('cross').click()  # dismiss the modal

    context.highest_priced_dress_price = highest_priced_dress[0]  # Save it so we can check it later


@when(u'I visit the dresses page')
def i_visit_the_dresses_page(context):
    context.webdriver.get('http://automationpractice.com/index.php?id_category=8&controller=category')
    context.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f'//p[contains(text(),"We offer")]')))


@when(u'I log out')
def step_impl(context):
    element = context.webdriver.find_element_by_class_name('logout')
    element.click()
    context.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'login')))


@when(u'I log in again as "Peter Pan"')
def step_impl(context):
    context.execute_steps('Given I am logged in as "Peter Pan"')


@then(u'I can see the most expensive dress is still in the cart')
def step_impl(context):
    context.webdriver.find_element_by_xpath('//*[text()="Cart"]').click()
    context.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f'//p[contains(text(),"Your shopping cart")]')))

    price = context.hightest_price_dress
    element = context.webdriver.find_element_by_class_name('cart_unit')
    cart_price = element.getAttruibute('innerHTML')
    assert price == cart_price
