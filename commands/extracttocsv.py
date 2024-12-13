from opensearchpy import OpenSearch
import pandas as pd
import csv

# Function to connect to OpenSearch
def connect_to_opensearch(host, port, username, password):
    client = OpenSearch(
        hosts = [{'host': host, 'port': port}],
        http_auth = (username, password),
        http_compress = True,
        use_ssl = True,
        verify_certs = False,
        ssl_assert_hostname = False,
        ssl_show_warn = False,
    )
    return client

# Function to retrieve records
def retrieve_high_status_code_records(client, index_name, start_time, end_time):
    query = {
        "query": {
            "range": {
                "@timestamp": {
                    "gte": start_time,
                    "lt": end_time,
                    "format": "strict_date_time"
                }
            }
        }
    }

    # Initialize an empty list to hold the results
    results = []

    # Scroll API parameters
    response = client.search(
        index=index_name,
        body=query,
        scroll='30m',  # Keep the search context alive for 2 minutes
        size=10000  # Number of results per batch
    )

    # Get the scroll ID
    scroll_id = response['_scroll_id']

    # Iterate over the batches
    while len(response['hits']['hits']) > 0:
        # Append the current batch of results to the list
        results.extend(response['hits']['hits'])

        # Fetch the next batch using the scroll ID
        response = client.scroll(
            scroll_id=scroll_id,
            scroll='2m'  # Keep the search context alive for 2 minutes
        )

    return results

# Function to write records to a CSV file
def write_records_to_csv(records, output_file):
    # Extract the _source field from each record
    records_source = [record['_source'] for record in records]
    flattened_records = pd.json_normalize(records_source)

    # Write the flattened records to a CSV file
    flattened_records.to_csv(output_file, index=False)

# Main function
def extracttocsv(host, port, username, password, index_name, output_file, start_time, end_time):
    host = host
    port = port
    username = username
    password = password
    index_name = index_name
    output_file = output_file
    start_time = start_time
    end_time = end_time

    # Connect to OpenSearch
    client = connect_to_opensearch(host, port, username, password)

    records = retrieve_high_status_code_records(client, index_name, start_time, end_time)

    # Write the records to a CSV file
    write_records_to_csv(records, output_file)