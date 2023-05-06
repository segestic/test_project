import os
import git

def commit_repo(commit_msg):
    # Get the current working directory
    cwd = os.getcwd()

    # Open the repository
    repo = git.Repo(cwd)

    # Add any changes to the index
    repo.index.add("*")
	
    # Commit the changes with a custom message
    repo.index.commit(commit_msg)

    # Push the changes to the remote repository
    origin = repo.remote(name="origin")

    # Set up authentication credentials
    origin_url = origin.url
    username = "segestic"
    password = "123456_your_token"

    # Push changes with authentication
    origin = repo.remote(name="origin") 
    
    #new_origin_url = origin_url.replace('https://', f'https://{username}:{password}@')
    new_origin_url = f'https://{username}:{password}@github.com/segestic/test_project.git'
    origin.set_url(new_origin_url)
    origin.push()
