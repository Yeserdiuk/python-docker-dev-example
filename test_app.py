import unittest
from app import app, create_db_and_tables, create_hero, read_heroes
from sqlmodel import Session, SQLModel
from config import settings

class TestApp(unittest.TestCase):
    def test_create_db_and_tables(self):
        create_db_and_tables()
        self.assertTrue(SQLModel.metadata.tables)

    def test_create_hero(self):
        hero = create_hero(Hero(name='Test Hero', secret_name='Test Secret Name', age=30))
        self.assertEqual(hero.name, 'Test Hero')
        self.assertEqual(hero.secret_name, 'Test Secret Name')
        self.assertEqual(hero.age, 30)

    def test_read_heroes(self):
        heroes = read_heroes()
        self.assertEqual(len(heroes), 1)
        self.assertEqual(heroes[0].name, 'Test Hero')
        self.assertEqual(heroes[0].secret_name, 'Test Secret Name')
        self.assertEqual(heroes[0].age, 30)

if __name__ == '__main__':
    unittest.main()