#!/bin/sh
git stash save
git checkout master
python maxs.py
python frisco.py 
python victoria.py
python alehouse.py
python klobys.py
python mahaffeys.py
jade index.jade
git add -u
git commit -m "Updated on $(date)"
git push origin master
git push production master
git checkout gh-pages
git merge master -m "merged on $(date)"
git push origin gh-pages
git checkout master
git stash apply