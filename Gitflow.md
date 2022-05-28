# Gitflow

## set up your SSH
1.   In your Linux terminal

` ssh-keygen -o -t rsa -C "your email address for github"`

3.   Set a file name
4.   Set a passphrase (if you think there is a chance that you are going to forget your passphrase simply put no passphrase and enter blank) 
5.   `cd ~/.ssh `and `ls` into it and make sure that your key is generated
6.   copy the content of `your_ssh_key_file_name.pub`
7.   go to your github account and go to "settings" and then go to "SSH and GPG keys" make a new SSH key call it something that you want and paste the key that you just copied

## Set up the repo architecture

1. First make a public repo on your account (the link to your public repo is something that you need to share)
2. Clone your public repo into your local device using ssh address and probably you will be asked for your ssh key passphrase
3. Check your remote git using:

	`git remote -v`

	At this point, you should just have access to your own repo probably called origin with both fetch and push option. 
 
4. you might need to set config

   ```
   -git config --global user.email "your email address"
   -git config --global user.name "your Name"
   ```
   
5. add local branch for your development

    `git checkout -b LocalDev`
    
	you change anything here in this branch
	
	```
	git add .
	git commit -m "message-here"
	git checkout main
	git merge LocalDev
	git push origin main #Push to your own remote repo
	```
	
	 
7. Add Fourthbrain repo as extra remote repo:

	`git remote add FB git@github.com:FourthBrain/MLE-7.git`
	
8.	`git remote -v`

	At this point, you should have access to both your own repo and FourthBrain (called FB) and should see something like this:
	
	```
	FB    git@github.com:FourthBrain/MLE-7.git (fetch)
	FB    git@github.com:FourthBrain/MLE-7.git (push)
	origin git@github.com:rafatisina/TestRepo.git (fetch)
	origin git@github.com:rafatisina/TestRepo.git (push)
	```
	
9. `git fetch --all`

10. make new branch for FB material

	`git checkout --track -b FBranch FB/main`

	you should see something like this:

	`Branch 'FBranch' set up to track remote branch 'main' from 'FB'.`


11. you can visually check whether you are in that branch:

	`git log --all –-graph`
 
12. `git checkout main`
13. `git merge FBranch --allow-unrelated-histories`

	If there is any conflict you need to take care of it

14. `git add` 
15. `git commit -m "message-here"`
16. push to your own remote repo

	`git push origin main`
	
	
## From now on fter each release

```
Git fetch --all
Git checkout FBranch
git merge --ff-only @{u}
git add .
git commit -m "branch is updated"
git checkout main
git merge FBranch --allow-unrelated-histories
you will be asked to add a comment about why this change is necessary --> put a message
git push origin main
```	