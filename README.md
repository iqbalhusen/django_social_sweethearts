## Getting Started

These instructions are for running the application in a UNIX based computer.

### Prerequisites

It is assumed that you already have the following packages

- python 3.6.5+

### Configuration

1. Pull the GitHub repository

```bash
$ git clone https://github.com/iqbalhusen/django_social_sweethearts.git
```

2. `cd` to directory `django_social_sweethearts`.

```bash
$ cd django_social_sweethearts
```

3. Create a virtual environment with Python 3.6.5+ as base interpreter and activate it.

4. Install dependencies

```bash
$ pip install -r requirements.txt
```

5. Migrate Database (Default SQLite, to change database engine check `settings.py`)

```bash
$ ./manage.py migrate
```

6. Create a superuser to log in to Django admin

```bash
$ ./manage.py createsuperuser
```

7. Run the development server

```bash
$ ./manage.py runserver localhost:8000
```

> **Note:** Specify localhost instead of 127.0.0.1 as Facebook doesn't allow this IP address to use use Login via Facebook feature.

8. Log into Django Admin at `http://localhost:8000/admin/` with the credentials created at step 6.

9. Go to `SOCIAL ACCOUNTS > Social applications`

10. Add a social application with the following information

    > **Note:**
    >
    > - This app was created by me from my personal account. You may provide different facebook app information.
    > - As this app is in development mode, I am not sure if other Facebook users can use this Facebook Connect feature untill making this app live. I could log in from the same account using which this app was created.

    | Provider        | Facebook                                                     |
| --------------- | ------------------------------------------------------------ |
    | **Name**        | Social Sweethearts Test                                      |
    | **Client ID**   | 323173681689912                                              |
    | **Secret Key**  | 3d6f772d8a873e1bf3779cc0c6c40181                             |
    | **Chosen Site** | example.com  # The site domain may need to be updated for certain features to work properly |



## Using the Application

- Go to the homepage `http://localhost:8000`
- Click on the link `Please Connect through Facebook`.
- You should see your name, your profile picture and a Logout link if login was successful.
- To see the connected user information like Facebook ID, name etc, check in model `allauth.socialaccount.models.SocialAccount` which can also be accessed via Django admin.
- The long living access token is stored in `allauth.socialaccount.models.SocialToken` which can also be accessed via Django admin.



## Built With

- Python
- Django
- django-allauth



## Author

- **Iqbal Hussain**