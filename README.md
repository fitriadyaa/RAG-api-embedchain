
# Retrieval Augmented Generation Chatbot API with Embedchain

This project integrates the `embedchain` library to facilitate the creation of a Flask-based chatbot that leverages the OpenAI API to provide responses based on a predefined set of data.

![App Screenshot](https://github.com/fitriadyaa/RAG-api-embedchain/blob/main/Screenshot.png?raw=true)


## Features

- Chatbot integration using `embedchain` and Flask.
- OpenAI API for LLMs/Generating responses.
- Provide data in JSON file

## Installation

- Clone this repository
- Ensure you have Python 3.6 or higher installed
- Install the required Python packages:
  ```sh
  pip install Flask embedchain python-dotenv
    
## Run Project

```bash
  python app.py
```

## Usage
After starting the server, you can interact with the chatbot by sending POST requests to /chat with a JSON payload containing the query.

Example request:
```sh
{
  "query": "Berapa biaya kuliah informatika?"
}
```

## Support Me ☕

If you find MyGithubUser helpful or just want to support my work, you can buy me a coffee! ☕

<a href="https://www.buymeacoffee.com/fitriadyaa" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
