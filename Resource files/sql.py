import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root',passwd = 'Pass@1234', database ='cricketfantasy')
cur = conn.cursor()
# query_bat = "Select name from stats where ctg = %s"
# cur.execute(query_bat, ('BAT',))
# batsmen = [i[0] for i in cur.fetchall()]

# for x in batsmen:
#     print(x)

# query = "Insert into teams values (%s, %s, %s)"
# cur.execute(query, ('Internshala', 'Kohli,Dhawan,Dhoni', 450,))
# conn.commit()

cur = conn.cursor()
# queryPlayers = 'Select players from teams where name = %s;'
# cur.execute(queryPlayers, ('KKR',))  # using tuple form adds ' ' for variables and values
# data = cur.fetchone()
# players = data[0].split(',')
# print(players)

matchName = 'match1'
playerName = 'Kohli'
# for table, we dont want another ' ', so we use it directly
query = "Select {0}.*, stats.ctg from {0}, stats where {0}.player_id = stats.player_id and stats.name = '{1}';".format(matchName, playerName)
# see this printed quuery
print(query)
cur.execute(query)
data = cur.fetchone()
print(data)
print(data[-1])
conn.close()