# EasyTable

### Installation
There are two options for installing EasyTable:

#### 1. Command Line: ####

Coming soon.

#### 2. Manual Download: ####

Download the `easytable.py` file from this git repository.  Place the downloaded file in the same directory as the file you are working with.  Continue with [getting started.](#getting-started)

### Usage
#### Getting Started: ####
Remember to import the library!
```python
# Remember to import the library!
import easytable
```

**Creating a table:**
This will create a new table object called `table_name` using the value from `header_value` (which is of type list or a tuple) as the header row for the table.
```python
# Instantiate a new table object
table_name = easytable.EasyTable( header_value )
```
