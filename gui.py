# Planned and coded by Trang Nguyen <pneppy@gmail.com>

import tkinter as tk
import tkinter.font as tkFont
from communicators import alice, bob, malice

"""
    This is involver-oriented GUI. 
    Each communicator has his/her own section to send messages. (Alice and Bob)
    Attacker has his/her own section to see messages (both encrypted and decrypted) 
    and modify them. (Malice)
"""

root = tk.Tk()

root.title("Attack on key-exchange protocol")
width = 800
height = 500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

alice_label = tk.Label(root, text="ALICE", font=tkFont.Font(family="Helvetica", size=20))
alice_label.place(x=30, y=120)

alice_input = tk.Text(root)
alice_input["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=12)
alice_input["font"] = ft
alice_input["fg"] = "#333333"
alice_input.place(x=30, y=170, width=190, height=50)


def alice_send_malice():
    alice.send_message(alice_input.get("1.0", 'end-1c'), malice)
    malice_input.delete("1.0", tk.END)
    bob_input.delete("1.0", tk.END)
    malice_input.insert(tk.END, malice.receive_message(alice))
    alice_input.delete("1.0", tk.END)


alice_send = tk.Button(root)
alice_send["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=12)
alice_send["font"] = ft
alice_send["fg"] = "#000000"
alice_send["justify"] = "center"
alice_send["text"] = "SEND TO MALICE"
alice_send["command"] = alice_send_malice
alice_send.place(x=90, y=230, width=140, height=25)

bob_label = tk.Label(root, text="BOB", font=tkFont.Font(family="Helvetica", size=20))
bob_label.place(x=540, y=120)

bob_input = tk.Text(root)
ft = tkFont.Font(family='Times', size=12)
bob_input["font"] = ft
bob_input["fg"] = "#333333"
bob_input.place(x=560, y=170, width=200, height=50)

malice_label = tk.Label(root, text="MALICE", font=tkFont.Font(family="Helvetica", size=20))
malice_label.place(x=150, y=300)

malice_input = tk.Text(root)
ft = tkFont.Font(family='Times', size=12)
malice_input["font"] = ft
malice_input["fg"] = "#333333"
malice_input.place(x=310, y=290, width=198, height=111)


def bob_send_malice():
    bob.send_message(bob_input.get("1.0", 'end-1c'), alice)
    alice_input.delete("1.0", tk.END)
    malice_input.delete("1.0", tk.END)
    malice_input.insert(tk.END, str(malice.receive_message(bob)))
    alice_input.insert(tk.END, alice.receive_message(bob))
    bob_input.delete("1.0", tk.END)


bob_send = tk.Button(root)
bob_send["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=12)
bob_send["font"] = ft
bob_send["fg"] = "#000000"
bob_send["justify"] = "center"
bob_send["text"] = "SEND TO ALICE"
bob_send["command"] = bob_send_malice
bob_send.place(x=620, y=230, width=130, height=25)


def malice_send():
    bob_input.insert(tk.END, malice_input.get("1.0", 'end-1c'))
    malice_input.delete("1.0", tk.END)


malice_send_alice = tk.Button(root)
malice_send_alice["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=12)
malice_send_alice["font"] = ft
malice_send_alice["fg"] = "#000000"
malice_send_alice["justify"] = "center"
malice_send_alice["text"] = "SEND TO ALICE"
malice_send_alice["command"] = malice_send
malice_send_alice.place(x=300, y=420, width=130, height=25)

malice_send_bob = tk.Button(root)
malice_send_bob["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=12)
malice_send_bob["font"] = ft
malice_send_bob["fg"] = "#000000"
malice_send_bob["justify"] = "center"
malice_send_bob["text"] = "SEND TO BOB"
malice_send_bob["command"] = malice_send
malice_send_bob.place(x=440, y=420, width=130, height=25)
