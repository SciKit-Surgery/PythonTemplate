base_dir=$(pwd)

python -m unittest discover -s "tests" -p "*.py"

mkdir -p build
cookiecutter --output-dir build --no-input --overwrite-if-exists .

cd build/MyNewProject/doc
make html

cd $base_dir/build/MyNewProject
./run_tests.sh