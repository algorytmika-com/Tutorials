# when proble running pytest
py -m pip install pytest-cov

#pytest - set enviroment ot recogniize modules, put inside test file
# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
# add to contest.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '\\..\\src\\assignment06')

# run pytest at level above scr and tests
python -m pytest

# run pytest without warning concerning the report
python -m pytest --cov