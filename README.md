# Spiceworks Ticket Viewer
Spiceworks ticket viewer

This app displays Spiceworks Helpdesk Tickets in a nicer format that allows printing only the relevant areas that I needed. The default ticket wasted to much paper and ink printing useless stuff. 

##Requirements

Python 3.4+

Flask

Flask-Paginate(*https://github.com/lixxu/flask-paginate*)

## Usage

Clone to the desired path. 

```pip install -r requirements.txt```

Edit Line 14 of *app.py* and set DATABASE= to be the path to your spiceworks database. If this app is run on the same system as spiceworks it may be something like ```c:\Program Files (x86)\Spiceworks\db\siceworks_prod.db```

Start the app by running ```python app.py```

Edit any of the queries in *sql_queries.py* to suit your requirements.

Alternatively use the included *wfastcgi.py* to host the website via IIS.

## Notes
This was developed using Python 3.4. It is untested on earlier versions.

This app uses only select queries, and does not write anything to the database, however I am not responsible for any corruption that may occur as a result of using this app.