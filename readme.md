# Getting started
* Clone this repository to a folder on your machine
* Get yourself an account at OpenAI.  See [Open AI Beta](https://beta.openai.com/overview)
* Create an API key on the [api keys page](https://beta.openai.com/account/api-keys).  Click on the "Create Secret Key" button and copy the key it creates.
* Create a new file names ".env" in the folder where the code was cloned. Add the following content replaing YOURKEY with the secret API key you copied above.  Save the file.

``OPENAI_API_KEY=YOURKEY``

* Install Python (version 3.10.7 or higher) from https://www.python.org/. You will need to know the path to the Python you installed or you can add it to your path variable. If you do not know how to do this, try a google search on "path to Python"
* Open a terminal window (or command prompt on Windows) and change your current directory to the location of the source code you cloned
* Type the following command to add the Python libraries needed to run the program to your machine.

``pip install -r requirements.txt``

* Type the following command and press "Enter".  If it fails to run and produce output or shows an error message, contact the author for help.  Make sure to replace "Path to Python on your machine" with the actual path.

``Path to Python ion your machine/python.exe ./app.py "summarize this" -o ./sample.txt``

* You can specify any input file instead of "./sample.txt"
* There are many other parameters you can play with.  Use the -h switch to see the options.

``Path to Python/python.exe ./app.py -h``



