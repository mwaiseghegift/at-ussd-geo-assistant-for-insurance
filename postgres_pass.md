sudo apt install postgresql postgresql-contrib

sudo systemctl start postgresql.service

sudo -i -u postgres

psql

-- set password for postgres user

\password postgres
