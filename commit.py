from git import Repo,remote



rw_dir = 'C:\\Users\\IEUser\\Desktop\\msf_venom'
COMMIT_MESSAGE = input("please enter a commit msg :")




repo = Repo(rw_dir)

def git_push():
	try:
		repo.git.add('.')
		repo.index.commit(COMMIT_MESSAGE)
		origin = repo.remote(name='origin')
		origin.push()
	except:
		print('Blah Blah ')


git_push()