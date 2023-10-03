from unittest import TestCase

from pythonProject.oop.Diaries.dairy import Diary
from pythonProject.oop.Diaries.entry_not_found import EntryNotFound


class TestDairy(TestCase):
    def setUp(self) -> None:
        self.diary = Diary('moscarce', 'password')

    def test_diary_is_locked(self):
        self.assertTrue(self.diary.is_locked())
        self.assertEqual('moscarce',self.diary.get_username())

    def test_unlock_diary(self):
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.is_locked())

    def test_lock_diary(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_create_entry_and_find_entry_by_id(self):
        self.diary.create_entry('python assignment', 'testing my diary app')
        self.assertEqual(1, self.diary.entries_size())
        self.assertEqual('python assignment', self.diary.find_entry_by_id(1).get_title())

    def test_delete_entry(self):
        self.diary.create_entry('python assignment', 'testing my diary app')
        self.assertEqual(1, self.diary.entries_size())
        self.assertEqual('python assignment', self.diary.find_entry_by_id(1).get_title())
        self.diary.delete_entry(1)
        self.assertEqual(0, self.diary.entries_size())
        self.assertRaises(EntryNotFound, self.diary.find_entry_by_id, 1)

    def test_update_entry(self):
        self.diary.create_entry('python assignment', 'testing my diary app')
        self.assertEqual('python assignment', self.diary.find_entry_by_id(1).get_title())
        self.assertEqual(1, self.diary.entries_size())
        self.diary.update_entry(1, 'java assignment', 'testing my diary app')
        self.assertEqual(1, self.diary.entries_size())
        self.assertEqual('java assignment', self.diary.find_entry_by_id(1).get_title())
