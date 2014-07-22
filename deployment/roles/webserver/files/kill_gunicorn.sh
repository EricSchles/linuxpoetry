ps -A | grep gunicorn | awk '{print "kill "$1}' | bash
