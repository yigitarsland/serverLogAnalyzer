Log Analyzer
This Python script, log_analyzer.py, provides functions to analyze server access logs. It reads log data from a file, extracts relevant information such as IP addresses, request details, and status codes, and performs various analyses on the data.

Functions:
read_log(file_path):

Reads the log file specified by file_path and parses each log entry.
Returns a list of dictionaries, each representing a log entry with fields like IP address, datetime, request details, and status code.

ip_requests_number(log_data):

Counts the number of requests made by each unique IP address.
Returns a dictionary where keys are IP addresses and values are the corresponding request counts.

ip_find(log_data, most_active=True):

Finds either the most or least active IP addresses based on the number of requests made.
Set most_active to True for finding the most active IPs, and False for the least active ones.
Returns a list of IP addresses with the highest or lowest request counts.

longest_request(log_data):

Identifies the longest request made based on the length of the request string.
Returns a tuple containing the longest request string and its corresponding IP address.

non_existent(log_data):

Finds requests that resulted in a "404 Not Found" status code, indicating non-existent pages.
Returns a list of unique non-existent requests.

run():

Executes the main functionality of the script.
Reads log data from a specified file, performs various analyses using the defined functions, and prints the results.

Usage:
To use this script, simply run it, and it will execute the main function, providing analyses based on the log file specified within the script.
