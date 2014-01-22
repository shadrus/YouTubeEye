YouTubeEye
==========

Python script, that helps to control stat changes for the YouTube channel in Mac OS Notification Center

First of all, for using this script, you should install ruby gem terminal-notifier

$ [sudo] gem install terminal-notifier

Then you should edit models/api_req.py to change USER_NAME = ''. It need to use YouTube user name.

And start app by

python /path_to_app/main.py

For start on Mac startup, I use Automator


No it can control last 50 public videos from user channel