def searcher():
    import time
    # some 4 sconds time consuming task
    book = "this is a book on harry and code with harry"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("your text is in the book")
        else:
            print("text is not in the book")

search = searcher()
next(search)
search.send("harry")
input("press any key")
search.send("harry and")
