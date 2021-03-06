
import psycopg2
# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL, start_time varchar, user_id varchar, level varchar ,song_id varchar, artist_id varchar, session_id varchar, 
location varchar, user_agent varchar);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar, title varchar, artist_id varchar, year int, duration numeric); 
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id varchar, name varchar, location varchar, lattitude decimal, longitude decimal );
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time time, hour int, day int, week int, month int, year int, weekday varchar);
""")
# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level,song_id, artist_id, session_id, location, user_agent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES(%s,%s,%s,%s,%s)
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES(%s, %s, %s, %s, %s) 
""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, lattitude, longitude) VALUES (%s,%s,%s,%s,%s)
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES(%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS
try :
    song_select = ("""Select songs.song_id, artists.artist_id FROM songs LEFT JOIN artists ON songs.artist_id = artists.artist_id where 
                    title = (%s) and name = (%s) and duration = (%s) """)
    #print(song_select)
except psycopg2.Error as e:
    print("Query is wrong")
    print(e)
        
    
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]