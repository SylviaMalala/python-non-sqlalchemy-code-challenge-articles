#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    author1 = Author("Monica Geller")
    author2 = Author("Ross Geller")

    mag1 = Magazine("Food & Fun", "Lifestyle")
    mag2 = Magazine("Dino Weekly", "Science")


    a1 = author1.add_article(mag1, "The Best Sandwich Ever")
    a2 = author1.add_article(mag1, "Holiday Cooking Tips")
    a3 = author1.add_article(mag1, "Kitchen Secrets")
    a4 = author2.add_article(mag2, "The History of Dinosaurs")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
