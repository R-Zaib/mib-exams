### MIB Exams
Task requirements:

BookPublisher
has a name

can publish given books

can show the published books (products): print all the published books after each other


A publisher can publish different types of books:


Fiction
can be created by its title, description and price

is represented in the following format:
«title» - «price»
«description»


Dictionary
can be created by the source language, the target language and the price

translations can be added later to it

a translation is a tuple with values: («word in source language», «word in target language»)

new dictionaries can be automatically generated from existing ones. For example if we have an English-Hungarian and an English-Russian dictionary, we should be able to generate a Hungarian-Russian dictionary by merging the common elements from the existing dictionaries. The price of the generated dictionary should be the price of the cheaper dictionary we use for generation.

is represented in the following format (after the first line, all the translations should appear in new lines):
«source» - «target» dictionary - «price»$
«word in source language» - «word in target language»


Tests
Write at least 2 unit tests/function calls to your dictionary merger function.




Complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

Handle errors with returning the integer -1 from the subunit, and optionally a print or log message explaining the nature of the error.

The following are some examples of how this class is used:

--

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid

--

# TODO: complete this class



class PaginationHelper:



    # The constructor takes in an array of items and a integer indicating

    # how many items fit within a single page

    def __init__(self, collection, items_per_page):

        pass



    # returns the number of items within the entire collection

    def item_count(self):

        pass



    # returns the number of pages

    def page_count(self):

        pass



    # returns the number of items on the current page. page_index is zero based

    # this method should return -1 for page_index values that are out of range

    def page_item_count(self, page_index):

        pass



    # determines what page an item is on. Zero based indexes.

    # this method should return -1 for item_index values that are out of range

    def page_index(self, item_index):

        pass