# gemchat

Toy for chatting with Gemini model over telnet.

# Installation

Install pipenv if not already present:

```sh
$ pip install --user pipenv
```

Then install the project dependencies:

```sh
$ pipenv install
```

# Environment Variables

- `GEMINI_API_KEY`: Key for communicating with Gemini API. [More info](https://ai.google.dev/gemini-api/docs/api-key).
- `PORT`: The port to bind the telnet server to. Defaults to `6023`.

# Usage

To invoke the server, simply run:

```sh
$ ./gemchat
```
