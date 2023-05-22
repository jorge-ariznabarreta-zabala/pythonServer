import sqlite3
con=sqlite3.connect("weather.db")
cur =con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cities(id, name, temperature, rain_probability)")
con.close()

def read(city_id):
    con=sqlite3.connect("weather.db")
    cur =con.cursor()
    res=cur.execute("SELECT id, name, temperature, rain_probability FROM cities WHERE id=?", [city_id])
    city_sql=res.fetchone()
    con.close()

    print("***************", city_sql)
    #queremos {"id": "BIO","name": "Bilbao","temperature": 30,"rain_probability": 0.5}
    #city_sql nos trae ('MAD', 'Madrid', '20', '0.5')
    city= { "id":city_sql[0], "name": city_sql[1], 'temperature':city_sql[2], "rain_probability":city_sql[3]}
    return city

def read_all():
    con=sqlite3.connect("weather.db")
    cur =con.cursor()
    res=cur.execute("SELECT id, name, temperature, rain_probability FROM cities")
    cities=res.fetchall()
    con.close()
    print("***************", cities)
    citi_list=[]
    for city_SQL in cities:
        #queremos {"id": "BIO","name": "Bilbao","temperature": 30,"rain_probability": 0.5}, {"id": 'MAD',"name": 'Madrid',"temperature": 20,"rain_probability": 0.5},...
        #cities nos trae [('BIO', 'Bilbao', '15', '1'), ('MAD', 'Madrid', '20', '0.5'), ('BER', 'Berlin', '15', '0.8'), ('MAN', 'Managua', '17', '.99')]
        city= { "id":city_SQL[0], "name": city_SQL[1], 'temperature':city_SQL[2], "rain_probability":city_SQL[3]}
        print("***************", city)
        citi_list.append(city)
    return citi_list


def create(new_city):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    values = (new_city['id'], new_city['name'], new_city['temperature'], new_city['rain_probability'])
    cur.execute("INSERT INTO cities (id, name, temperature, rain_probability) VALUES (?, ?, ?, ?)", values)
    con.commit()
    con.close()
    return "********he recibido una ciudad"


def update(update_city):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    values = (update_city['id'], update_city['name'], update_city['temperature'], update_city['rain_probability'])
    cur.execute("UPDATE cities SET id = ?, name = ?, temperature = ?, rain_probability = ? WHERE id = ?", values + (update_city['id'],))
    con.commit()
    con.close()
    return "Se ha actualizado una ciudad"

def delete(city_id):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    cur.execute("DELETE FROM cities WHERE id=?", (city_id,))
    con.commit()
    con.close()
    return 

