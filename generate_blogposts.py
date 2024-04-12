"""generate_blogposts.md

Generates HTML blogposts from Markdown using md4c."""

import subprocess
import os
from datetime import datetime
from bs4 import BeautifulSoup

MD_FILEDIR = "blogposts_md/"
HTML_FILEDIR = "blogposts/"
TEMPLATE_DIR = "templates/blogpost_template.html"


def create_blog_html(fname, time_mod):
    """Creates a blogpost from supplied md file."""
    try:
        result = subprocess.run(["md2html", MD_FILEDIR + fname],
                                stdout=subprocess.PIPE )
    except subprocess.CalledProcessError as cpe:
        print("File: " + fname + " is not a valid MD file.")
        return

    soup = BeautifulSoup(result.stdout)
    md_title = soup.h1.string

    with open(HTML_FILEDIR + os.path.splitext(fname)[0] + ".html", "w") as out:
        soup2 = BeautifulSoup(open(TEMPLATE_DIR, "r"))

        soup2.main.append(soup)

        # add time to file in case it is needed later
        soup2.title.string = md_title
        soup2.aside.string = datetime.fromtimestamp(time_mod).strftime("%d %b - %H:%M")
        soup2.time.string = str(time_mod)

        out.write(soup2.prettify())    


for file in os.scandir(os.fsencode("blogposts_md/")):
    fname = os.fsdecode(file.name)
    create_blog_html(fname, os.stat(MD_FILEDIR + fname).st_mtime)

