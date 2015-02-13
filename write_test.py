
from time import gmtime, strftime

# Some initializations
time_string = strftime("%Y-%m-%d %H:%M:%S", gmtime())
house_list_file = open('House_list_at_' + time_string + '.txt', 'w')
for house in range(10):
    house_list_file.write("%s\n" % house)

house_list_file.close()
