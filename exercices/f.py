with open("data.txt") as f, open('d.txt') as p:
    for line in  f.readlines():
        print(line)

# pour windows:
# Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
# .\venv\Scripts\Activate.ps1