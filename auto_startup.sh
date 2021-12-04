python3 /home/xandor19/Scripts/Battery/get_env.py | sudo -S su && echo 30 | sudo tee /sys/class/power_supply/BAT0/charge_control_end_threshold
