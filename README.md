# Step 1 Clone the project
```shell
git clone https://github.com/mdtahmidhossain/news_api.git
```


# Step 2 activate virtualenv
```
virtualenv venv && source venv/bin/activate
```

# Step 3 Install all requirements
```shell
pip install -r requirements.txt
```

# Step 4 Make migrate
```shell
python3 manage.py makemigrations && python3 manage.py migrate
```
This project populate the database when you visit the **News Listing** page. So we dont have to do anything.

# Step 5 Setup apiKey and api Url
Create a **.env** file in the root directory
```shell
nano .env
```
add following in items in the .env file. Replace the **thekey**(NEWS_API_KEY's value) with the actual key.
```text
NEWS_API_KEY=thekey
NEWS_API_URL=https://newsapi.org/v2/everything
```
And save the file.

# Step 6 run the server
```shell
python3 manage.py runserver
```

# This Project has 3 pages.
1) Home => http://localhost:8000/web/home
2) News Listing(Pagination on the bottom) => http://localhost:8000/web/news_listing
3) Json Listing => http://localhost:8000/web/json_listing

