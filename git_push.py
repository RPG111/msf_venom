from git import Repo

PATH_OF_GIT_REPO = r'https://github.com/MrHackIT/msf_venom.git'
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='master')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()