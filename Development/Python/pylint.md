# run pylint on whole project
pylint my_project

# run pylint on all modules in a directory
py -m pylint *.py

# disable checking issue. Just add a comment above class or method definition:
# pylint: disable=R0903
class PylintDemo():
...

# install
py install pylint

# run on a module
py -m pylint .\calculator.py

# create a configuration file
pylint --generate-rcfile > .pylintrc

# ignore messages C0116: Missing function or method docstring (missing-function-docstring)
Find the section that says [MESSAGES CONTROL]. In this section, there will be a line that starts with disable=. If it's not there, you can add it.
Add C0116 to the list of codes on the disable= line. Separate each code with a comma. Here is an example of what the line could look like:

disable=C0116,another-code-to-disable,third-code-to-disable
