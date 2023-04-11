import os
import subprocess

remote_repo = "origin"

base_branch = "master"

feature_branch = input("Please enter the feature branch name (e.g., feature/123456-changeajob): ")

commit_message = input("Please enter the commit message (e.g., Short Description of Change): ")

subprocess.run(["git", "checkout", base_branch])

subprocess.run(["git", "pull", remote_repo, base_branch])
# Pause for user input
input("Press Enter after you've made your changes to continue with creating the pull request...")

subprocess.run(["git", "checkout", "-b", feature_branch])

subprocess.run(["git", "add", "."])

subprocess.run(["git", "commit", "-m", commit_message])

subprocess.run(["git", "push", remote_repo, feature_branch])

subprocess.run(["gh", "pr", "create", "--title", f"Pull request for {feature_branch}", "--body", f"This is a pull request for the changes in {feature_branch}.", "--base", base_branch, "--head", feature_branch])

print("Pull request created successfully.")
