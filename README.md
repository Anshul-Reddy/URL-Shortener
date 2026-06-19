#  URL Shortener

A simple and efficient URL Shortener built using **Python, Flask, SQLite, HTML, and CSS**.

This application allows users to convert long URLs into short, easy-to-share links while storing all generated URLs in a database.

---

## 🚀 Features

 Shorten long URLs

 Redirect short URLs to original URLs

 Duplicate URL prevention (same URL gets the same short code)

 URL History tracking

 Copy URL functionality

 SQLite database integration

 Clean and modern dark-themed UI

---

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS

## 🧠 How It Works

1. User enters a long URL.
2. Flask checks whether the URL already exists in the database.
3. If it exists, the existing short code is returned.
4. Otherwise, a new random short code is generated.
5. The URL is stored in SQLite.
6. Visiting the short URL redirects users to the original URL.

---

## 🎯 Future Improvements

- Click analytics
- QR code generation
- Custom short URLs
- User authentication
- Cloud database support
- Online deployment

---

## 👨‍💻 Author

**Anshul Reddy**

- GitHub: https://github.com/Anshul-Reddy
- LinkedIn: https://www.linkedin.com/in/k-anshul-reddy/
