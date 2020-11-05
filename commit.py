from git import Repo,remote

rw_dir = '/home/mrhackit/Desktop/msf_venom'
COMMIT_MESSAGE = 'comment from python script'
repo = Repo(rw_dir)


def git_push():
	try:
		repo.git.add(update=True)
		repo.index.commit(COMMIT_MESSAGE)
		origin = repo.remote(name='origin')
		origin.push()
	except:
		print('Blah Blah ')


git_push()





