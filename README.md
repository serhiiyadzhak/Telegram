# Telegram Bot for News Aggregation

This Telegram bot aggregates news from various RSS feeds and sends them to a designated Telegram channel. It summarizes the news articles and translates them into Ukrainian before sending them.

## Introduction

This project aims to provide users with a convenient way to stay updated on the latest news without having to browse multiple news websites. The bot fetches news articles from predefined RSS feeds, summarizes them using natural language processing (NLP) techniques, and delivers them to a Telegram channel.

## Features

- Fetches news articles from multiple RSS feeds.
- Summarizes news articles using the transformers library.
- Translates news summaries into Ukrainian using Google Translate.
- Sends summarized news to a Telegram channel.
- Supports multimedia content such as videos and images in news articles.

## Requirements

To run this project, you need to have Python 3.7 or higher installed on your system. You also need to install the required Python packages listed in the `requirements.txt` file.

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Set up the Telegram bot by obtaining a bot token from the BotFather and specifying it in the `TELEGRAM_TOKEN` variable in the `config.py` file.
4. Configure the MongoDB connection string in the `config.py` file if you want to store news links in a database.
5. Run the `main.py` file to start the Telegram bot.

## Usage

Once the bot is running, add it to your Telegram channel and configure it to receive updates from the bot. The bot will periodically fetch news articles from the configured RSS feeds, summarize them, and send them to the Telegram channel.

## Support

If you encounter any issues or have suggestions for improvements, please feel free to open an issue on the [GitHub repository](https://github.com/serhiiyadzhak/Telegram).

## Telegram Channel

You can follow our Telegram channel for the latest news updates: [NewsHubDaily](https://t.me/+JucpNKucww82MmJi)
