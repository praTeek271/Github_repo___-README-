# Django GitHub README Extractor

This Django web application allows you to extract and display README files from a GitHub user's account.

## Features

- Fetches repository data using the GitHub API
- Displays a list of repositories with links to view README files
- Renders README files as HTML with Markdown formatting

## Demo

Check out the live demo of the application: [https://github-repo-readme.onrender.com](https://github-repo-readme.onrender.com/)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/praTeek271/Github_repo___-README-.git
   cd Github_repo___-README-

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:

   ```bash
   python manage.py runserver
   ```

4. Access the application in your browser at `http://127.0.0.1:8000/github-username/`

## Usage

1. Enter a GitHub username in the URL to view the user's repositories and README files.
2. Click on "View README" to see the rendered README file content.

## Technologies Used

- Django
- GitHub API
- Markdown

## Screenshots

Include screenshots of your application in action here.

## Future Enhancements

- Add user authentication for accessing private repositories
- Improve UI/UX with additional styling
- ...

## Contributing

Contributions are welcome! Fork the repository and create a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
