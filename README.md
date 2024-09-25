# Gemini

A simple command line app for interacting with google's gemini-1.5-flash AI
model. The chat bot is multimodal, allowing the user to enter standard text
prompts as well as uploading files.

## Getting Started

To run the application you will need to add your api key to a .env file in the
root of the project. The .env file should look like this:

```.env
API_KEY=your_api_key_here
```

### Dependencies

| Dependency          | Installation                                                    |
| ------------------- | --------------------------------------------------------------- |
| python 3.11         | [python](https://www.python.org/downloads/release/python-3110/) |
| pipenv              | [site](https://pipenv.pypa.io/en/latest/)                       |
| google-generativeai | [pypi](https://pypi.org/project/google-generativeai/)           |
| rich                | [pypi](https://pypi.org/project/rich/)                          |

With the above dependencies installed, you can clone the repository and install
the required packages with the following command from within the project
directory:

```bash
pipenv install
```

## Scripts

- `pipenv run app`: Runs the chat bot.
