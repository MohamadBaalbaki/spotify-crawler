# SpotifyCrawler

## Bored of waiting till Friday to check out your favorite artists' new releases on Spotify? If you answered yes, then my Heroku based cloud Spotify crawler & bot should become your best friend. Schedule it to run everyday at a certain time and receive daily updates of the newest Spotify releases of all of your favorite artists. It also retrieves compilations that are not shown on Release Radar!

*Full Documentation:*

1-Create a [Spotify Developer Account](https://developer.spotify.com/dashboard/login) and set your Spotify profile URL as the Redirect URI, all while keeping track of it

2-Create an App and keep track of your **client_id** and **client_secret**

3-Create a [SendGrid Account](https://signup.sendgrid.com/)
This account will be used to authenticate the Email API

4-Generate an API Key and keep track of it as it will disappear

5-Create a Sender in the Single Sender Verification section with the **From Email Address** and **Reply To** fields being the email you want to use as your sender (these 2 fields should be identical)

6-Verify this sender by following the link sent to your email

7-Disable **Open Tracking** and **Click Tracking** in the Tracking Settings section

8-Create an Account on [Heroku](https://www.heroku.com/)

9-Create an App on Heroku and name it: spotify-crawler

10-Fork my [repository](https://github.com/MohamadBaalbaki/spotify-crawler) on GitHub

11-Clone it on your computer

12-Delete the **.git** folder from your local repository as we will now link this repo to Heroku's remote repo

13-Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

14-Run the following commands in succession in your terminal:

```
heroku login

cd spotify-crawler

heroku git:remote -a spotify-crawler
```

15-Install [Spotipy](https://spotipy.readthedocs.io/en/2.12.0/), [DateTime](https://docs.python.org/2/library/datetime.html) and [SendGrid](https://pypi.org/project/sendgrid/) via pip

16-Run the following commands in succession in your terminal, all while replacing "xxxx_api_key_xxxx" by the API key you kept track of in step **4**

```
heroku config:set SENDGRID_API_KEY=xxxx_api_key_xxxx

heroku config
```

17-Maximize [Heroku's boot timeout](https://tools.heroku.support/limits/boot_timeout)

18-Open the file `spotify-artistcrawler.py` and click **CTRL+F** and write: INSERT
Replace all of the values in the code by the tracked credentials in the previous steps and save the file

19-Install Python using `sudo apt install python3.8`

20-Open the terminal and run the file while saving its stream to artists.txt:
`python spotify-artistcrawler.py > artists.txt`

21-Open the file `spotify-albumcrawler.py` and click **CTRL+F** and write: INSERT
Replace all of the values in the code by the tracked credentials in the previous steps and save the file

22-Run the file once locally using: `python spotify-albumcrawler.py`. You will be prompted to confirm that you agree to Spotify's terms and you will be redirected to a URL once you do so. Copy this URL to the input prompt and click enter. Once the code finishes to run, you will receive an email with all of the current releases of the day for all of your followed Spotify artists. *P.S:* a **.cache** file will be generated to further prevent an authentication input prompt on the server side, and fetch its response from the cached file instead

23-Scale Web Dynos to 0 using the following command: `heroku ps:scale web=0` since the scheduler on Heroku already utilizes a Dyno. If you don't scale Web Dynos to 0, you risk having your code randomly running every now and a then, thus receiving dozens of emails per day

23-Run the following commands in succession in your terminal:
```
git add .

git commit -m "Initial commit"

git push heroku master
```

24-Once the code finishes running, install the [Heroku Scheduler](https://dashboard.heroku.com/apps/spotify-crawler) add-on in your app and configure it to run `python spotify-albumcrawler.py` anytime you want

*#DONE*

**Mohamad Baalbaki**
[https://www.mohamadbaalbaki.com/](https://www.mohamadbaalbaki.com/)
