import os
import extract_data as ext
import pickle

path = '../secret_closet/pages_extracted @2015-02-21 16:51:16/'
files = [fi for fi in os.listdir(path) if fi.endswith('.html')]

address_array = []
for index, fi in enumerate(files):
    print index, fi
    addr, facts, area, history = ext.get_all_address(path + fi)
    address_array.append(addr)

output = open('list_of_addresses.txt', 'wb')
pickle.dump(address_array, output)
output.close()
