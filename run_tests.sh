tox

rm -rf build
mkdir -p build
cookiecutter --output-dir build --no-input --overwrite-if-exists .
cd build/MyNewProject
tox
