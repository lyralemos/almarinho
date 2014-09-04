from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm

def prepare_deploy():
    local("git add -p && git commit")
    local("git push")

def deploy():
    code_dir = '/home/almarinho/almarinho'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")