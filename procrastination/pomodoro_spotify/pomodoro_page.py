#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 [Anselmos](github.com/anselmos) <anselmos@users.noreply.github.com>
#
# Distributed under terms of the MIT license.

from page_objects import PageObject, PageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PomodoroPage(PageObject):

    """Spotify Playlist Page for Selenium Page Object Pattern"""
    main_uri = "https://tomato-timer.com/"

    timer_start = PageElement(css='button[id="timer_start"]')

    def start_pomodoro(self):
        self.get(self.main_uri)
        self.timer_start.click()
