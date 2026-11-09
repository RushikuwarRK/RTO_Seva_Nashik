# RTO Seva Nashik — Flask + MySQL Production Starter

## Features
- Flask application factory
- MySQL via SQLAlchemy/PyMySQL
- CSRF protection
- Admin authentication with hashed passwords
- Persistent appointment bookings with unique tracking IDs
- Public tracking API
- Persistent enquiries
- Admin dashboard for booking/enquiry status updates
- Downloadable document PDFs
- Responsive reference-based frontend
- Gunicorn deployment entry point

## Windows setup
1. Install MySQL Server and create the DB/user by running `schema.sql` in MySQL Workbench.
2. Create venv: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and change SECRET_KEY, DB password, admin email/password.
6. Create tables: `flask --app app init-db`
7. Create admin: `flask --app app create-admin`
8. Run: `flask --app app run --debug`
9. Website: http://127.0.0.1:5000/
10. Admin: http://127.0.0.1:5000/admin/login

## Production
Set environment variables on your host. Do not commit `.env`. Use a managed MySQL database and run `gunicorn app:app`. Enable HTTPS at the hosting/proxy layer.

## Important
The fee values are illustrative and must be checked against current official government/RTO fees before public launch. Add your privacy policy/terms and verify all business contact/address details.
