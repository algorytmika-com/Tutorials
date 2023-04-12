# 
git config --global core.excludesfile ~/.gitignore_global

# clone github repository
git clone https://github.com/UWPCE-PY310-SP-2022/automated-interviewer-assignment-2-piotreks-uw-edu.git

# go back to a commit
# This will destroy any local modifications.
# Don't do it if you have uncommitted work you want to keep.
git reset --hard 0d1d7fc32

# rename branch
git branch -m "new_name"

# show commits with dates
git log --pretty="%ad%x09%h%x09%s"
# In case you were curious what the different options were:
# %h = abbreviated commit hash
# %x09 = tab (character for code 9)
# %an = author name
# %ad = author date (format respects --date= option)
# %s = subject

#create new branch after switching to a commit
git switch [<options>] (-c|-C) <new-branch> [<start-point>]

# git revert a directory only
git checkout <refspec> -- path/to/directory  # or path/to/file
#where <refspec> can, for instance, be HEAD, that is, the current working commit. Note that this usage of the checkout command will affect the working tree but not the index.
#git revert is used to "revert a commit", and by this, it should not be understood that the commit disappears from the tree (it would play havoc with history -- if you want that, look at git rebase -i). A reverted commit consists of applying, in reverse, all changes from the commit given as an argument to the tree and create a new commit with the changes (with a default commit message, which you can modify).

# check origin repositories
git remote -v

# change user name  email locally 
git config --local user.email "vector@test.com"

# change user user name locally 
git config --local user.name "Vector"

# get user name
git config user.name

# call alias
git graph

# git set alias
git config --global alias.graph "log --graph --oneline --all"

# show git log in one line
git log --graph --oneline --all

# show information connected with revision
git show

# initialize git
git intit