import mysql.connector as mysql
from selenium import webdriver

db = mysql.connect(
    host='localhost',
    user='root',
    password=YOUR_PASSWORD,
    database='nfl1' #this was the name of my database
)

cursor = db.cursor()

driver = webdriver.Chrome()

for year in range(2020, 1969, -1):
    print(year)
    url = f"https://www.pro-football-reference.com/years/{year}/index.htm"
    driver.get(url)

    cursor.execute(f"INSERT INTO playoff_points (year) VALUES ({year})")

    playoffGames = driver.find_elements_by_xpath('//table[@id="playoff_results"]/tbody/tr')
    for game in playoffGames:
        round = game.find_element_by_xpath('./th').text
        winner = game.find_element_by_xpath('./td[@data-stat="winner"]/strong').text.split()[-1]
        loser = game.find_element_by_xpath('./td[@data-stat="loser"]/a').text.split()[-1]

        if winner == "Oilers":
            winner = "Titans"
        if loser == "Oilers":
            loser = "Titans"

        if winner == "Team":
            winner = "Redskins" 
        if loser == "Team":
            loser = "Redskins" 

        loserPoints = {"WildCard": 1, "Division": 2, "ConfChamp": 4, "SuperBowl": 8}
        cursor.execute(f"UPDATE playoff_points SET {loser}={loserPoints[round]} WHERE year={year}")
        if round == "SuperBowl":
            cursor.execute(f"UPDATE playoff_points SET {winner}=16 WHERE year={year}")

db.commit()
db.close()
