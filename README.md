# Lexicon-Site-Project
Hey all! This is where we will be storing the site files for the foreseeable future. The repository could do with some restructuring, but for the time being it should serve us just fine. The repository is currently split into 2 sections: the front end and the back end. 

The folder titled "Front" will contain all the front-end files we interact with, and the backend will contain all the database content which is required even for the current blog application.

We will also likely be integrating with our hosting service through github, so performing that integration will be one of my personal goals for the winter break.


<h2>General Instructions</h2>
Information specific to working with git can be found <a href = "https://docs.github.com/en/get-started/quickstart/hello-world">here.</a> <br>
<i>note: in order to clone repositories now, you need an authentication token (if you are not logged in via github desktop, and are trying to clone from the command line).</i>

<h3>Frontend</h3>
For the time being, because the front end / UI is being developed independently of the backend, it is actually probably easiest to just upload files/changes directly to the repository, rather than having to clone, add, commit and push each time. So for HTML, CSS, and JavaScript files, those can all go in the frontend folder. From there, I (Zaheer) will make the necessary changes in order for them to be deployed directly to the site (because Django requires that we register each file directly, and there is some strange mixing of Python into the HTML files that gets a tad confusing). 

<h3>Backend</h3>
This is a slightly more laborious process.
Once you've entered into the desired path and cloned the repository, perform the following commands in order to set up the environment:
<br>
<br>
<i>
path $ cd Backend
  <br>
path\Backend $ .\venv\Scripts\activate
  <br>
(venv)path\Backend $
  </i>
  <br>
  <br>

Because individual migrations performed will impact the overarching file structure withinn Backend, it is important to clone the repo and push to a separate branch which can then be merged to main, once a pull request is approved.
  
