import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    password=YOUR_PASSWORD,
    database='nfl1' #this was the name of my database
)

cursor = db.cursor()

TEAMS = ['Patriots', 'Jets', 'Dolphins', 'Bills', 'Bengals', 'Steelers', 'Ravens', 'Browns', 'Colts', 'Titans', 'Jaguars', 'Texans', 'Broncos', 'Chiefs', 'Chargers', 'Raiders', 'Eagles', 'Cowboys', 'Giants', 'Redskins', 'Packers', 'Bears', 'Lions', 'Vikings', 'Panthers', 'Saints', 'Falcons', 'Buccaneers', 'Seahawks', '49ers', 'Cardinals', 'Rams']
teams_column_name_sql = ", ".join([f"{team} INT DEFAULT 0" for team in TEAMS])

sql_statement = f'''CREATE TABLE playoff_points (
    year INT, {teams_column_name_sql})
;'''
cursor.execute(sql_statement)

db.commit()
db.close()
