import selenium

from selenium import webdriver

# Spuštění webového prohlížeče
driver = webdriver.Chrome()  # Budete potřebovat ovladač pro prohlížeč, jako například ChromeDriver, stažený a přidaný do vaší cesty
driver.get("https://www.example.com")