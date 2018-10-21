# Doxie to Dropbox

This service script automatically retrieves scans on your Doxie Go or Doxie Q, and uploads them through the Dropbox API to a specific folder

Feel free to add bugs or feature suggestions in the "issues" section.

To run:

0) Ensure you have virtualenv and pip installed

1) Clone this repository

3) Rename example.env to .env and update the DOXIE_USERNAME, DOXIE_PASSWORD and DOXIE_FOLDER, DROPBOX_ACCESS_TOKEN

4) Create a virtual environment and install requirements with pip
	
	virtualenv venv
    source venv/bin/activate
    curl https://bootstrap.pypa.io/get-pip.py | python
    pip install -r requirements.txt

5) Run "python main.py" 


To install as a background script:

	pip install doxietodropbox
	cp (todo)/example.env ~/dropboxtodoxie.conf
	vi ~/dropboxtodoxie.conf
	cp (todo)/example.service doxietodropbox.conf
	sudo initctl reload-configuration
	sudo start doxietodropbox
