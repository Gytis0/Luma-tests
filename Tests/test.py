import unittest
from token import EQUAL

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class LumaTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_scenario_1(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        mensElement = driver.find_element(By.ID, "ui-id-5")
        hover = ActionChains(driver).move_to_element(mensElement)
        hover.perform()

        topsElement = driver.find_element(By.ID, "ui-id-17")
        hover = ActionChains(driver).move_to_element(topsElement)
        hover.perform()

        hoodiesElement = driver.find_element(By.ID, "ui-id-20")
        hoodiesElement.click()

        listOfItems = driver.find_elements(By.XPATH ,"//*[@class='item product product-item']")

        selecter = driver.find_element(By.ID, "limiter")
        options = selecter.find_elements(By.XPATH, ".//*")

        selectedPerPage = 0
        for option in options:
            if option.get_property("selected") == True:
                selectedPerPage = int(option.get_attribute("value"))
                break

        self.assertEqual(selectedPerPage, len(listOfItems))

        frankieSweatshirt = driver.find_element(By.LINK_TEXT, "Frankie Sweatshirt")
        frankieSweatshirt.click()

        smallSizeButton = driver.find_element(By.ID, "option-label-size-143-item-167")
        smallSizeButton.click()

        yellowColourButton = driver.find_element(By.ID, "option-label-color-93-item-60")
        yellowColourButton.click()

        quantityToOrder = "2"
        quantityField = driver.find_element(By.ID, "qty")
        quantityField.clear()
        quantityField.send_keys(quantityToOrder)

        addToCart = driver.find_element(By.ID, "product-addtocart-button")
        addToCart.click()

        doesExist = False
        try:
            doesExist = WebDriverWait(driver, 4).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "counter-number"), quantityToOrder)
            )
        except:
            print("Counter number does not equal to the quantity ordered")

        if doesExist:
            self.assertEqual(driver.find_element(By.CLASS_NAME, "counter-number").text, quantityToOrder)

        cartButton = driver.find_element(By.XPATH, "//*[@class='action showcart']")
        cartButton.click()

        toggleButton = driver.find_element(By.XPATH, "//*[@class='toggle']")
        toggleButton.click()

        details = driver.find_element(By.XPATH, "//*[@class='product options list']")
        detailsInfo = details.find_elements(By.TAG_NAME, "dd")

        self.assertEqual(detailsInfo[0].text, "S")
        self.assertEqual(detailsInfo[1].text, "Yellow")

        checkoutButton = driver.find_element(By.ID, "top-cart-btn-checkout")
        checkoutButton.click()

        try:
            doesExist = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.ID, "customer-email"))
            )
        except:
            print("Fields are not visible")

        emailField = driver.find_element(By.ID, "customer-email")
        emailField.clear()
        emailField.send_keys("testEmail@mail.com")

        try:
            doesExist = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "firstname"))
            )
        except:
            print("Fields are not visible")

        firstNameField = driver.find_element(By.NAME, "firstname")
        firstNameField.clear()
        firstNameField.send_keys("testFirstName")

        lastNameField = driver.find_element(By.NAME, "lastname")
        lastNameField.clear()
        lastNameField.send_keys("testLastName")

        addressField = driver.find_element(By.NAME, "street[0]")
        addressField.clear()
        addressField.send_keys("testAddress")

        cityField = driver.find_element(By.NAME, "city")
        cityField.clear()
        cityField.send_keys("testCity")

        select = Select(driver.find_element(By.NAME, 'region_id'))
        select.select_by_index(1)

        zipCode = driver.find_element(By.NAME, "postcode")
        zipCode.clear()
        zipCode.send_keys("01234")

        select = Select(driver.find_element(By.NAME, 'country_id'))
        select.select_by_index(1)

        phoneField = driver.find_element(By.NAME, "telephone")
        phoneField.clear()
        phoneField.send_keys("testPhone")

        shippingMethodRadio = driver.find_element(By.NAME, "ko_unique_2")
        shippingMethodRadio.click()

        nextButton = driver.find_element(By.XPATH, "//*[@class='button action continue primary']")
        nextButton.click()



        billingAddress = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='billing-address-details']")))
        placeOrderButton = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='action primary checkout']")))
        placeOrderButton.click()

        checkoutSuccess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='checkout-success']")))
        checkoutObject = driver.find_element(By.XPATH, "//*[@class='checkout-success']")
        checkoutChildren = checkoutObject.find_elements(By.TAG_NAME, "p")

        self.assertEqual("We'll email you an order confirmation with details and tracking info.", checkoutChildren[1].text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()