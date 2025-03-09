# AIpedia
Create Wikipedia with AI, quickly!

## Description
This is a Python web app that allows you to host an AI version of Wikipedia.

It supports Gemini 2.0 Flash models for content generation and gives you quick wikis on any topic.

## How to setup
### Get the Gemini API key
Create a `.env` file and add your Gemini API key:
```sh
touch .env
echo "GEMINI_API_KEY=[your Gemini API key here]" >> .env
```
If you don't have one, you can create a free API key [here](https://aistudio.google.com/apikey).

### Get your SSL certificates
Create an SSL certificate for your domain at [Let's Encrypt](https://letsencrypt.org/).
Run the following commands to issue and set up certificates quickly:
```sh
# Ubuntu/Debian
sudo apt update
sudo apt install certbot
certbot certonly -d [your domain name]
mkdir certs
cp /etc/letsencrypt/live/[your domain name]/* certs

# Arch Linux
sudo pacman -Syu
sudo pacman -S certbot
certbot certonly -d [your domain name]
mkdir certs
cp /etc/letsencrypt/live/[your domain name]/* certs
```

### Run the app
You can set up this project either directly, or via Docker.
  
  **Directly**
  
  Please run the following commands to set up AIpedia:
  ```sh
  python -m venv .venv
  source .venv/bin/activate
  pip install -U -r requirements.txt
  python main.py
  ```

  **With Docker**

  Please run the following commands to set up AIpedia on your Docker container:
  ```sh
  sudo docker build -t aipedia .
  sudo docker run -d -p 443:443 aipedia
  ```

  Make sure your system has a working copy of [Docker](https://docker.com/).

Now you have a working AI Wikipedia, ready for use at any time. Have fun learning new information!
