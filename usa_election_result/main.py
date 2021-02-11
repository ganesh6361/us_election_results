import pandas
wiki = pandas.read_html('https://en.wikipedia.org/wiki/2020_United_States_presidential_election')
election = wiki[4]
print(election)
