#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 [Anselmos](github.com/anselmos) <anselmos@users.noreply.github.com>
#
# Distributed under terms of the MIT license.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from spotify_playlist import SpotifyPlaylist
from pomodoro_page import PomodoroPage

def main():
    driver = webdriver.Firefox()
    album_id = '56QpDqnTzXqMn3Jjxv73lz'
    driver.execute_script('''window.open("https://open.spotify.com/album/{}", "_blank");'''.format(album_id))
    pomodoro_timer = PomodoroPage(driver)
    pomodoro_timer.start_pomodoro()

if __name__ == "__main__":
    main()
