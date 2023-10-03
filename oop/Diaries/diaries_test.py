from unittest import TestCase

from pythonProject.oop.Diaries.custom_exception.diary_not_found import DiaryNotFound
from pythonProject.oop.Diaries.diaries import Diaries


class testDiaries(TestCase):
    def setUp(self) -> None:
        self.diaries = Diaries()
        self.diaries.add('tobi', '1234')

    def test_add_diary_and_find_by_username(self):
        self.assertEqual('tobi', self.diaries.find_by_username('tobi').get_username())

    def test_delete_diary(self):
        self.diaries.add('tayo','1234')
        self.assertEqual('tayo', self.diaries.find_by_username('tayo').get_username())
        self.diaries.delete('tayo','1234')
        self.assertRaises(DiaryNotFound, self.diaries.find_by_username,'tayo')

