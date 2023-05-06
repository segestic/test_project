import os
import git

def commit_repo(commit_msg):
    # Get the current working directory
    cwd = os.getcwd()
    print ('cwd is ', cwd)

    # Open the repository
    repo = git.Repo(cwd)
    print (repo)

    # Add any changes to the index
    repo.index.add("*")
	
    # Commit the changes with a custom message
    repo.index.commit(commit_msg)
#    repo.git.commit('-m', commit_msg) # , author='sunilt@xxx.com')

    # Push the changes to the remote repository
    origin = repo.remote(name="origin")

    # Set up authentication credentials
    origin_url = origin.url
    username = "segestic"
    password = "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"

    # Push changes with authentication
    origin = repo.remote(name="origin") 
    #origin.push(refspec="refs/heads/main", force=True, progress=True, auth=(username, password))
    #origin.push(refspec="main:main", force=True, progress=True, auth=(username, password))
    #origin.push(auth=(username, password))
#    origin.push()
    origin_url = origin.url
    print (origin_url)
    new_origin_url = origin_url.replace('https://', f'https://{username}:{password}@')
    origin.set_url(new_origin_url)
    origin.push()













commit_repo('testing')


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

