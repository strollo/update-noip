Update your no-ip.com domain name through crontab
=================================================

Reason
------

I created this script because my IP address does not change really often and I was bothered by the fact that www.noip.com sends email about your domain name expiring after more than 30 days without a change. To remedy this behavior I decided to write that script and run it into a scheduled job every 10 days.

How does this work
------------------

The script can be run every 20 days and it will force your domain name to update with a wrong IP address and a moment after it will update it with the proper IP address. This will bypass the expiration rule.

Installation
------------

*Requirements
This little script requires the ``requests`` python module from http://docs.python-requests.org/en/latest/

.. code-block:: bash

	git clone git@github.com:drivard/update-noip.git
	
	cd update-noip
	
	pip install -r requirements.txt
	
	# or
	
	pip install -U requests
	
	# or
	 
	easy_install requests


Configuration
=============

The script
----------

- Copy the file in etc/noip.ini.sample in etc/noip.ini
- Edit the credentials in this file

Execution
---------
To run the script once you edited the parameters.

.. code-block:: bash
	
	python update_noip.py

Crontab
-------

.. code-block:: bash

	15 3 */10 * *   /usr/bin/python /<path_to_python_script>/update_noip.py >> /dev/null 2>&1


