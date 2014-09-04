from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm

def prepare_deploy():
    local("git add --all && git commit")
    local("git push")

def deploy():
    prepare_deploy()
    code_dir = '/home/almarinho/almarinho'
    with cd(code_dir):
        run('su - almarinho -c "git pull"')
        run("supervisorctl restart almarinho")