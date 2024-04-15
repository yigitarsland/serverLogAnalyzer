
def read_log(file_path):
    log_data = []  # Initialize an empty list to store log data
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()  # Split the log line into parts
            # Create a dictionary representing the log entry and append it to log_data list
            log_entry = {
                'ip': parts[0],
                'datetime': parts[3][1:] + ' ' + parts[4][:-1],  # Extract date and time without brackets and timezone
                'request': parts[5] + ' ' + parts[6] + ' ' + parts[7],  # Extract request method, URL, and protocol
                'status_code': parts[8],  # Extract status code
            }
            log_data.append(log_entry)
    return log_data

def ip_requests_number(log_data):
    ip_requests = {}  # Initialize an empty dictionary to store IP request counts
    for entry in log_data:
        ip = entry['ip']  # Get the IP address from the log entry
        ip_requests[ip] = ip_requests.get(ip, 0) + 1  # Increment the count for the IP address
    return ip_requests

def ip_find(log_data, most_active=True):
    ip_counts = ip_requests_number(log_data)  # Get the dictionary of IP request counts
    if most_active:
        max_requests = max(ip_counts.values())  # Find the maximum number of requests
        most_active_ips = [ip for ip, count in ip_counts.items() if count == max_requests]  # Find IPs with maximum requests
        return most_active_ips
    else:
        min_requests = min(ip_counts.values())  # Find the minimum number of requests
        least_active_ips = [ip for ip, count in ip_counts.items() if count == min_requests]  # Find IPs with minimum requests
        return least_active_ips

def longest_request(log_data):
    longest_request = ''  # Initialize variables to store the longest request and its IP address
    longest_ip = ''
    max_length = 0  # Initialize variable to store the maximum length of request
    for entry in log_data:
        request = entry['request']  # Get the request string from the log entry
        ip = entry['ip']  # Get the IP address from the log entry
        if len(request) > max_length:  # Check if current request length is greater than maximum length
            max_length = len(request)  # Update maximum length
            longest_request = request  # Update longest request string
            longest_ip = ip  # Update IP address corresponding to longest request
    return longest_request, longest_ip

def non_existent(log_data):
    non_existent_requests = set()  # Initialize a set to store unique non-existent requests
    for entry in log_data:
        status_code = entry['status_code']  # Get the status code from the log entry
        request = entry['request']  # Get the request string from the log entry
        if status_code == '404':  # Check if status code is 404 (Page not found)
            non_existent_requests.add(request)  # Add request string to set
    return list(non_existent_requests)  # Convert set to list and return

def run():
    file_path = "access_log-20230305"
    log_data = read_log(file_path)
    
    # Test the functions and print results
    print("Number of requests per IP:")
    print(ip_requests_number(log_data))
    print()
    
    print("Most active IPs:")
    print(ip_find(log_data, most_active=True))
    print()
    
    print("Least active IPs:")
    print(ip_find(log_data, most_active=False))
    print()
    
    print("Longest request:")
    print(longest_request(log_data))
    print()
    
    print("Non-existent requests:")
    print(non_existent(log_data))
    print()

if __name__ == "__main__":
    run()  # Execute the main function if the script is run directly
