# OpenSearch quality of life tools

This is just a group of tools that I've started writing just to make every day life easier with OpenSearch.
It includes things like extracting data to csv, moving indexes up and down between storage tiers, etc.
A much more detailed README.md file will come up as soon as this tool has more stuff in it. For now there's only one useful function

# Extract to CSV

This command launches a query on the specified index, fetching all documents and writing them into a CSV file.
This can be extremely memory intensive if the dataset is large, so use with caution.

This command assumes that the time field for all documents is "@timestamp".

 ### Usage:
```
ostool extracttocsv --host HOST --port PORT --username USERNAME --password PASSWORD --indexname INDEXNAME --outputfile OUTPUTFILE --starttime STARTTIME --endtime ENDTIME
```

### Example:
```
ostool extracttocsv --host localhost --port 9200 --username admin --password $LHOSP --indexname test-index --outputfile test.csv --starttime "2024-12-12T13:00:00.000Z" --endtime "2024-12-14T13:00:59.999Z"
```

 - Host: Hostname or IP of the OpenSearch cluster you're connecting to
 - Port: Service port of the cluster (typically: 443 or 9200)
 - Username: Local user in the cluster that will be used for the connection
 - Password: The password for said user
 - Index name: Name of the index to be queried
 - Output file: Name of the CSV file to be written
 - Start time: Start time of the period to be fetched. It needs to be in the format of: "2024-12-12T13:00:59.999Z"
 - End time: End time of the period to be fetched. Same as above.


## License