sudo chmod 755 stop.cgi

sudo chmod 755 reverse.cgi

sudo chmod 755 left.cgi

sudo chmod 755 right.cgi

Now, execute some tests to confirm that all is working:

./forward.cgi

./left.cgi

./reverse.cgi

./right.cgi

./stop.cgi

It is a good practice that we have a specific directory for the programs used and call it “bin”. So, to save the scripts that we will use in the project, we must create a directory like cgi-bin containing all executable scripts (or binary files). For example, /var/www/cgi-bin.

So, let’s create the directory www under var, where our webpage will be located and under it, the cgi-bin directory with the scripts:

sudo mkdir /var/www

sudo mkdir /var/www/cgi-bin

Now, let’s move all files to this new directory:

sudo mv /*.cgi /var/www/cgi-bin

cd /var/www/cgi-bin

Using the line command ls, you can see the files created (see photo).

ls

One last thing before we move to another step. If you reboot the RPi, the GPIOs will return to their default condition that is INPUT. So, we must change the script /etc/rc.local that is executed at any Raspberry’s start. Just before the last command at the script ==> exit 0, we must include the GPIOs mode commands:

sudo nano /etc/rc.local

…

gpio -g mode 5 out

gpio -g mode 6 out

gpio -g mode 13 out

gpio -g mode 19 out

...

exit 0