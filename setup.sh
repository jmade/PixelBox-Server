#!/bin/sh

# COLORS
_reset=$(tput sgr0)
_green=$(tput setaf 76)
_purple=$(tput setaf 171)
_red=$(tput setaf 1)
_tan=$(tput setaf 3)
_blue=$(tput setaf 38)
_bold=$(tput bold)
_unknown=$(tput setaf 77)
_underline=$(tput sgr 0 1)


function _success()
{
    printf "${_green}✔ %s${_reset}\n" "$@"
}

function _bold()
{
	printf "${_bold}%s${_reset}\n" "$@"
}

function _error()
{
	printf "${_red}%s${_reset}\n" "$@"
}



function setupForSSH()
{
	echo "Setting up SSH..."
	cd $HOME 
	mkdir .shh
	cd .ssh/
	touch authorized_keys
	_success "SSH Setup Complete"
}

function systemUpgrades()
{
	echo "System Upgrades"
	sudo apt-get -y update
	sudo apt-get -y upgrade
	_success "System Upgrade Success!"
}

function install_venv()
{
	echo "Install python3-venv."
	sudo apt-get -y install python3-venv
}

function install_pip3()
{
	echo "Install pip Python package manager."
	sudo apt-get -y install python3-pip
}

function install_flask()
{
	echo "Installing Flask."
	sudo pip3 install Flask
}

function install_tmux()
{
	echo "Installing tmux"
	sudo apt-get -y install tmux
	_success "tmux Installed!"
}

function install_gunicorn()
{
	echo "Installing gUnicorn"
	sudo pip3 install gunicorn
	_success "gUnicorn Installed!"
}


function install_rpi_ws281X()
{
	printf "Installing ${_blue}RPI_WS281X${_reset} LED Library\n"
	sudo pip3 install rpi_ws281x
}


function install_pillow()
{
	printf "Installing ${_purple}Pillow${_reset} Library\n"
	sudo pip3 install Pillow
}

function install_image_libs()
{
	printf "Installing ${_tan}Image Libraries${_reset}\n"
	sudo apt-get -y install libtiff5 libopenjp2-7 libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
}

function install_numpy()
{
	printf "Installing ${_unknown}libatlas${_reset}\n"
    sudo apt-get -y install libatlas-base-dev
	printf "Installing ${_unknown}NumPy${_reset} Library\n"
	sudo pip3 install numpy
}



function installh264()
{
	cd
	git clone git://git.videolan.org/x264
	cd x264
	./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl
	make -j4
	sudo make install
	_success "h.264 Installed!"
}

function install_ffmpeg()
{
	cd
	git clone git://source.ffmpeg.org/ffmpeg.git
	cd ffmpeg
	./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
	make -j4
	sudo make install
	_success "ffmpeg Installed!"
}


# MariaDB
function install_mariaDB()
{
	_bolded "Installing MariaDB"
	sudo apt-get install mariadb-server -y
	_success "MariaDB Installation Successful!"

}

# pymysql
function install_pymysql()
{
	_bolded "Installing pymysql"
	sudo pip3 install pymysql
	_success "pymysql Installation Successful!"
}





function _main()
{
	_bold "-~- Starting Setup Script -~-"
	# install_image_libs
	install_numpy
	_success "-~- Finished Install Script -~-"
}


_main

