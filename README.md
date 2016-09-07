# dotswag

Here are three scripts, for managing your dotfiles on multiple devices.
You all know the problem, you have made some changes to a dotfile on one device. As soon as you start working on another device, you have to patch your dotfile on the new device, to keep both on sync.
With this script you can choose a file, which contains all your configs in one place, then choose, which configs you want to 
use and automatically generate them from this one config file.

#Warning

Please backup your configs, before trying this.
Tell me, if something went wrong, and i try to fix it.

#Usage

You need to have a /.swagconf (i guessed no other program uses this one :D ), which is formatted like this:
```
\#\#\#DOTSWAG "tag" "Path/something.conf"
//Your config comes here

\#\#\#DOTSWAG "other_tag" "other_Path/.important.conf"
//Another config file
```
In Tag you can choose a name for this configfile, like vim, i3 or sth.
In Path you specify the Path, where to save the config.
You can work with ~

To generate this file on your device you have 2 Options:
1. Manually copy all your configs into the file and write the headers
2. execute get_configlist.py with the desired URL to the already existing config

After you generated the .swagconf, you need to create a list of tags, you want to use on your devices.
It is stored at ~/.swagsources and automatically generated from your .swagconf, after executing create_config_lists.py .
You can edit it, to exclude some configs from being generated.

To finally generate all of your dotfiles, run create_configs.py and you are done.
