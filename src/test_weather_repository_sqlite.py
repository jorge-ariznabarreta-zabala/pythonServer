import unittest
from unittest.mock import patch

import sqlite3
from sqlite3 import Error

from weather_repository_sqlite import read, read_all, create, update, delete

class TestApp(unittest.TestCase):
    def setUp(self):
        # Establecer una conexión a una base de datos de prueba
        self.conn = sqlite3.connect(":memory:")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cities (id, name, temperature, rain_probability)")

    def tearDown(self):
        # Cerrar la conexión y eliminar la base de datos de prueba
        self.conn.close()

    def test_read(self):
        # Insertar datos de prueba en la tabla cities
        self.cur.execute("INSERT INTO cities VALUES (?, ?, ?, ?)", ('BIO', 'Bilbao', 30, 0.5))
        self.conn.commit()

        # Llamar a la función read para obtener los datos de una ciudad específica
        city = read('BIO')

        # Comprobar que los datos devueltos son los esperados
        self.assertEqual(city, {"id": "BIO", "name": "Bilbao", "temperature": 30, "rain_probability": 0.5})

    def test_read_all(self):
        # Insertar datos de prueba en la tabla cities
        cities_data = [('BIO', 'Bilbao', 30, 0.5), ('MAD', 'Madrid', 20, 0.5), ('BER', 'Berlin', 15, 0.8)]
        self.cur.executemany("INSERT INTO cities VALUES (?, ?, ?, ?)", cities_data)
        self.conn.commit()

        # Llamar a la función read_all para obtener todos los datos de las ciudades
        cities = read_all()

        # Comprobar que se devuelven todos los datos esperados
        expected_cities = [
            {"id": "BIO", "name": "Bilbao", "temperature": 30, "rain_probability": 0.5},
            {"id": "MAD", "name": "Madrid", "temperature": 20, "rain_probability": 0.5},
            {"id": "BER", "name": "Berlin", "temperature": 15, "rain_probability": 0.8}
        ]
        self.assertEqual(cities, expected_cities)

    def test_create(self):
        # Llamar a la función create para insertar una nueva ciudad
        new_city = {"id": "MIA", "name": "Miami", "temperature": 25, "rain_probability": 0.3}
        result = create(new_city)

        # Comprobar que la función devuelve el mensaje esperado
        self.assertEqual(result, "********he recibido una ciudad")

        # Comprobar que los datos se han insertado correctamente en la base de datos
        self.cur.execute("SELECT * FROM cities WHERE id=?", ('MIA',))
        city = self.cur.fetchone()
        self.assertIsNotNone(city)
        self.assertEqual(city, ('MIA', 'Miami', 25, 0.3))

    def test_update(self):
        # Insertar datos de prueba en la tabla cities
        self.cur.execute("INSERT INTO cities VALUES (?, ?, ?, ?)", ('MAD', 'Madrid', 20, 0.5))
        self.conn.commit()

        # Llamar a la función update para actualizar una ciudad existente
        update_city = {"id": "MAD", "name": "Madrid", "temperature": 25, "rain_probability": 0.7}
        result = update(update_city)

        # Comprobar que la función devuelve el mensaje esperado
        self.assertEqual(result, "Se ha actualizado una ciudad")

        # Comprobar que los datos se han actualizado correctamente en la base de datos
        self.cur.execute("SELECT * FROM cities WHERE id=?", ('MAD',))
        city = self.cur.fetchone()
        self.assertIsNotNone(city)
        self.assertEqual(city, ('MAD', 'Madrid', 25, 0.7))

    def test_delete(self):
        # Insertar datos de prueba en la tabla cities
        self.cur.execute("INSERT INTO cities VALUES (?, ?, ?, ?)", ('MAD', 'Madrid', 20, 0.5))
        self.conn.commit()

        # Llamar a la función delete para eliminar una ciudad existente
        delete('MAD')

        # Comprobar que la ciudad ha sido eliminada de la base de datos
        self.cur.execute("SELECT * FROM cities WHERE id=?", ('MAD',))
        city = self.cur.fetchone()
        self.assertIsNone(city)

if __name__ == '__main__':
    unittest.main()
