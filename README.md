# Linux-Battery-Control
A very simple scripts pack with GUI to manage the charging limit of a Linux laptop's battery

It modifies a system file that requires root access, so to avoid the scripts breaking because of the
password, it takes it from environment variable SUDO_PASS which must be created

It's higly recommended to own all files to the root user (sudo chown root.root path_to_each_file)
to avoid its modification by 3rd parties and compromise security

# Requirements
-Python 3.* with Tkinter (sudo apt install python3-tk) and a global environment variable named SUDO_PASS containing the sudo access password

# Content:
-auto_startup.sh: Bash Script that runs the automathic charging limit when the system starts, this file
 should be modified to set the custom value
-manual_conf.sh: Bash Script file that runs a simple Tkinter GUI with multiple charging limit choices
-interface.py: The Tkinter interface mentioned in the previous line
-get_env.py: Python Script to get the sudo password from the previous mentioned environment variable

# Setup
-You must replace in both .sh files the line "path to file" with the path in which you placed the Python scripts 

# Usage
-auto_startup.sh is conceived for auto-running at system startup, via the distros' own options or using cron
-manual_conf.sh is conceived for creating a .desktop file at usr/share/applications to use it as a regular desktop
 appliaction or to launch it via a custom keyboard shortcut
 
 Feedback would be very appreciated, feel free of making any suggestions or improvments
