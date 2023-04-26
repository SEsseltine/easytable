# EasyTable

### Installation
#### Manual Download

Download the `easytable.py` file from this git repository.  Place the downloaded file in the same directory as the file you are working with.  Continue with [getting started.](#getting-started)

### Usage
#### Getting Started ####
##### Creating a table
```python
from easytable import EasyTable
# Instantiate a new table object with data
table = EasyTable.from_from_data(data)

# Instantiate a new table object with a header and optional data
table = EasyTable.from_from_data(data)

# Add a bunch of data to the table
table.add_all(data)
```
