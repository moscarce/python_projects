from abc import ABC,abstractmethod

class TV:
    def __init__(self):
        self.__channel:int = 0
        self.__volume_level:int = 0
        self.__on:bool = False

    def turn_on(self):
        self.__on = True

    def turn_off(self):
        self.__on = False

    def get_channel(self):
        if self.__on: return self.__channel

    def set_channel(self,channel:int):
        if self.__on:
            if 101 > channel >= 0:
                self.__channel = channel

    def get_volume(self):
        if self.__on: return self.__volume_level

    def set_volume(self,volume_level:int):
        if self.__on:
            if 101 > volume_level >= 0:
                self.__volume_level = volume_level

    def channel_up(self):
        if self.__on:
            if 101 > self.__channel >= 0:
                self.__channel += 1

    def channel_down(self):
        if self.__on:
            if 101 > self.__channel >= 0:
                self.__channel -= 1

    def volume_up(self):
        if self.__on:
            if 101 > self.__volume_level >= 0:
                self.__volume_level += 1

    def volume_down(self):
        if self.__on:
            if 101 > self.__volume_level >= 0:
                self.__volume_level -= 1



