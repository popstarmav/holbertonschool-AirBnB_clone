# AirBnB Clone - The Console

## Project Description

The AirBnB Clone project is a Python-based implementation of a simplified version of the AirBnB website. This project aims to provide a command-line interface (CLI) that allows users to interact with various components of the AirBnB application, such as creating, updating, and managing listings, users, reviews, and more.

The core component of this project is the command interpreter, which facilitates communication between users and the underlying data models. Users can issue commands to create, update, delete, and query data using a variety of commands in the console.

## Command Interpreter

The command interpreter, often referred to as the "console," is the user interface for interacting with the AirBnB data models. It allows users to perform various operations on the data, such as creating new instances, updating existing ones, querying for information, and more.

### How to Start the Console

To start the console, follow these steps:

1. Clone the AirBnB Clone repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the root directory of the project.
4. Run the following command:

   ```shell
   run ./console.py

### How to Use the Console

Once the console is running, you can issue various commands to interact with the AirBnB data models. The available commands include:

* create: Create a new instance of a data model and save it to the storage file.
* show: Display information about a specific instance based on its class name and ID.
* destroy: Delete an instance based on its class name and ID.
* all: Display all instances or instances of a specific class.
* update: Update an instance based on its class name, ID, and attribute name and value.
* count: Count the number of instances of a specific class.
Examples
Here are some example commands and their usage:

To create a new instance:

   ```shell
    create BaseModel

To show information about an instance:

   ```shell
   show BaseModel 1234-1234-1234

To destroy (delete) an instance:

    ```shell
    destroy BaseModel 1234-1234-1234

To list all instances:

     ```shell
      all
To list instances of a specific class:

     ```shell
     all BaseModel

To update an instance:

     ```shell
     update BaseModel 1234-1234-1234 name "New Name"

To count instances of a specific class:

     ```shell
     count BaseModel

Contributors
CHARLES JOHNSON
