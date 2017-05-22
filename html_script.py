#!/usr/bin/env python3.5 
import subprocess
import os

def check_package():
	check_apache = subprocess.run(["dpkg","-l","apache2"]).returncode
	if check_apache != 0:
		print("Please install apache") 
		install_apache2()
	else:
		print("Apache installed so edit config") 
		change_config()

def install_apache2():
	update_sys = subprocess.run(["apt-get","update"])
	upgrade_sys = subprocess.run(["apt-get","-y","upgrade"])
	install_apache = subprocess.run(["apt-get","-y","install","apache2"]).returncode
	if install_apache !=0:
		print("Successfully installed")

def change_config():
	cmd = subprocess.run(["cp", "/etc/apache2/sites-available/000-default.conf", "/etc/apache2/sites-available/mynewsite.conf"]).returncode
	print(cmd)


check_package()


