import os
import git
from decouple import config, Csv

def commit_repo(commit_msg):
    # Get the current working directory
    cwd = os.getcwd()

    # Open the repository
    repo = git.Repo(cwd)

    #checkout to the main branch
    repo.git.checkout('main')
    
    # Add any changes to the index
    repo.index.add("*")
    #repo.git.add(update=True)
    #repo.index.add(['db.sqlite3'])
	
    # Commit the changes with a custom message
    repo.index.commit(commit_msg)

    # Push the changes to the remote repository main branch
    origin_main_branch = repo.remotes.origin.refs.main
    origin = repo.remote(name="origin")

    # Set up authentication credentials
    origin_url = origin.url
    username = config('GIT_USER')
    password = config('GIT_KEY')
    #print (f'username is {username}, password is {password}')

    # Push changes with authentication
    #origin = repo.remote(name="origin") 
    
    #new_origin_url = origin_url.replace('https://', f'https://{username}:{password}@')
    new_origin_url = f'https://{username}:{password}@github.com/{username}/test_project.git'
    origin.set_url(new_origin_url)
    #origin.pull()
    
    print (f'origin url is {new_origin_url}')
    origin.push().raise_if_error()
    


#commit_repo('testing-database-added')


#repo.index.add(['file1.txt', 'file2.txt'])
#commit_message = 'My commit message'
#repo.index.commit(commit_message)

# push changes to remote repository
#origin = repo.remote(name='origin')
#origin.push()




#import git

#def commit_repo(commit_msg):
#repo = git.Repo(os.getcwd())
#files = repo.git.diff(None, name_only=True)
#for f in files.split('\n'):
#    show_diff(f)
#    repo.git.add(f)

#repo.git.commit('test commit', author='sunilt@xxx.com')

#repo.git.commit('-m', 'test commit', author='sunilt@xxx.com')

