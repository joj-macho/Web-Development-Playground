# Password Generator

## Description

The Password Generator is a Flask-based web application that allows users to generate random passwords based on their preferences. Users can specify the password length and choose whether to include symbols, digits, and uppercase letters in the generated password.

This application serves as a web-based counterpart to the [CLI password generator](https://github.com/joj-macho/Pythological-Playground/tree/main/password-generator) program. The CLI version is a simple program that enables users to generate passwords, save them to a JSON file, and search for passwords by website.

## How it Works

- The Flask web application provides a user-friendly interface where users can input their preferences for password generation. It includes checkboxes for including symbols, digits, and uppercase letters.

- **Password Generation**: When users submit the form, the server-side code processes the input, generates a random password based on the specified preferences, and displays the result on the same page.

- **Error Handling**: Errors, such as invalid input or missing preferences, are handled using Flask's `flash` mechanism.

The Flask Password Generator web application is an alternative to the CLI version. Both versions share the same password generation logic, but the Flask implementation adds a user interface for ease of use.

### How to Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your web browser to access the Password Generator.

The output of the program will look like this:

![Password Output](output/password-output.gif)