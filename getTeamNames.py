from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.pro-football-reference.com/years/2013/index.htm")
afcTeams = driver.find_elements_by_xpath('//table[@id="AFC"]/tbody/tr/th[@data-stat="team"]/a')
nfcTeams = driver.find_elements_by_xpath('//table[@id="NFC"]/tbody/tr/th[@data-stat="team"]/a')
teams = [team.text.split()[-1] for team in afcTeams] + [team.text.split()[-1] for team in nfcTeams]
print(teams)
