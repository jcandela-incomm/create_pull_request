## Setting up and using the Python script for creating a pull request

#### Prerequisites
- Python installed on your system (version 3.6 or later). Download and install from https://www.python.org/downloads/
- Git installed on your system. Download and install from https://git-scm.com/downloads
- GitHub CLI installed on your system. Download and install from https://cli.github.com/

#### Steps

1. Copy the Python script provided and save it as a file named create_pull_request.py in a convenient location on your system.
2. Open the create_pull_request.py file in a text editor and update the remote_repo and base_branch variables with the appropriate values for your project.
3. Open PowerShell
4. In the PowerShell window, navigate to the directory where your Git repository is located using the cd command. For example:
powershell


```
cd C:\path\to\repo
```

- Verify your system's PATH: Ensure that Python, Git, and GitHub CLI are in your system's PATH. To do this, run the following commands in PowerShell:
  - If any of the commands fail, please refer to the respective installation guides to make sure the tools are properly installed and added to your system's PATH.

```powershell
py --version
git --version
gh --version
```



5. Execute the script: To run the Python script from PowerShell, use the following command, replacing path\to\create_pull_request.py with the actual path to the script file:

```powershell

py path\to\create_pull_request.py
```

6. Enter the feature branch name: When prompted, enter the feature branch name (e.g., feature/123456-changeajob) and press Enter.

7. Enter the commit message: When prompted, enter a short description of the change as the commit message (e.g., "Short Description of Change") and press Enter.

8. Make your changes: After pulling the latest changes from the remote repository, the script will pause. Make the required changes to your repository files.

9. Continue the script: Once you have made your changes, return to the PowerShell window and press Enter to continue executing the script. The script will create the feature branch, commit your changes, push the feature branch to the remote repository, and create a pull request using the GitHub CLI.
10. Verify the pull request
