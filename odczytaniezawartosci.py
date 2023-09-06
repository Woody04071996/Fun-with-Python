import subprocess
prog = subprocess.Popen("dir", stdout=subprocess.PIPE, shell=True)
(wynik, err) = prog.communicate()
print(f"'Surowy' wynik komendy \'dir\':\n {wynik} ")
