# Getting started with Git and GitHub
By following the instructions in this tutorial, you'll learn how to use Git and GitHub with both command line and visual interfaces to:
* Create a repository (a place to keep your code)
* Commit your code (similar to saving a snapshot of it) for later
* Perform basic GitHub operations such as forking and making pull requests
## What's Git? What's GitHub?
Git is a piece of **version control software** (also referred to as a VCS for short). Similar to how many online services keep an edit history of all the changes that have been made to a document, Git provides a history of snapshots of your code at different points in time. Each one of these snapshots is called a **commit**, and they can be useful when you want to see what your code was like at different points in time for any reason.

GitHub is an online service which uses Git to allow users to host repositories. It takes advantage of the utility of Git while also adding its own functionality like **pull requests**. But we'll get to that later!
## Getting started
This tutorial assumes you already have Git installed on your computer. The easiest way to check whether you have it or not is to run `git --version` on your command line. The command line will be necessary for this tutorial, so [install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) then come back!

Side note: accessing your command line is dependent on your operating system.
* On macOS, just open Terminal app (found in `/Applications/Utilities/` or use Spotlight Search to find Terminal)
* On Windows, you'll need to find the Command Prompt (you can open it by pressing Win + R on your keyboard, then type `cmd` and click OK)

You'll also need a GitHub account. You can sign up for one here. (Pro tip: if you're a student, you also qualify for a [free subscription to GitHub Pro](https://education.github.com/pack) plus a bunch more awesome developer tools!)
### Fork this repository
The first thing you'll need to do is make a **fork** of this repository. A fork is a way of making your own copy of someone else's repository which you can use to make changes. In addition, if you want to add the changes you made back to the original repository, you'll be able to do that later by using a **pull request** which will integrate the code on your fork back into the original codebase.
- On the upper right of your screen, right under your profile picture, you should see a "Fork" button. Click this, then click your GitHub username if prompted.
It's as easy as that! But right now, your fork only lives on GitHub. Next, we'll want to get a copy of your fork onto your computer.
### Clone your new fork
After installing Git on your computer, the next step is to make a **clone** of this repository. A clone is a local (offline) copy of this repository that lives on your computer—you can make code changes there yourself, then when you're done you can push (upload) your changes back to the online (remote) repository.
* First, if you haven't already been redirected to your fork, you'll need to find it. A good place to look is `https://github.com/USERNAME/tutorials` (replacing `USERNAME` with your GitHub username.)
* Once you're inside your new fork, you should see a green button that says "Clone or download" with a dropdown menu. Click it and copy the URL.
* Next, open your command line (see instructions above, under the "Getting started" header). Use the `cd` command to change into the directory in which you want to house your code. When we clone the repository, it'll make a new folder inside the directory you change to with this command.
* Finally, run `git clone <url>`, but make sure to replace <url> with the Git URL you copied earlier. After a couple of seconds, you should see that a new folder was generated inside the directory you chose with `cd`, containing all the files of your `tutorials` fork!
### Make some changes
The next step is the one which you'll spend the most time on when actually coding! For this example, adding a file with your name should be sufficient.
* When you're actually coding, you'll need a good editor! You can choose any one you like, but some of our favorites at HDAC are [Visual Studio Code](https://code.visualstudio.com/) and [Atom](https://atom.io/). They're both free, so you can try them and see which one you like!
### Commit your changes
Next, we're going to make a **commit**—essentially a snapshot of the changes you've made since your last commit. Eventually, when you've built up your codebase, these snapshots will be very useful to look back on, so you can see how previous versions of your code looked.
* Going back to the command line from before, run `git commit -a -m "<message>"`, replacing <message> with a message describing what you changed in the commit.
* Next, we have to push your changes. Right now, they're only stored as a commit on your local computer, but we want to send them to GitHub. We can do that by running `git push origin master`.
* After a couple seconds, you should be done! Go back to your fork's GitHub page, and check to make sure you see your new commit in the recent commit bar.
## Pull request
Now that you've made changes on your local computer and pushed them to your fork on GitHub, it's time to merge them back into the original repository, by using a **pull request**. This allows the maintainers of the repository which you're trying to merge into to have a look at your code, and if everything looks good, they can merge the changes automatically!
* On the webpage for your fork, you should see a button that says "New pull request". Click that, then make sure you're merging with your fork as the head repository and the original repository as the base repository (this should be already be done for you by default).
* Next, click the green button which says "Create pull request", and follow the steps to submit a request, including a title and message.

Once you've submitted your pull request, you're done! You've completed the essential Git/GitHub workflow—you forked and cloned, made code changes, pushed, and made a pull request to merge your code back into the original repository. Nice job! After the pull request is approved, you'll see your changes reflected in the original repository! 😄
