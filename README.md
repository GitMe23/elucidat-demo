# elucidat-demo
Example Python-behave test automation framework

## Setup checklist

### Change directory or clone the repository
```bash
cd python-behave-test-demo
```
Or
```bash
git clone https://github.com/GitMe23/elucidat-demo.git
```

### Python 3
Check that Python 3 is installed... 
```bash
python3 --version
```

Downloads can be found at https://www.python.org/downloads/

### Install requirements
After installing the repo and Python 3, the required dependencies need to be installed within the project folder by running:
```bash
python3 -m pip install -r requirements.txt
```
### Running the tests:
Inside the repository, run the test script:
```bash
sh run_tests.sh
```

### Test report
###### -- OPTIONAL
If you have Node Package Manager (npm) installed, install 'Allure' to generate web app based reports.sh run  

Inside the repository folder:
```bash
npm install -g allure-commandline
```
then
```bash
python3 -m pip install allure-behave
```
You can run the test script with Allure reporting:
```bash
sh run_with_allure.sh
```
See the report as a single index.html file at:
```bash
{path to repo}/allure-reports/index.html
```

