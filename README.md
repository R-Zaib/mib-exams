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