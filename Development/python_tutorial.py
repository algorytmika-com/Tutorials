#create virtual enviroment
py -m venv venv

# activate virtual enviroment
 .\venv\Scripts\activate

# Generate libraries from current projects virtual enviroment
py -m pip freeze > requirements.txt

If you want install python libs and their dependencies offline, finish following these steps on a machine with the same os, network connected, and python installed:

1) Create a requirements.txt file with similar content (Note - these are the libraries you wish to download):

Flask==0.12
requests>=2.7.0
scikit-learn==0.19.1
numpy==1.14.3
pandas==0.22.0
One option for creating the requirements file is to use 

pip freeze > requirements.txt

. This will list all libraries in your environment. Then you can go in to requirements.txt and remove un-needed ones.

2) Execute command mkdir wheelhouse && pip download -r requirements.txt -d wheelhouse to download libs and their dependencies to directory wheelhouse

3) Copy requirements.txt into wheelhouse directory

4) Archive wheelhouse into wheelhouse.tar.gz with tar -zcf wheelhouse.tar.gz wheelhouse

Then upload wheelhouse.tar.gz to your target machine:

1) Execute tar -zxf wheelhouse.tar.gz to extract the files

2) Execute pip install -r wheelhouse/requirements.txt --no-index --find-links wheelhouse to install the libs and their dependencies