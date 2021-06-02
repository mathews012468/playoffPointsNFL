import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    password=YOUR_PASSWORD,
    database='nfl1'
)

cursor = db.cursor()

teams = ['Patriots', 'Jets', 'Dolphins', 'Bills', 'Bengals', 'Steelers', 'Ravens', 'Browns', 'Colts', 'Titans', 'Jaguars', 'Texans', 'Broncos', 'Chiefs', 'Chargers', 'Raiders', 'Eagles', 'Cowboys', 'Giants', 'Redskins', 'Packers', 'Bears', 'Lions', 'Vikings', 'Panthers', 'Saints', 'Falcons', 'Buccaneers', 'Seahawks', '49ers', 'Cardinals', 'Rams']
teamStatement = ["SUM(" + team + ")" for team in teams]

sqlStatement = "SELECT " + ", ".join(teamStatement) + "FROM playoff_points WHERE year>2010;"
cursor.execute(sqlStatement)
sums = cursor.fetchall()

teamSums = [(teams[i], sums[0][i]) for i in range(32)]
sortedSums = sorted(teamSums, key = lambda x: x[1])
[print(sortedSum[0], sortedSum[1]) for sortedSum in sortedSums]
