"""
Prac 10 - Wiki
"""
import wikipedia


def main():
    """Program to interact with the Wikipedia API using the 'wikipedia' package and display information about this program."""

    title = input("Enter page title: ")
    while title != "":
        try:
            page = wikipedia.page(title, autosuggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
            print()
        except wikipedia.exceptions.PageError:
            print(f"Page id '{title}' does not match any pages. Try another id!")
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search: ")
            print(e.options)
        title = input("Enter page title: ")
    print("Thank you")


main()
