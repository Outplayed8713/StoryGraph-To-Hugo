#!/usr/bin/env python3
import os

os.system("~/projects/storygraph/storygraph.bash")
ftitles = open("titles", "r")
fimgs = open("imgs", "r")
fgenres = open("genres", "r")
freviews = open("reviews", "r")
titles = ftitles.readlines()
imgs = fimgs.readlines()
genres = fgenres.readlines()
reviews = freviews.readlines()


class Book:
    def __init__(self, title, genre, img, star="", rexp=""):
        self.title = title
        self.genre = genre
        self.img = img
        self.star = star
        self.rexp = rexp

    def __str__(self):
        return f"Title:{self.title}\nGenres:{self.genre}\nImg:{self.img}\nStars:{self.star}\nExplanation:{self.rexp}"


books = []


def make_books():
    for i, title in enumerate(titles):
        tbook = Book(title.strip(), genres[i].strip(), imgs[i].strip())
        books.append(tbook)
    for review in reviews:
        if review.isspace():
            continue
        try:
            rtitle, rstar, rexp = review.split(" | ")
        except Exception:
            rtitle, rstar = review.split(" | ")
            rstar = rstar[:-3]
            rexp = ""

        rtitle = rtitle.strip()
        rstar = rstar.strip()
        rexp = rexp.strip()
        for i, book in enumerate(books):
            if book.title == rtitle:
                books[i].star = rstar
                books[i].rexp = rexp


def make_md():
    fbook = open("books.md", "w")
    fbook.write('---\ntitle: "My Books"\ndraft: false\n---')
    fbook.write("## What is this page?\n")
    fbook.write(
        "Hi I made this page mainly as a challenge for myself to see if I could scrape my book reviews from storygraph using only command-line tools. FYI, some of these reviews are very old and out of order. The reviews are mainly for me to reminisce upon, so don't judge too harshly. =P "
    )
    fbook.write("{{< rawhtml >}}\n")
    for book in books:
        if book.title == "":
            continue
        fbook.write('<div class="book-container">\n')
        fbook.write('<div class="book-thumb"><img src=' + book.img + " /></div>\n")
        fbook.write('<div class="book-content">')
        if book.star == "":
            fbook.write('<h3 class="book-title">' + book.title + "</h3>")
        else:
            fbook.write(
                '<h3 class="book-title">' + book.title + " ⭐: " + book.star + "</h3>"
            )
        fbook.write('<h4 class="book-genre">' + book.genre + "</h4>")
        fbook.write("<p>" + book.rexp + "</p></div>")
        fbook.write("</div>")

    fbook.write("{{< /rawhtml >}}\n")


make_books()
make_md()

os.system("rm ~/website/content/books.md")
os.system("cp books.md ~/website/content/books.md")
