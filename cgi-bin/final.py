#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()
f = cgi.FieldStorage()
cmd = f.getvalue("x")

if cmd == "list":
    cmd = "docker ps -a"
    o = subprocess.getoutput("sudo " + cmd)

elif cmd == "run":
    cmd = "docker run -dit " + f.getvalue("y") + ":" + f.getvalue("z")
    o = subprocess.getoutput("sudo " + cmd)

elif cmd == "pull":
    cmd = "docker pull " + f.getvalue("y") + ":" + f.getvalue("z")
    o = subprocess.getoutput("sudo " + cmd)

elif cmd == "images":
    cmd = "docker images"
    o = subprocess.getoutput("sudo " + cmd)

elif cmd == "start":
    cmd = "docker start " + f.getvalue("y")
    o = subprocess.getoutput("sudo " + cmd)

elif cmd == "stop":
    cmd = "docker stop " + f.getvalue("y")
    o = subprocess.getoutput("sudo " + cmd)


elif cmd == "exec":
    cmd = "docker exec -d " + f.getvalue("y") + " " + f.getvalue("z")
    o = subprocess.getoutput("sudo " + cmd)

elif cmd == "remove":
    cmd = "docker rm " + f.getvalue("y") + " --force"
    o = subprocess.getoutput("sudo " + cmd)




print(cmd + "<br />")
print("<br />")
print("<pre>")
print(o)
print("</pre>")
print("<br />")

