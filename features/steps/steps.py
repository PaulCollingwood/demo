from behave import given, when, then
from selenium.webdriver.support import expected_conditions
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
