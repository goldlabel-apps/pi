# enviro config file

# you may edit this file by hand but if you enter provisioning mode
# then the file will be automatically overwritten with new details

provisioned = 1

# enter a nickname for this board
nickname = 'White Box'

# network access details
wifi_ssid = 'ARRIS-A751'
wifi_password = 'BWR123201500'

# how many log files to keep
log_count = 20

# how often to wake up and take a reading (in minutes)
reading_frequency = 5

# where to upload to ("web_hook", "mqtt", "adafruitio")
destination = 'http'

# how often to upload data (number of cached readings)
upload_frequency = 1

# web hook settings
custom_http_url = 'https://helloworld-gupgkbhkma-uc.a.run.app/'
custom_http_username = 'aa88d1d5-8632-4a20-a1d2-d91d86078c37'
custom_http_password = '58235fe5-b321-4fa2-a369-11c3b6608163'