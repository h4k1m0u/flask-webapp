# Installation of node/npm with nvm
- nvm allows to manage different versions of node, and can be installed with:

```
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```

- Install node and npm with: `nvm install 9` (couldn't build potree from source using other versions)


# Potree
- Download latest stable pre-built version from [Potree 1.6](https://github.com/potree/potree/releases/download/1.6/Potree_1.6.zip).
- Or download the [source code](https://github.com/potree/potree/archive/1.6.zip) of the same version and build it with:

```
npm install
npm install -g gulp
gulp watch
```


# Creation of a virual-host for potree examples
- Install apache2: `sudo apt install apache2`
- Copy potree folder to `/var/www`, and make this folder editable with: `chown -R hakim:hakim potree`
- Create a vhost in `/etc/apache2/sites-available/potree.local.conf`, and copy the following in it:

```
<VirtualHost *:80>
	ServerName potree.local

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/potree-1.6

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

- Enable vhost: `sudo a2ensite potree.local.conf`
- Reload apache2: `sudo service apache2 reload`
- Add to `etc/hosts` this line: `127.0.0.1 potree.local`
- From the browser access: `potree.local/examples`
