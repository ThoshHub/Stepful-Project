# Coaching Conundrum Application

## Setup Instructions

### Create Virtual Environment
To get started, you need to create and activate a virtual environment for the project.

```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
# On Windows:
myenv\Scripts\activate
# On Mac/Linux:
source myenv/bin/activate
```

### Install Dependencies
Install Django and other necessary dependencies.

```bash
pip install django
```

### Run the Application
Navigate to the project directory and start the server.

```bash
cd coaching_conundrum
python manage.py runserver
```

The server will start and can be accessed in your browser at `http://127.0.0.1:8000/`.

## Application Overview
The Coaching Conundrum application is a web-based platform for scheduling and managing coaching sessions. Coaches and students can interact to set up slots, provide feedback, and manage past and upcoming sessions.

### Features:
1. **Login and User Authentication**: Users can log in as either coaches or students to access different features of the application.
2. **Available Slots**: Coaches can add available slots, and students can view and book these slots.
3. **Booked Slots Management**: Users can manage their booked slots, either cancel or reschedule them.
4. **Feedback**: Coaches can add feedback for completed sessions, and students can view this feedback.
5. **Session History**: Users can view their past calls to keep track of the sessions they have attended.

## How to Use the Application
1. **Login**: Access the login page at `http://127.0.0.1:8000/login/`. Use one of the predefined accounts to log in.
   - **Student Account**
     - Username: `student1`
     - Password: `password123`
   - **Coach Account**
     - Username: `coach1`
     - Password: `password123`
   - **Admin Account**
     - Username: `kikyo`
     - Password: `testpassword`

2. **Dashboard**: After logging in, you will be redirected to the appropriate dashboard based on your user role (student or coach).

3. **For Coaches**:
   - **Add Available Slots**: Navigate to `Available Slots` to add time slots during which you are available for coaching sessions.
   - **View Booked Slots**: Check which slots have been booked by students by accessing the `Booked Slots` page.
   - **Provide Feedback**: After completing a session, go to `Past Calls` and add feedback for each student to help them improve.

4. **For Students**:
   - **View Available Slots**: Go to `Available Slots` to see all available coaching sessions. Select and book a time slot that fits your schedule.
   - **View Booked Slots**: Manage your upcoming sessions through the `Booked Slots` page where you can see details or cancel a session if needed.
   - **View Feedback**: After a session, check the `Feedback` section to view comments provided by the coach on your performance.

5. **Logout**: Click on the `Logout` link in the top navigation bar to end your session securely.

## Common User Actions
- **Book a Slot**: Navigate to the `Available Slots` page, select a slot, and click on `Book Now` to reserve it.
- **Add Feedback (Coaches Only)**: Go to `Past Calls`, select a student, and enter feedback to provide insights on their progress.
- **Cancel a Booking**: Go to `Booked Slots` and click on `Cancel` to free up the slot if you are unable to attend.

## Accessing Static Files
To make sure all CSS, JavaScript, and images load properly, run the following command to collect all static files:
```bash
python manage.py collectstatic
```
This will gather all static assets into a single directory, which can then be accessed by the application.

Feel free to use these accounts to explore the different features of the application.

## Troubleshooting
- **Server Not Starting**: Ensure that the virtual environment is activated and Django is installed.
- **CSS or Static Files Not Loading**: Make sure to run `python manage.py collectstatic` and confirm that the static files are correctly configured.

## License
This project is licensed under the MIT License. Feel free to modify and use it as needed.

