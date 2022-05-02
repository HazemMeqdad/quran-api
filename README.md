# quran-api

allahuma saliy ealaa sayidina muhamad, the quri-api is a python web application that provides a simple and easy way to access the quran api.

## Features

* simple and easy to use and easy to understand
* you can find all the quran surahs and verses
* you can find & add your favorite reciters and listen to their recitations
* you can find azkar with categories
* you can find the quran translation

## Configuration

First make directory as name `instance` in your project directory.

Then create a file named `config.py` in the `instance` directory.

```python
# config.py
SECRET_KEY = "any string to secret your app"
ALLOW_HOSTS = ["*"]
```

## Installation

First, you need to clone porject from github.
```bash
git clone https://github.com/DwcTeam/quran-api.git
```
    
Then, you need to install all the dependencies.
```bash
pip install -r requirements.txt  # Windows
pip3 install -r requirements.txt  # Linux / MacOS
```

Then, you need to run the server.
```bash
python app.py  # Windows
python3 app.py  # Linux / MacOS 
```

* Optional: you can install the server with `pip install gunicorn` & run it with `gunicorn app:app -b="host:port"` replace `host:port` with your host and port or run `gunicorn app:app`.

After that, you need to install a cdn files to your server. from this link: [soon]()


## Routes
* `/` - States the root of the application & is allow host.
* `/moshaf/{page_number}.png` - Get the page image of the moshaf.
* `/reciters/{reciter_name}/{surah_number}.mp3` - Get the recitation of the surah.


## Copyright

All copyright belongs to the [HazemMeqdad](https://hazemmeqdad.me) and [DwcTeam](https://fdrbot.com).
