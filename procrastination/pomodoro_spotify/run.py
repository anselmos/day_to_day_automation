#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 [Anselmos](github.com/anselmos) <anselmos@users.noreply.github.com>
#
# Distributed under terms of the MIT license.

from selenium import webdriver
from spotify_playlist import SpotifyPlaylist

def main():
    driver = webdriver.Firefox()
    spotify_page = SpotifyPlaylist(driver)
    spotify_page.open_album('56QpDqnTzXqMn3Jjxv73lz')

if __name__ == "__main__":
    main()
