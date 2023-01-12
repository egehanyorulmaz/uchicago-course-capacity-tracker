After spending hours on the website just to add the classes that I want, I decided to create this repository so that the available spots in each course will be checked in certain intervals.

I have utilized Selenium, BeautifulSoup and Docker to achieve my goal.

To use this repository:
 1. You should add your credentials to the uchicago-course-capacity-tracker/config/credentials. This information will stay at your local machine, and will not be shared with anybody. 
 2. Run the "curriculum_tracker.py"
 3. In the DuoPush screen, manually click to the push and confirm the notification that comes to your device for authentication.
 4. Wait until the process is completed :)

My goal is to automate the entire process and deploy the docker container as an API, and open access to every UChicago student. By registering the classes that you want to add in the add/drop period, you will be notified when there is an open spot in the section with an email :) 
