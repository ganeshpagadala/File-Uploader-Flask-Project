# File Manager Web Application

## Project Description

File Manager is a full-stack Flask web application that allows users to upload, view, download, and manage files securely. The application stores files in a MySQL database with unique file hashes to prevent duplicates, and provides a simple web interface for file management.

This project demonstrates practical skills in Flask development, database integration, file handling, and dynamic content rendering. It reflects intermediate to advanced full-stack proficiency suitable for real-world applications.

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MySQL
* **Frontend:** HTML, CSS, Jinja2 Templates
* **Tools:** Git, VS Code, Flask Debug Server, hashlib module for file hashing

## Features

* Upload files through a web interface with duplicate file detection
* View all uploaded files with metadata
* Download files securely
* Inline viewing of supported file types in the browser
* Delete files from the database
* Automatic file hash generation to ensure file uniqueness
* Modular code structure for easy extension

## Key Skills / Concepts Learned

* Flask routing, rendering templates, and request handling
* File uploads and downloads in Flask
* Database CRUD operations with MySQL
* Handling binary data and generating SHA-256 file hashes
* Dynamic content rendering using Jinja2
* Modular and maintainable project structure

## Project Structure

```
/File-Manager-App
│
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   ├── index.html        # File upload page
│   └── files.html        # File listing page
├── static/               # (Optional) CSS/JS/images
└── database/             # Database connection and utility functions
```

## How to Run

1. Clone the repository:

```bash
git clone <your-repo-link>
```

2. Install dependencies:

```bash
pip install flask mysql-connector-python
```

3. Ensure MySQL server is running and update database credentials in `app.py`
4. Run the Flask application:

```bash
python app.py
```

5. Open a browser and visit:

```
http://127.0.0.1:5000/
```

## Sample Data

No sample files are needed. Upload any file through the interface for testing.

## Future Enhancements

* Add user authentication and role-based access
* Add file search and filter functionality
* Add file versioning to track changes
* Enhance UI/UX using Bootstrap or Tailwind CSS
* Implement cloud storage integration for larger file handling

## Screenshots

*(Add screenshots of file upload page, file listing, and
