# enviro config file

# you may edit this file by hand but if you enter provisioning mode
# then the file will be automatically overwritten with new details

provisioned = 1

# enter a nickname for this board
nickname = 'Your Nickname'

# network access details
wifi_ssid = '<your-wifi-name>'
wifi_password = '<your-wifi-password>'

# how many log files to keep
log_count = 20

# how often to wake up and take a reading (in minutes)
reading_frequency = 5

# where to upload to ("web_hook", "mqtt", "adafruitio")
destination = 'http'

# how often to upload data (number of cached readings)
upload_frequency = 1

# web hook settings
custom_http_url = 'https://<api-baseurl>/'
custom_http_username = '<userId>'
custom_http_password = '<apiKey>'