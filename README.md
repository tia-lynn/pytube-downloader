# Introduction
This script is my personal pytube downloader specifically for personal use in tabletop games on various VTTs. Uses your Google account to authenticate and get an OAuth token in order to download the files from YouTube's API, then converts the downloaded file into .ogg format.

## Installation
Clone this repository into a project folder then pip install the requirements. For new people,

- Create a new GitHub account and sign in
- Download and install Python from the official website https://www.python.org/downloads/
- Download and install Visual Studio Code (VSC) from the official website https://code.visualstudio.com/download
- Create a new project folder, for example in `C:\Users\{Your Username}\dev`
- Open that new `dev` folder in VSC then hit ``ctrl + ` `` to open the TERMINAL console
- Inside that terminal window, you should see `C:\Users\{Your Username}\dev>`
    - If not, type `cd /d C:\Users\{Your Username}\dev` and press `Enter` to switch to that directory
- Type `git clone https://github.com/tia-lynn/pytube-downloader.git` and press `Enter` to create a copy of this repository into your new project folder
- Type `cd pytube-downloader` to switch to the new folder
- Type `python -m venv .venv` to create a new virtual environment
- Type `.venv\scripts\activate` to activate that new venv
- Type `pip install -r requirements.txt` to install the necessary packages for this script
- Run the script by using `python download-youtube-video.py` or by running it through VSC's interface. Make sure you switch to the venv you created if using the VSC interface (https://code.visualstudio.com/docs/python/environments)

When installing new repositories, it's important to check `requirements.txt` for any malicious libraries. Don't blindly install stuff you find online. However, in this case, you can totally trust me. 🙂

## Usage
Within the `urls` list, paste any YouTube URLs that you want to download, e.g.
```python
urls = [
    "https://youtu.be/K8JoYyGCGgQ",
    "https://youtu.be/3JZ_D3ELwOQ"
    ]
```

Then just run the script. The first time you run this, a window should open in your browser from Google asking you to sign in in order to use their OAuth API service. Just sign in and the script should continue normally. Again, this is usually kind've sketchy and I recommend not trusting random prompts for you to sign in if you don't know where it's coming from.

Once authenticated, the script will automatically create a `downloaded-audio` folder within the project folder to place the downloaded files, convert them to .ogg, then delete the old .mp3 it downloaded.