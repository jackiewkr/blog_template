"""sidebar.py

Generates the sidebar `a` tags based on the contents of the folder `blogposts/`.
"""
from bs4 import BeautifulSoup
import os

with open("templates/sidebar_template.html", "r") as f:
    soup = BeautifulSoup(f)
    navbar = soup.nav

    # adds all html blogposts to sidebar in order (not specified as any order)
    for file in os.listdir(os.fsencode("blogposts/")):
        fname = os.fsdecode(file)
        if fname.endswith(".html"):
            # add to navbar
            with open("blogposts/"+fname, "r") as f2:
                soup2 = BeautifulSoup(f2)
                title = soup2.title.string
                
                link = soup.new_tag("a", href="blogposts/"+fname)
                link.string = title
                navbar.append(link)

    with open("sidebar.html", "w") as out:
        out.write(soup.prettify())
