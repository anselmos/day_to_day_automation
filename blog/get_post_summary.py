#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 [Anselmos](github.com/anselmos) <anselmos@users.noreply.github.com>
#
# Distributed under terms of the MIT license.

import pyperclip
import argparse
YOUR_DOMAIN = "http://witkowskibartosz.com/blog/"


def get_summary(post_file_markdown):
    SLUG_TAG = "Slug: "
    SUMMARY_TAG = "Summary: "
    summary = ""
    slug = ""
    with open(post_file_markdown, 'r') as filemarkdown:
        for line in filemarkdown.read().split("\n"):
            if SLUG_TAG in line:
                slug = line.split(SLUG_TAG)[1]
            if SUMMARY_TAG in line:
                summary = line.split(SUMMARY_TAG)[1]

    return (slug, summary)


def make_social_text_and_copy(slug, summary):
    text = summary + " : "+ YOUR_DOMAIN + slug + ".html"
    pyperclip.copy(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Arguments of this script')
    parser.add_argument('markdownfile', metavar='N', type=str, nargs='+')
    args = parser.parse_args()
    data = get_summary(args.markdownfile[0])
    make_social_text_and_copy(*data)
