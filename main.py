import json
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Changed Option to Options

# Step 1: Load contacts from the JSON file
def load_contacts():
    with open('chats.json', 'r') as file:
        data = json.load(file)
    return data['contacts']

# Step 2: Set up Selenium with Chrome options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("Please scan the QR code to log in.")
time.sleep(30)  # Wait for the user to scan the QR code

# Step 3: Function to send message to a contact
def send_message(contact_number, message):
    try:
        # Search for the contact by number
        search_box = driver.find_element(By.XPATH, "//div[@title='Search input textbox']")
        search_box.click()
        search_box.send_keys(contact_number)
        time.sleep(2)  # Wait for search results to appear
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for the chat to load

        # Type and send the message
        send_message_box = driver.find_element(By.XPATH, "//div[@title='Type a message']")
        send_message_box.click()
        send_message_box.send_keys(message)
        send_message_box.send_keys(Keys.RETURN)

        print(f"Message sent to {contact_number}")
        time.sleep(2)  # Short pause before sending the next message
    except Exception as e:
        print(f"Failed to send message to {contact_number}: {e}")

# Step 4: Load contacts from the JSON and send messages
contacts = load_contacts()
for contact in contacts:
    send_message(contact['contact'], contact['message'])

# Close the browser once done
driver.quit()
