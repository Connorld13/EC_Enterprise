
# InMemoryDB

InMemoryDB is a simple in-memory key-value database implemented in Python, designed to demonstrate basic transactional operations such as beginning, committing, and rolling back transactions to ensure data consistency and isolation.

## Features

- **In-memory storage**: Provides fast access to data stored temporarily in memory.
- **Transactional Control**: Supports beginning, committing, and rolling back transactions to maintain data consistency.
- **Isolation**: Ensures that changes made during a transaction are not visible until the transaction is committed.

## Installation

This project is written in Python and does not require any external libraries beyond the Python standard library. Make sure you have Python 3.6 or higher installed on your system.

### Setup

Clone this repository to your local machine using:

```bash
git clone https://github.com/yourusername/inmemorydb.git
cd inmemorydb
```

No further installation of packages is required, as the project uses only the Python standard library.

## Usage

To use the InMemoryDB class within your own Python projects, include the `inmemorydb.py` file in your project directory. Here's a quick example of using the database:

```python
from inmemorydb import InMemoryDB

db = InMemoryDB()
db.begin_transaction()
db.put("key1", 100)
print(db.get("key1"))  # Outputs None, as the transaction is not yet committed
db.commit()
print(db.get("key1"))  # Outputs 100, after the transaction has been committed
```

## Running the Tests

Navigate to the project directory and execute the following command to run the unit tests:

```bash
python -m unittest discover -s tests
```

Ensure all test files are placed in a `tests` directory and named appropriately to be discovered by the unittest framework.

## Future Assignment Modifications

To elevate this project into an "official" assignment, consider the following enhancements:
1. **Expand the data types supported**: Currently, the database only supports integer values. Extending support to strings, lists, and other data types would provide a more robust experience.
2. **Include persistence capabilities**: Adding the ability to write to disk would simulate a more realistic database environment.
3. **Enhance transaction features**: Implement features such as transaction logs, support for nested transactions, and concurrency control mechanisms.
4. **Detailed grading rubric**: Develop a detailed rubric that assesses code quality, correct implementation of transactional features, and the inclusion of additional features like logging and persistence.

These improvements will provide students with a more comprehensive understanding of database management systems and prepare them for real-world applications.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request with your enhancements. For significant changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the [MIT License](LICENSE).
