# Installing and Setting Up Git

We will use Git to work together on our shared codebase. Git is version-control open-source software that allows us to work on code individually while we test, document, and prepare new functions and features. Once we are ready to share the new additions to the larger project, we can open a pull request to receive feedback and modify our code until it is accepted and incorporated into the larger project's codebase.

GitHub is a popular code repository web-based hosting service web-based hosting service that uses Git to help developers collaborate on code. It offers a desktop program to help make Git more intuitive.

## Install Git

Open up a terminal window and type the following command to check whether Git is installed:

```
git --version
```

If you receive output that indicates that `git` is not a recognized command, it is most likely because Git is not installed. If you are working with the most current version of Git, feel free to move on to the **Create a GitHub Account** section.

Please follow the relevant sections below for Windows or Mac installation. For more context on Git and open source, you can read [How To Contribute to Open Source: Getting Started with Git](https://www.digitalocean.com/community/tutorials/how-to-contribute-to-open-source-getting-started-with-git)

If you have determined that Git is not installed on your computer, you can download the installer for the current version from [Git's Website](https://git-scm.com). Once it has finished downloading the file, launch the installer and accept the license information displayed at its start.

![](./images/git/git_site.png)


### Windows Users

You will now see a screen showing several installation options. Make sure that you have all of these boxes checked:

![](./images/git/git_install_options.png)

Once you have checked all of the boxes displayed in the picture, hit "Next" to move on to the next step.

![](./images/git/vim_default.png)

Git allows you to designate a default text editor for handling merge conflicts and other changes that you will need to make to your code. We will be using Atom for this, but will change the settings at a later point. For now, leave the default editor as Vim.

The next screen allows you to set your PATH environment, which is what allows you to use Git from the command line. Make sure that the middle option is checked.

![](./images/git/git_path.png)

On the next screen, make sure that "Use the OpenSSL Library" option is checked, and move on to the next page.

![](./images/git/git_line_ending.png)

Make sure that check the top option ("Checkout Windows-style"), as these settings will help tell Git what type of computer you are using, and will allow it to convert files as necessary. This lets other people view your code no matter what operating system they are on.

After this step, you should select the default terminal emulator that Git uses. Please ensure that you are using MinTTY.

![](./images/git/git_terminal.png)

The following step should be left as its defaults:

![](./images/git/git_options.png)

If you are given the option to install experimental options on the next page, please do not select any of them at the moment. Often times they are not yet fully tested, and can sometimes cause issues that are best to avoid.

Finally, you should now be able to install Git onto your computer. Once it is finished, you can move on to the **Create a GitHub Account** section.

### Mac Users

After you have downloaded the installer file, run the file. If you get an error saying that the file is from an unidentified developer, you should hold "Control" while clicking on the file, and then select "Open".

![](./images/git/mac_force_open.png)

You should now get another screen with a ".pkg" file. Double click on it and follow the remaining steps. You will probably need to enter your password at some point in the process.

Git should now be installed on your computer. Once you are finished, you can move on to the **Create a GitHub Account** section.

![](./images/git/git_dmg.png)

## Create a GitHub Account

Next, you should create a [GitHub account](https://github.com/join) if you don't already have one.

It is worth noting that you can get added benefits through GitHub and other technology organizations — including unlimited private code repos — by signing up for the [Student Developer Pack.](https://education.github.com/pack)

## Install Atom
Atom is a text editor created by GitHub that allows you to make quick edits to code as well as manage several Git commands directly from the editor.

When [Installing Atom](https://atom.io), make sure to install the appropriate version for your machine and follow the installation steps.
