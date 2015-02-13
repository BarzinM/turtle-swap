#!/usr/bin/env python

from time import gmtime, strftime, time, sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import os
import sys
import argparse
from selenium.webdriver.common.by import By

# Initializations
logger_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
i = 1
successful_verifications = 0
failed_verifications = 0
program_start_time = time()
warning_color = '\033[93m'
end_color = '\033[0m'
fail_color = '\033[91m'
fail_message = fail_color + '### VERIFICATION FAILD ###' + end_color

# Make argument parser and program help
parser = argparse.ArgumentParser(
    description='Save fully loaded HTML sources of a set of URLs. The program triggers all the JavaScript injected HTML parts coupled to scroll down event or other user specified events.')
parser.add_argument('-i', '--inputfile', help='Address of input file. This file should contain a list of URLs.', default=[])
parser.add_argument('-d', '--directory', help='Set the destination for saving sources.', default='../secret_closet/')
parser.add_argument('-t', '--text', help='Set the text to look for in the page before going to next page.', default='Price History')
parser.add_argument('-g', '--tag', help='Set the tag that contains the verification text to look for in the page before going to next page.', default='h2')
parser.add_argument('-l', '--leading-url', help='Set the tag that contains the verification text to look for in the page before going to next page.', default='')
parser.add_argument('-e', '--examination-count', help='Number of examination trials to get verification text from any of the verification tags', default='5')
parser.add_argument('-u', '--url', help='Extract source of just one URL specified with this argument.')
parser.add_argument('-j', '--jscode', help='Executes assigned the JavaScript code before finding verification text.', default='window.scrollTo(0,document.body.scrollHeight);')

args = parser.parse_args()
inputfile = args.inputfile
directory = args.directory
full_directory = args.directory + '/pages_extracted @' + logger_time + '/'
verification_text = args.text
verification_tag = args.tag
leading_url = args.leading_url
examination_count = int(args.examination_count)
if args.url:
    if inputfile:
        print fail_color + 'Program Terminated: Only one of the two arguments (URL, INPUTFILE) should have value.' + end_color
        sys.exit()
    else:
        search_set = [args.url]
else:
    if inputfile:
        search_set = np.genfromtxt(inputfile, dtype=None)
    else:
        print warning_color + 'URL argument (-u <URL>, --URL <URL>) or INPUTFILE argument (-i <input file>, --INPUTFILE <input file>) should be assigned. The URLs will be set as "http://google.com" + "http://en.wikipedia.org/wiki/Web_scraping" to demo the execution of the program.' + end_color
        search_set = ['http://google.com', 'http://en.wikipedia.org/wiki/Web_scraping']
number_of_urls = len(search_set)
log = number_of_urls > 0
js_code = args.jscode

# setup logger file
if log:
    logger_file = open(args.directory + 'crawler_logger @' + logger_time + '.txt', 'w')
# Make output directory if it does not exist
if not os.path.exists(full_directory):
    os.makedirs(full_directory)

# print args
print '-------------- Bulk HTML source extractor by BarzinM --------------'
print 'Input file is:', inputfile
print 'Results will be saved at:', full_directory

# get page source for each url
for list_url in search_set:

    # Initialization
    iteration_start_time = time()
    time_string = strftime("%Y-%m-%d_%H:%M:%S", gmtime())
    url = leading_url + list_url
    counter = str(i) + '/' + str(number_of_urls)
    print '\n' + counter + ':', url

    # setup adblock into driver
    ffprofile = webdriver.FirefoxProfile()
    ffprofile.set_preference('permissions.default.stylesheet', 2)
    ffprofile.set_preference('permissions.default.image', 2)
    ffprofile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

    adblockfile = 'adblockplusfirefox.xpi'
    ffprofile.add_extension(adblockfile)

    # Start firefox driver and to to url
    driver = webdriver.Firefox(ffprofile)
    driver.get(url)

    driver.execute_script(js_code)

    # verify existence of text in driver.page_source
    for j in range(examination_count):
        try:
            if driver.find_elements(By.XPATH, '//' + verification_tag + '[text()=' + verification_text + ']'):
                successful_verifications = successful_verifications + 1
                break
        except:
            print 'URL\'s complete load is not verified, trial:', j + 1, 'out of', examination_count
            if j < examination_count - 1:
                sleep(1)

    logger_file.write('%s: ' % counter)
    if j + 1 == examination_count:
        failed_verifications = failed_verifications + 1
        print fail_message
        logger_file.write(fail_message)
    pass
    logger_file.write('%s\n' % url)
    logger_file.flush()

    # Get page source and close driver session
    html_source = driver.page_source
    driver.close()

    # Make a soup out of the html_source for better formatting during save
    soup = BeautifulSoup(html_source)
    text = soup.prettify().encode('utf-8').strip()

    # write to file
    js_loaded_source_file = open(full_directory + time_string + '_' + url.replace('/', '[slash]') + '.html', 'w')
    # if j=something write something
    js_loaded_source_file.write("%s\n" % text)

    # close file
    js_loaded_source_file.close()
    i = i + 1

    print 'finished after:', time() - iteration_start_time, 'seconds'

# Generate result, display them on terminal and write them to logger file
program_end_time = time()
log_text = '\n############### Results:'
log_text = log_text + '\nOverall time for ' + str(number_of_urls) + ' URL(s): ' + str(program_end_time - program_start_time) + ' seconds'
log_text = log_text + '\nAverage extracting time: ' + str((program_end_time - program_start_time) / i) + ' seconds'
log_text = log_text + '\nNumber of successful verification(s): ' + str(successful_verifications)
log_text = log_text + '\nNumber of failed verification(s): ' + str(failed_verifications)


# close logger file
if log:
    print log_text
    logger_file.write('%s' % log_text)
    logger_file.close()
    print 'Results are saved at: ', args.directory
print '------------------- Program exited successfully -------------------'
