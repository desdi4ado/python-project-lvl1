#!c:\users\іван\desktop\hexlet\002-python\project_1\python-project-lvl1\.venv\scripts\python.exe -x
# EASY-INSTALL-ENTRY-SCRIPT: 'desdi4ado-brain-games','console_scripts','brain-games'
__requires__ = 'desdi4ado-brain-games'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('desdi4ado-brain-games', 'console_scripts', 'brain-games')()
    )
