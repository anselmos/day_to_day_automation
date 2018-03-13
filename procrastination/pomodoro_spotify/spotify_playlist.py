#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 [Anselmos](github.com/anselmos) <anselmos@users.noreply.github.com>
#
# Distributed under terms of the MIT license.

"""

"""
class SpotifyPlaylist(object):

    """Spotify Playlist Page for Selenium Page Object Pattern"""
    album_uri = "https://open.spotify.com/album/"
    playlist_uri = "https://open.spotify.com/playlist/"

    def __init__(self, driver, playlist_id):
        """TODO: to be defined1. """
        self.driver = driver
        self.playlist_id = playlist_id

    def open_playlist(self):
        self.driver.get(self.playlist_uri + self.playlist_id)

    def open_album(self, album_id):
        self.driver.get(self.album_uri + album_id)
