# Remove old versions
rm dist/*.*

# Build the distribution
python setup.py sdist bdist_wheel bdist_egg

# Push to github
echo "Enter commit comment: "
read comment
git add --all
git commit -m "$comment"
git push

twine upload dist/*
