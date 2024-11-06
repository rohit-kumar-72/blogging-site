# Blogging Site

This is a simple Django-based blogging site where users can create, update, delete, and view blog posts. The site allows users to log in and manage their own posts. The project is designed to be easy to use and customizable, with user-friendly interfaces and essential blogging functionalities.

## Features

- **User Authentication**: Secure login and registration system.
- **Blog Management**: Create, update, and delete blog posts.
- **Image Upload**: Upload and display post thumbnails.
- **Real-time Display**: Updated post data is displayed instantly after any changes.
- **Responsive Design**: Works smoothly on both mobile and desktop devices.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rohit-kumar-72/blogging-site.git
   ```

2. Navigate to the project directory:

   ```bash
   cd blogging-site
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:

   ```bash
   python manage.py runserver
   ```

7. Access the site by navigating to `http://127.0.0.1:8000/` in your browser.

## Usage

- Navigate to `http://127.0.0.1:8000/` to view the blog homepage.
- Log in to create, edit, or delete your blog posts.
- Admin users can manage all posts via the Django admin panel.


## snapshots

1. Home page
   ![image](https://github.com/user-attachments/assets/0ee29763-9667-4254-ab40-648a466cdadb)
   
3. signup page
  ![image](https://github.com/user-attachments/assets/34f64dea-830f-4baa-9800-7b60e802f10e)

4. Login page
  ![image](https://github.com/user-attachments/assets/2a156278-344b-4885-a58a-f0505c02aacf)
