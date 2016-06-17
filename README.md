# pybot
Python library for Facebook Messenger bot API

## To install

`pip install -r requirements.txt`

## To run test suites

`nosetests tests`

## Before submitting

You should run `flake8 <PATH_TO_CODE>` to ensure changes conform to PEP8 standards

## To Submit a new build to pip

1. Add a new tag to repo 
	`git tag -a <TAG> -m "<MESSAGE>"`
2. Push the new tag
	`git push origin --tags`
3. Update the `setup.py` file 
	* Update version to latest tag
	* Update the download url for latest tag
4. Upload to pip
	`python setup.py sdist upload`