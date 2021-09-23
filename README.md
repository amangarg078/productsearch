## Setup Instructions

 - Change directory using `cd producsearch`
 - Run `pip install -r requirements.txt` after activating a virtual environment.
 - In the `settings.py`, point `DATABASES` to a Postgres database. If you are using SQLite, set `IS_DB_POSTGRES = False`
 - Run `python manage.py migrate`
 - Add the `.jl` file to the root folder (where `manage.py` is located)
 - Run `python manage.py import_data` to start importing data. There are two optional variables
 -- `batch_size` - Defaults to `1000`
 -- `filepath` - Path for the `.jl`file
 Usage: `python manage.py import_data --batch_size=1000 --filepath="file.jl"`
 - Run server using `python manage.py runserver`
