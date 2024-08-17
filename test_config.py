import unittest
from config import Settings

class TestConfig(unittest.TestCase):
    def test_settings(self):
        settings = Settings()
        self.assertEqual(settings.POSTGRES_SERVER, 'localhost')
        self.assertEqual(settings.POSTGRES_PORT, 5432)
        self.assertEqual(settings.POSTGRES_USER, 'myuser')
        self.assertEqual(settings.POSTGRES_PASSWORD, 'mypassword')
        self.assertEqual(settings.POSTGRES_DB, 'mydb')

    def test_sqlalchemy_database_uri(self):
        settings = Settings()
        uri = settings.SQLALCHEMY_DATABASE_URI
        self.assertEqual(uri.scheme, 'postgresql+psycopg')
        self.assertEqual(uri.username, 'myuser')
        self.assertEqual(uri.password, 'mypassword')
        self.assertEqual(uri.host, 'localhost')
        self.assertEqual(uri.port, 5432)
        self.assertEqual(uri.path, '/mydb')

if __name__ == '__main__':
    unittest.main()