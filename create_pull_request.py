import os
import subprocess

# Set your remote repository name (e.g., 'origin')
remote_repo = "origin"
# Set your base branch name (e.g., 'main' or 'master')
base_branch = "master"
# Prompt for the feature branch name
feature_branch = input("Please enter the feature branch name (e.g., feature/123456-changeajob): ")
# Prompt for the commit message
commit_message = input("Please enter the commit message (e.g., Short Description of Change): ")
# Checkout the base branch
subprocess.run(["git", "checkout", base_branch])
# Pull the latest changes from the remote repository
subprocess.run(["git", "pull", remote_repo, base_branch])
# Pause for user input
input("Press Enter after you've made your changes to continue with creating the pull request...")
# Create and checkout the feature branch
subprocess.run(["git", "checkout", "-b", feature_branch])
# Stage all the changes
subprocess.run(["git", "add", "."])
# Commit the changes with the provided commit message
subprocess.run(["git", "commit", "-m", commit_message])
# Push the feature branch to the remote repository
subprocess.run(["git", "push", remote_repo, feature_branch])
# Create the pull request using the GitHub CLI (install it if not already present)
subprocess.run(["gh", "pr", "create", "--title", f"Pull request for {feature_branch}", "--body", f"This is a pull request for the changes in {feature_branch}.", "--base", base_branch, "--head", feature_branch])

print("Pull request created successfully.")
