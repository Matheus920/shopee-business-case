# shopee-business-case
A repository for the Shopee's Junior FullStack Developer position Business Case test.

# Description
This script aims to solve the Shopee's Junior Fullstack Developer Business Case test, 
provided by yulia.allar@shopee.com. Basically, it's a CLI tool responsible by add
sales for different sellers. Once a sale is added, it is stored in a JSON file and a 
report csv is also stored, containing which seller had the best sale performance so far.
As the output of the script, there is a JSON showing each sale stored in the application,
sorted by the seller name which sold the most amount so far.

# How to run it?
The instructions are pretty straightforward, you just have to run the following commands:

``pip install -r requirements.txt``

(The creation of a virtual environment is recommended, although not mandatory.)

``python case.py -h``

This command will give you all the information you need to run the script, which parameters are accepted
by the script and how to input them in a correct way.

ATTENTION: In this script, validation was implemented. So, if you pass an incorrect argument for any
of the options, a validation error will show in your terminal, so please be aware.

# Dependencies

This code was written in Python3.7 and all third-party modules used are contained in the
requirements.txt file. There is also a pre-commit hook pre-configured to be used with the module
pre-commit, which is absolutely not mandatory to run the code, but was used during the development.
To use it, after run the initial pip command you have to execute the following:

``pre-commit install``

``pre-commit run --all-files``