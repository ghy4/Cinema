# Cinema Movie Ticket Booking System

A web application for cinema lovers to browse movies, buy tickets, and get a QR code sent to their email for easy entry!  
Built with Python Flask and PostgreSQL, this project offers an automated ticketing experience, a full movie database, and dynamic user discounts based on roles.

---

## Features

- **Movie Listing**: Browse upcoming and past movies.
- **Ticket Booking**: Purchase tickets for available movies.
- **Automated Email Delivery**: Upon purchase, users receive an email with a QR code containing ticket information.
- **QR Code Entry**: Scan your QR code at the cinema entrance for seamless check-in.
- **User Roles & Discounts**: Role-based models for users (e.g., student, regular, premium) provide automatic discounts.
- **Movie Database**: Keep track of all films, showtimes, and historical data.

---

## Technology Stack

- **Backend**: Python Flask
- **Database**: PostgreSQL
- **QR Code Generation**: Various Python libraries (e.g., qrcode)
- **Email Sending**: Integrated with a mail server and libraries for email delivery
- **User & Role Management**: Custom models for flexible discounts

---

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/ghy4/Cinema.git
    cd Cinema
    ```

2. **Set up a virtual environment (optional, but recommended)**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure environment variables**
    - Copy `.env.example` to `.env` and fill in your database and mail server details.
    - Example:
      ```
      DATABASE_URL=postgresql://user:password@localhost:5432/cinema
      MAIL_SERVER=smtp.yourmail.com
      MAIL_PORT=587
      MAIL_USERNAME=your_email@example.com
      MAIL_PASSWORD=your_password
      SECRET_KEY=your_secret_key
      ```

5. **Set up the database**
    - Ensure PostgreSQL is running and the database specified in your `.env` is created.
    - Run migrations or the provided scripts to initialize tables.

6. **Run the application**
    ```sh
    flask run
    ```
    The app will be available at `http://127.0.0.1:5000`

---

## Project Structure

```
Cinema/
├── src/                  
├── denv/                 
├── requirements.txt      
├── config.py                
└── ...
```

---

## Key Feature: QR-Code Ticketing

- After a successful ticket purchase, an email is sent to the user with a QR code.
- This QR code contains all necessary ticket information for entry.
- At the cinema entrance, scanning the code verifies and checks in the user.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

For questions or contributions, open an issue or contact [ghy4](https://github.com/ghy4).
