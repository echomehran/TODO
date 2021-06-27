# TODO WEB APPLICATION

A simple task manager based on Python/Django

**How to run the google login part**

In order to add the google login feature, you need to follow the instructions below

1.  You’ll need to set up OAuth application via [Google Developers Console][1]
2.  Go to Dashboard, create a NEW PROJECT
3.  Name your new project, preferably your website or app name. User
    will be able to see this project name when we redirect them to
    Google login page.
4.  Click “CREATE” to proceed.
5.  Back to “Dashboard”, go to “Credentials” on left panel.
6.  Create credentials. On the dropdown, choose “OAuth Client ID”
    option.
7.  Make sure you fill out the “OAuth Consent Screen” form.
8.  You’ll only need to provide “Application name”, “Email” and click
    “SAVE”.
9.  Now, you can create your OAuth Client ID by filling out these
    details;
10. Authorized Javascript origins (http://127.0.0.1:8000)
11. Authorized redirect URL
    (http://127.0.0.1:8000/accounts/google/login/callback/)
12. Once you click “CREATE”, you will be able to obtain your “client
    ID” and “client Secret”.
13. You’ll need this information to proceed the next steps

**Django admin**

14. $ python manage.py createsuperuser

15. $ python manage.py runserver

16. On the SITES section, click “sites” and fill out the details and
    click “Save”

17. Domain name: 127.0.0.1:8000 Display name: 127.0.0.1:8000

**Add social applications**

18. Provider: Google Name: Google API Client id: (refer step 7, your
    OAuth details) Secret key: (refer step 7, your OAuth details)

**See the result**

You’re almost done! Now navigate to (http://127.0.0.1:8000/) to see the “Sign in with Google” page.

[1]: https://console.developers.google.com/
