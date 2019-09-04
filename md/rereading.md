# Setting up Prompted Readings 

At this point, you have all of the tools necessary to work on our project installed -- Git, Atom, Python, Node/npm, and PyCharm -- so let's put it all together and get the project running.

##### Cloning the Repository
Go to the GitHub page for [Prompted Readings](https://github.com/dhmit/prompted_readings).

![](./images/prompted_readings.png)

Click on the green "Clone or Download" button, and then copy the url to your clipboard.

![](./images/clipboard_copy.png)

Open Atom and go to `View > Toggle Command Palette`.

![](./images/toggle_palette.png)

In the box that appears, type `GitHub: Clone`.

![](./images/command_palette.png)

Paste the url from GitHub into the `Clone from` field.

![](./images/clone_prompted.png)

Please use the default location for the project.

After the project finishes downloading, you should now have a "Project" pane with a file tree. 


##### Sign in with GitHub
After the project is successfully cloned onto your computer, click on the GitHub logo in the bottom-right corner of Atom

![](./images/github_button.png)

You should see a screen that prompts you to login to GitHub.

![](./images/login.png)

The process will require you to login from a browser in order to retrieve a token specific to your account. Once you have the token, paste it into the prompt and hit `Login`.


##### Setting up our project in PyCharm 
Open PyCharm, and select "Open".
![](./images/pycharm_init_6.png)

Select the path where you cloned the repo in the step above. This will bring up the main PyCharm window with the loaded prompted_readings directory
on the left.

On a Mac, select `PyCharm -> Preferences`; On Windows, `File -> Settings`
![](./images/pycharm_config_4.png)

You need to configure your Python interpreter under "Project: prompted_readings"
-> Project Interpreter. Click on the wheel in the top right and select "Add".
![](./images/pycharm_config_6.png)

Select "New Environment". Make sure that the base interpreter is the path that you noted when installing Python.
![](./images/new_venv.png)

Leave the location for the interpreter as the default provided by PyCharm.

Apply your changes and exit the settings.

##### Preparing npm
Open PyCharm and go to the `prompted_readings` Repository.

At the bottom left of the PyCharm window, there should be a button labelled `Terminal`, which will open a terminal window inside of the IDE.

![](./images/find_terminal.png)

Once it is open, it should function the same as other terminals that you may have used. Note that there is now a (venv) marker at the start of the line - this indicates that we are using the virtual environment that was [set up with PyCharm](3_pycharm_install_setup.md).

In the PyCharm terminal, enter the `frontend` directory with:

```
$ cd frontend
```

Now that we are in the directory that contains all of our package requirements for our Javascript, we can install everything that you need with the following command:

```
$ npm install
```

After npm indexes and installs the required packages, you will be setup for using and editing all of the frontend code in the repository.

