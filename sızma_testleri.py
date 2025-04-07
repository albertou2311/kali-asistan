import subprocess

def sql_injection_testi():
    subprocess.run(["sqlmap", "-u", "http://hedefsite.com/login", "--dbs"])

def xss_test():
    subprocess.run(["xsser", "-u", "http://hedefsite.com"])

# Testleri çalıştır
sql_injection_testi()
xss_test()
