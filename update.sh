#!/bin/sh
git stash save
git checkout master
echo "Maxs" && python maxs.py
echo "Frisco" && python frisco.py 
echo "VGP" && python victoria.py
echo "Alehosue" && python alehouse.py
echo "Kloby" && python kloby.py
echo "Mahaffey" && python mahaffeys.py
echo "Arundel" && python arundel.py
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