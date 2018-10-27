## smsfy
A tool to notify a SMS if a server is down using uptime robot and kavenegar API.

## Installation

clone the repo using this:

```git clone https://github.com/numb95/smsfy.git```

Use [Virtualenv](https://virtualenv.pypa.io/en/stable/userguide/) to create a virtualenv and then use this to install requirements:

```pip install -r requirements.txt```

Then add your server(s) or website(s) to (uptime robot)[https://uptimerobot.com]. 

Edit the ```smsfy.json``` and put your uptime robot API Key (which can be found in ([uptimerobot.com/dashboard#mySettings](https://uptimerobot.com/dashboard#mySettings) ) it the provided location.
then add your Kavenegar API Key (which can be found in [panel.kavenegar.com/Client/setting/account](https://panel.kavenegar.com/Client/setting/account) ).

After all add a desireable phone number in receptor location, then run the script to test it. 

## Usage

you can use **systemd** or **supervisor** to run it in background. Will add this feature soon :D


## Todo
- [x] Temporary run api keys and reciever from a local json file. will change it to a better solution.
- [ ] Make it systemd friendly, which can run on background 
- [ ] Clean the code. Make it more readable.
- [ ] Make a config file with yaml or json format which can specified the API Keys and receptor
- [ ] Handling custom message.
- [ ] Run config file in ```/etc/smsify.conf``` as a default location.
- [ ] Using ```-c /home/user/smsfy.json``` as a custom located config.
- [ ] Make it to run with multiply receptor.
- [ ] Make a init argument which can create config file in default or user specified location.
- [ ] Create systemd file and enable / start it in init command.
- [ ] Add multiply receptor wizard in init.
- [ ] Add multiply hosts and nickname feature.
- [ ] Add test to the code.

## Contribution
Fork it. Improve it. PR it. I will be very grateful. If you have an idea, put it in issue section. 

## License

> MIT

