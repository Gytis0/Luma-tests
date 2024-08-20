import unittest

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

        #Open the site
        driver.get("https://magento.softwaretestingboard.com/")

        #Find the dropdown elements
        #Navigate to mens hoodies
        mensElement = driver.find_element(By.ID, "ui-id-5")
        hover = ActionChains(driver).move_to_element(mensElement)
        hover.perform()

        topsElement = driver.find_element(By.ID, "ui-id-17")
        hover = ActionChains(driver).move_to_element(topsElement)
        hover.perform()

        hoodiesElement = driver.find_element(By.ID, "ui-id-20")
        hoodiesElement.click()

        #Find all displayed items
        listOfItems = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='products list items product-items']")))
        allItems = listOfItems.find_elements(By.TAG_NAME, "li")

        selecter = driver.find_element(By.ID, "limiter")
        options = selecter.find_elements(By.XPATH, ".//*")

        #Find selected items per page count
        selectedPerPage = 0
        for option in options:
            if option.get_property("selected") == True:
                selectedPerPage = int(option.get_attribute("value"))
                break

        #Assert that count of displayed items equals to selected items per page
        self.assertEqual(selectedPerPage, len(allItems))

        #Find and navigate to frankie sweatshirt
        frankieSweatshirt = driver.find_element(By.LINK_TEXT, "Frankie Sweatshirt")
        frankieSweatshirt.click()

        #Select attributes
        smallSizeButton = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "option-label-size-143-item-167")))
        smallSizeButton.click()

        yellowColourButton = driver.find_element(By.ID, "option-label-color-93-item-60")
        yellowColourButton.click()

        quantityToOrder = "2"
        quantityField = driver.find_element(By.ID, "qty")
        quantityField.clear()
        quantityField.send_keys(quantityToOrder)

        #Add to cart
        addToCart = driver.find_element(By.ID, "product-addtocart-button")
        addToCart.click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='counter qty']")))

        #Assert that quantity of ordered items equals to the count of items in the cart
        self.assertEqual(driver.find_element(By.CLASS_NAME, "counter-number").text, quantityToOrder)

        #Open the details about the item
        cartButton = driver.find_element(By.XPATH, "//*[@class='action showcart']")
        cartButton.click()

        toggleButton = driver.find_element(By.XPATH, "//*[@class='toggle']")
        toggleButton.click()

        #Find the details
        details = driver.find_element(By.XPATH, "//*[@class='product options list']")
        detailsInfo = details.find_elements(By.TAG_NAME, "dd")

        #Assert that the details shown here match the ones that were selected in the item page
        self.assertEqual(detailsInfo[0].text, "S")
        self.assertEqual(detailsInfo[1].text, "Yellow")

        #Go to checkout
        checkoutButton = driver.find_element(By.ID, "top-cart-btn-checkout")
        checkoutButton.click()

        #Fill the form
        emailField = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "customer-email")))
        emailField.clear()
        emailField.send_keys("testEmail@mail.com")

        firstNameField = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "firstname")))
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

        #Wait for billing address to load so it wouldn't get in the way later
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='billing-address-details']")))
        placeOrderButton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='action primary checkout']")))
        placeOrderButton.click()

        #Assert that the order was successful
        checkoutObject = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='checkout-success']")))
        checkoutChildren = checkoutObject.find_elements(By.TAG_NAME, "p")

        self.assertEqual("We'll email you an order confirmation with details and tracking info.", checkoutChildren[1].text)

    def test_scenario_2(self):
        driver = self.driver

        #Open the site
        driver.get("https://magento.softwaretestingboard.com/")

        #Navigate to women's pants section
        womensElement = driver.find_element(By.ID, "ui-id-4")
        hover = ActionChains(driver).move_to_element(womensElement)
        hover.perform()

        bottomsElement = driver.find_element(By.ID, "ui-id-10")
        hover = ActionChains(driver).move_to_element(bottomsElement)
        hover.perform()

        pantsElement = driver.find_element(By.ID, "ui-id-15")
        pantsElement.click()

        #Find and click sorter
        sorter = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "sorter")))
        sorter.click()

        #Sort by price
        options = sorter.find_elements(By.XPATH, ".//*")
        for option in options:
            if option.text == "Price":
                option.click()

        #Add 3 first items to the cart
        lastCount = 0
        for i in range(3):
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='item product product-item']")))
            listOfItems = driver.find_elements(By.XPATH, "//*[@class='item product product-item']")
            listOfItems[i].click()

            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "product-addtocart-button")))

            sizeButton = driver.find_element(By.XPATH, "//*[@class='swatch-option text']")
            sizeButton.click()
            colorButton = driver.find_element(By.XPATH, "//*[@class='swatch-option color']")
            colorButton.click()

            addButton = driver.find_element(By.ID, "product-addtocart-button")
            addButton.click()

            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='counter qty']")))
            self.assertGreater(int(driver.find_element(By.CLASS_NAME, "counter-number").text), lastCount)
            lastCount = int(driver.find_element(By.CLASS_NAME, "counter-number").text)

            driver.back()

        #Navigate to cart
        cartButton = driver.find_element(By.XPATH, "//*[@class='action showcart']")
        cartButton.click()

        actionViewCart = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='action viewcart']")))
        viewCheckout = actionViewCart.find_element(By.TAG_NAME, "span")
        viewCheckout.click()

        #Find and navigate to the first suggested item
        allItems = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='products list items product-items']")))
        options = allItems.find_elements(By.TAG_NAME, "li")

        options[0].find_element(By.TAG_NAME, "img").click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='action primary tocart']")))

        #Choose size and color if the item has such options
        try:
            sizeButton = driver.find_element(By.XPATH, "//*[@class='swatch-option text']")
            sizeButton.click()
            colorButton = driver.find_element(By.XPATH, "//*[@class='swatch-option color']")
            colorButton.click()
        except:
            print("Item does not have any color or size options.")

        #Add to the cart
        addButton = driver.find_element(By.ID, "product-addtocart-button")
        addButton.click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='counter qty']")))

        #Find and remove first item in the cart
        cartButton = driver.find_element(By.XPATH, "//*[@class='action showcart']")
        cartButton.click()

        deleteButton = driver.find_element(By.XPATH, "//*[@class='action delete']")
        deleteButton.click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='action-primary action-accept']")))
        acceptButton = driver.find_element(By.XPATH, "//*[@class='action-primary action-accept']")
        acceptButton.click()

        #Go to checkout and fill out the forms
        checkoutButton = driver.find_element(By.XPATH, "//*[@class='action primary checkout']")
        checkoutButton.click()

        emailField = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "customer-email")))
        emailField.clear()
        emailField.send_keys("testEmail@mail.com")

        firstNameField = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "firstname")))
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

        #shippingMethodObject = driver.find_element(By.XPATH, "//*[@class='checkout-shipping-method-load']")
        shippingMethodObject = driver.find_element(By.ID, "checkout-shipping-method-load")
        shippingMethodRadio = shippingMethodObject.find_elements(By.XPATH, "//*[@class='radio']")
        shippingMethodRadio[1].click()

        nextButton = driver.find_element(By.XPATH, "//*[@class='button action continue primary']")
        nextButton.click()

        billingAddress = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='billing-address-details']")))
        placeOrderButton = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='action primary checkout']")))
        placeOrderButton.click()

        checkoutObject = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='checkout-success']")))
        checkoutChildren = checkoutObject.find_elements(By.TAG_NAME, "p")

        #Assert that the order was successful
        self.assertEqual("We'll email you an order confirmation with details and tracking info.",
                         checkoutChildren[1].text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()