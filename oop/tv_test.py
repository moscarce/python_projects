import unittest

from oop.tv import TV


class TestTV(unittest.TestCase):
    def setUp(self) -> None:
        self.tv = TV()

    def test_tv_methods_with_tv_on(self):
        self.tv.turn_on()
    def test_that_i_can_get_channel_and_volume_with_on(self):
        self.tv.turn_on()
        self.assertEqual(0,self.tv.get_channel())
        self.assertEqual(0,self.tv.get_volume())
    def test_that_i_can_set_volume_with_tv_on(self):
        self.tv.turn_on()
        self.tv.set_volume(50)
        self.assertEqual(50,self.tv.get_volume())
        self.tv.set_volume(500)
        self.assertEqual(50,self.tv.get_volume())
        self.tv.volume_up()
        self.assertEqual(51,self.tv.get_volume())
        self.tv.volume_down()
        self.assertEqual(50,self.tv.get_volume())

    def test_that_i_can_set_channel_with_tv_on(self):
        self.tv.turn_on()
        self.tv.set_channel(30)
        self.assertEqual(30,self.tv.get_channel())
        self.tv.channel_up()
        self.assertEqual(31,self.tv.get_channel())
        self.tv.channel_down()
        self.assertEqual(30,self.tv.get_channel())

    def test_methods_with_tv_off(self):
        self.tv.turn_off()

    def test_that_i_cannot_get_volume_and_channel_when_tv_is_off(self):
        self.tv.turn_off()
        self.assertEqual(None, self.tv.get_channel())
        self.assertEqual(None, self.tv.get_volume())
    def test_that_i_cannot_set_volume_when_tv_is_off(self):
        self.tv.turn_off()
        self.tv.set_volume(50)
        self.assertEqual(None, self.tv.get_volume())
        self.tv.set_volume(500)
        self.assertEqual(None, self.tv.get_volume())
        self.tv.volume_up()
        self.assertEqual(None, self.tv.get_volume())
        self.tv.volume_down()
        self.assertEqual(None, self.tv.get_volume())
    def test_that_i_cannot_set_channel_when_tv_is_off(self):
        self.tv.turn_off()
        self.tv.set_channel(30)
        self.assertEqual(None, self.tv.get_channel())
        self.tv.channel_up()
        self.assertEqual(None, self.tv.get_channel())
        self.tv.channel_down()
        self.assertEqual(None, self.tv.get_channel())



