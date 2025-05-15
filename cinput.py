import locationparser
#(city, state, country, [api])
#tolower
#cities must be given to call api
#states may or may not be given
#countries may or may not be given

#Empty strings are falsy
city = input('Enter city. ')
state = input('Enter state. ')
country = input('Enter country. ')

locationparser.parse_input(city, state, country)




