from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import validators

import time

from dotenv import load_dotenv
import os
load_dotenv()

import localStorage



class EntradaSala():
    SUCCESS = 1
    FAIL = 0
    NO_ELEMENT = -1

class Haxball:
    def __init__(self):
        self.__driver = webdriver.Firefox()
        self.__nombre = os.getenv("nombre")
        self.__auth = os.getenv("auth")
        self.__sala = os.getenv("sala")
        self.__extrapolation = os.getenv("extrapolation")
        self.__geo = os.getenv("geo")
        self.__localStorage = localStorage.LocalStorage(self.__driver)
        self.__link = "https://www.haxball.com/play"
        self.__password = os.getenv("password")
    
    def irALink(self):
        self.__driver.get("https://www.haxball.com/play")
        return self.ponerNombre()

    def ponerVariablesDeLocalStorage(self):
        self.__localStorage.set("geo", self.__geo)
        self.__localStorage.set("player_auth_key", self.__auth)
        self.__localStorage.set("extrapolation", self.__extrapolation)
        return self.irABuscarSala()

    def ponerNombre(self):
        self.goToIframe()
        textField = self.__driver.find_element(By.CSS_SELECTOR, "input")
        textField.send_keys(self.__nombre)
        textField = self.__driver.find_element(By.CSS_SELECTOR, "button")
        return self.ponerVariablesDeLocalStorage()
    
    def irABuscarSala(self):
        botonIrASala = self.__driver.find_element(By.CSS_SELECTOR, "button")
        botonIrASala.click()
        return self.buscarSala()

    def buscarSala(self):
        print(f"Buscando sala: {self.__sala}")
        time.sleep(3)
        salas = self.__driver.find_elements(By.CSS_SELECTOR, 'span[data-hook="name"]')
        target_element = None
        for element in salas:
            print(element.get_attribute("innerHTML"))
            if self.__sala in element.get_attribute("innerHTML"):
                target_element = element
                break
        
            
        
        if target_element:
            actions = ActionChains(self.__driver)
            actions.double_click(target_element).perform()
            h1 = self.__driver.find_element(By.CSS_SELECTOR, 'h1')
            if (h1.get_attribute("innerHTML") == "Disconnected"):
                print("Disconnected from the room")
                print("Try again later")
                return EntradaSala.FAIL
            else:
                print("Connected to the room")
                return EntradaSala.SUCCESS
        else:
            print("No element with 'elo' in innerHTML was found.")
            return EntradaSala.NO_ELEMENT

    def goToIframe(self):
        iframe = self.__driver.find_element(By.CSS_SELECTOR, "iframe")
        self.__driver.switch_to.frame(iframe)

    def logToRoom(self):
        input = self.__driver.find_element(By.CSS_SELECTOR, "input")
        input.send_keys(f"!login {self.__password}")
        input.send_keys(Keys.ENTER)

    def setExtrapolation(self):
        input = self.__driver.find_element(By.CSS_SELECTOR, "input")
        input.send_keys(f"/extrapolation {self.__extrapolation}")
        input.send_keys(Keys.ENTER)

    def iterateUntilConnectSuccess(self):
        value = self.irALink()
        while (value == EntradaSala.FAIL):
            time.sleep(15)
            print("Trying to connect again")
            value = self.irALink()
        
        if (value == EntradaSala.NO_ELEMENT):
            print("Try again later")
        else:
            print("Setting the extrapolation")
            self.setExtrapolation()
            print("Loggin to the room")
            self.logToRoom()


def main():
    haxball = Haxball()
    haxball.iterateUntilConnectSuccess()

if __name__ == "__main__":
    main()