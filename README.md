# picoCTF-2021
my solutions to picoCTF 2021


# General Skills
## Obedient Cat
This file has a flag in plain sight (aka "in-the-clear"). [Download flag.](picoCTF-2021-assets/Obedient-Cat/flag)

**solution:**

:checkered_flag: **picoCTF{s4n1ty_v3r1f13d_f28ac910}**

when opening the file in Notepad++ - the flag is right there.

![image](https://user-images.githubusercontent.com/119416868/204558531-1793b137-32c7-4def-8d01-bdd1f53fa5bb.png)

## Python Wrangling
Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](picoCTF-2021-assets/Python-Wrangling/ende.py) using [this password](picoCTF-2021-assets/Python-Wrangling/pw.txt) to get [the flag](picoCTF-2021-assets/Python-Wrangling/flag.txt.en)?

**solution:**

:checkered_flag: **picoCTF{4p0110_1n_7h3_h0us3_6008014f}**

We have 3 files here - python script, a password (a string) and a flag (a string). When looking at the python script there are two interesting strings:

![image](https://user-images.githubusercontent.com/119416868/205485956-f1dde24c-7cfe-4fd3-94ef-6a309980b9d1.png)

sys.argv[0] refers to the python script. We can assume from the script and the help_msg that we need to use the flag -e if we would like to encrypt and the flag -d if we would like to decrypt.

![image](https://user-images.githubusercontent.com/119416868/205485937-0be2977b-4222-4a0a-8370-6498a20b35e8.png)

Now, we will enter the password that was given to us - 6008014f6008014f6008014f6008014f and reveal the correct flag.

## Wave a flag
Can you invoke help flags for a tool or binary? [This program](picoCTF-2021-assets/Wave-A-Flag/warm) has extraordinarily helpful information...

**solution:**

:checkered_flag: **picoCTF{b1scu1ts_4nd_gr4vy_d6969390}**

I found two ways to solve this challenge:

_Way 1_-
Opening the program in HxD and searching (with ctrl+f) "pico" - this will find us the beginning of the flag.

![image](https://user-images.githubusercontent.com/119416868/205487497-8a1cb8ba-db7a-4e7f-ae01-124e08ca6abd.png)

_Way 2_-
Trying to run the program in wsl. When adding the flag -h - it would reveal us the correct flag.

![image](https://user-images.githubusercontent.com/119416868/205487515-13131987-c155-4983-8a2f-e56d0ceb7b10.png)


## Nice netcat...
There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22342`, but it doesn't speak English...

**solution:**

:checkered_flag: **picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}**

`nc mercury.picoctf.net 22342` is giving us a list of numbers. I thought that these numbers represent ASCII characters. Therefore, I redirect this list to a file called `inputNetcat.txt`.

Note that I used the command `bash` for the next commands.
Then, I ran a code that goes line by line and convert the number to its ASCII charecter: `while read -r line; do printf \\$(printf "%o" $line); done < inputNetcat.txt`.

![image](https://user-images.githubusercontent.com/119416868/205496322-83f27e37-5565-4c4e-bb83-75aebe2df488.png)


## Static ain't always noise
Can you look at the data in this binary: [static](picoCTF-2021-assets/Static-aint-always-noise/static)? This [BASH script](picoCTF-2021-assets/Static-aint-always-noise/ltdis.sh) might help!

**solution:**

:checkered_flag: **picoCTF{d15a5m_t34s3r_98d35619}**

I found two ways to solve this challenge:

_Way 1_- Opening "static" in HxD and searching (with ctrl+f) "pico" - this will find us the beginning of the flag.

![image](https://user-images.githubusercontent.com/119416868/206221922-4253304a-249b-4c70-a000-b4d2d505c7e1.png)

_Way 2_- Using the BASH script that was given to us. 

![image](https://user-images.githubusercontent.com/119416868/206221998-92059293-a192-45c3-bd65-99c8b41d4184.png)

Then, I opened the "static.ltdis.strings.txt" file and found the flag.

![image](https://user-images.githubusercontent.com/119416868/206222070-e24907cd-e032-4d0f-abde-88c8b7b9d088.png)


## Tab, Tab, Attack
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](picoCTF-2021-assets/Tab-Tab-Attack/Addadshashanammu.zip)

**solution:**

:checkered_flag: **picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}**

First, I uziped the file we got. Then, I wrote the name of the file (without the `.zip` ending) and pressed `tab` until I got to a file that is not a directory. After that, I pressed `enter` and got the flag. It is shown in the video below:

https://user-images.githubusercontent.com/119416868/206487395-449662d3-0e22-4121-a07b-d8de526f933e.mp4


## Magikarp Ground Mission
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`

**solution:**

:checkered_flag: **picoCTF{xxsh_0ut_0f_\/\/4t3r_1118a9a4}**

This challenge launches an instance on demand by pressing this bottom:

>insert photo

After pressing I got a `ssh` command:

>insert photo

Then, I copied and pasted it to the "picoCTF Webshell" and inserted the password that was given - `481e7b14`. 
After connecting I used the command `ls` and found out there were 2 files - `1of3.flag.txt, instructions-to-2of3.txt`. `1of3.flag.txt` contained part of the flag and `instructions-to-2of3.txt` instructed me to go to the root directory. In the root directory there were many files but I needed only two - `2of3.flag.txt, instructions-to-3of3.txt`. `2of3.flag.txt` contained another part of the flag and `instructions-to-3of3.txt` instructed me to go to the home directory. There, in the file `3of3.flag.txt` I found the last part of the flag. I put all the pieces together and got my flag - picoCTF{xxsh_0ut_0f_\/\/4t3r_1118a9a4}. You can see the full journey below:

>insert photo


# Cryptography
## Mod 26
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}

**solution:**

:checkered_flag: **picoCTF{next_time_I'll_try_2_rounds_of_rot13_aFxtzQWR}**

cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE} is encrypted with ROT13. Hence, for example, c becomes p, v becomes i and so on.

## Mind your Ps and Qs
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](picoCTF-2021-assets/Mind-Your-Ps-and-Qs/values)

**solution:**

:checkered_flag: **picoCTF{sma11_N_n0_g0od_00264570}**

RSA, which stands for Rivest–Shamir–Adleman is an asymmetric cryptography algorithm. For understanding the algorithm, I have found the following videos very useful:
- [The RSA Encryption Algorithm (1 of 2: Computing an Example)](https://youtu.be/4zahvcJ9glg)
- [The RSA Encryption Algorithm (2 of 2: Generating the Keys)](https://youtu.be/oOcTVTpUsPQ)

After watching the videos I found the prime factors of the n we got using this [site](https://www.dcode.fr/prime-factors-decomposition). 
I got that the prime factors are:
```
p = 2159947535959146091116171018558446546179  
q = 658558036833541874645521278345168572231473 
```
Then, I wrote the next python code and found the flag:
```
from Crypto.Util.number import inverse, long_to_bytes  
  
# prime factors of n  
p = 2159947535959146091116171018558446546179  
q = 658558036833541874645521278345168572231473  
# The given e  
e = 65537  
# The given c - what we want to decrypt  
c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667  
  
phi = (p - 1) * (q - 1)  
d  = inverse(e, phi)  
# inverse is logically equivalent to:  
# for d in range(phi + 1):  
#     if d * e % phi == 1:  
#         break  
  
n = p * q  
num_integer = pow(c, d, n)  
# logically equivalent to:  
# num_integer = (c ^ d) % n  
  
print(long_to_bytes(num_integer))
```

# Forensics
## information
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](picoCTF-2021-assets/information/cat.jpg)

**solution:**

:checkered_flag: **picoCTF{the_m3tadata_1s_modified}**

When opening the image there is a cute :cat2: but it doesn't help us. We will look at the meta-data of this image with exiftool (`exiftool cat.jpg`).

![image](https://user-images.githubusercontent.com/119416868/205489998-a9afe0cb-9206-4bdd-8a0c-7914c95095d1.png)

The License field looks like Base64 - and when decoding it we will reveal the flag.
:cat:

## Matryoshka doll
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](picoCTF-2021-assets/Matryoshka-doll/dolls.jpg)

**solution:**

:checkered_flag: **picoCTF{96fac089316e094d41ea046900197662}**

We got an image of a doll. I tried to use the tool `binwalk` (`binwalk dolls.jpg`) which is a tool for searching a given binary image for embedded files and executable code. Then, I got the following output:

![image](https://user-images.githubusercontent.com/119416868/211202213-ab29bad7-5d25-41f6-8d30-36fff70ffdb1.png)

I assumed that I should add tha `-e` flag in order to extract the zip file so I tried again with `binwalk -e dolls.jpg`. Then, an interasting directory was shown - `_dolls.jpg.extracted`. When opening this file there is another interesting directory (`base_images`) with another doll image inside. Here we can see a living example of matryoshka dolls - an image inside image. Therefore I wrote a [bash script](picoCTF-2021-assets/Matryoshka-doll/matryoshkaScript.sh) in order to go through all the images untill I find the flag. Then, I found the flag:

![image](https://user-images.githubusercontent.com/119416868/211202195-3c55e066-8d68-437d-ae09-cea54e95475e.png)



# Reverse Engineering
## Transformation
I wonder what this really is... [enc](picoCTF-2021-assets/Transformation/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

**solution:**

:checkered_flag: **picoCTF{16_bits_inst34d_of_8_e141a0f7}**

In the site CyberChef I chose the Magic option with Intensive mode and found the flag.

## keygenme-py
[keygenme-trial.py](picoCTF-2021-assets/keygenme-py/keygenme-trial.py)

**solution:**

:checkered_flag: **picoCTF{1n_7h3_|<3y_of_0d208392}**

I ran the python file we got. Then, I had to choose one of four options. Because the name of the challenge is `keygenme-py`, I chose `(c) Enter License Key`. 

![image](https://user-images.githubusercontent.com/119416868/208479461-d246c7c4-1545-4643-834b-d12a8d7438fb.png)

But, I don't know the license key so I will try to figure it out from the python file.
When opening the file the is the beginning of a flag and I guess we will have to find the `dynamic` part of it.
```
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
When I chose the `(c)` option, the function `enter_license` was called. This function is the only one which is calling to the function `decrypt_full_version` - our goal in this challenge. 

![image](https://user-images.githubusercontent.com/119416868/208479751-4bc56522-1e00-4363-83a4-1c257a7a9235.png)

In order to reach the `decrypt_full_version` function, I will have to look at the function `check_key`. From this function I can assume that my license key should be as long as the `key_full_template_trial` that can be seen above. In addition, both should have the same static part and we can get the dynamic part by using the sha256 hashing algorithm as can be seen in the following code:
```
import hashlib  
username_trial = b"FREEMAN"  
  
dynamic = [ hashlib.sha256(username_trial).hexdigest()[4],  
    hashlib.sha256(username_trial).hexdigest()[5],  
    hashlib.sha256(username_trial).hexdigest()[3],  
    hashlib.sha256(username_trial).hexdigest()[6],  
    hashlib.sha256(username_trial).hexdigest()[2],  
    hashlib.sha256(username_trial).hexdigest()[7],  
    hashlib.sha256(username_trial).hexdigest()[1],  
    hashlib.sha256(username_trial).hexdigest()[8] ]  
  
print(*dynamic, sep="")
```

I got that the dynamic part is `0d208392` and when combined with the static parts I got that the flag is: picoCTF{1n_7h3_|<3y_of_0d208392}.
After entering it as the license key, we get the full version.

![image](https://user-images.githubusercontent.com/119416868/208479824-99fcee05-8d24-411a-9c60-0ed2057cc2cc.png)


## crackme-py
[crackme.py](picoCTF-2021-assets/crackme-py/crackme.py)

**solution:**

:checkered_flag: **picoCTF{1|\/|_4_p34|\|ut_ef5b69a3}**

I ran the python file with wsl and entered some numbers just to understand the program.

![image](https://user-images.githubusercontent.com/119416868/208692444-ba2758d7-71e1-4cb2-a7b7-14528244416d.png)

Then, I opened the python file and understood that I had to decode a secret -
```
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE067d3eh2bN"
```
Also, there were two functions at that file - `decode_secret` and `choose_greatest` but it only used `choose_greatest`. Therefore I used the function `decode_secret` with `bezos_cc_secret` as parameter and after I ran it - I got the flag. You can see the new and correct file `ICrackedYou.py` [here](picoCTF-2021-assets/crackme-py/ICrackedYou.py).
And below you can see the revealing of the flag:

![image](https://user-images.githubusercontent.com/119416868/208692498-0bf2f873-72c7-4a1f-9e1d-6b6895c59eb7.png)



# Binary Exploitation
## Stonks
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](picoCTF-2021-assets/Stonks/vuln.c) `nc mercury.picoctf.net 33411`

**solution:**

🏁 **picoCTF{I_l05t_4ll_my_m0n3y_a24c14a6}**

We will focus on the `buy_stonks` function.

![image](https://user-images.githubusercontent.com/119416868/205678644-18ef89c8-4e3a-4547-b46f-83bb24363a1e.png)

buffer + scanf + printf is a 🚩 for me. 
In line 93 there is an interestig line: `printf(user_buf);`. The command `printf` without `%s` is prone to format strings attacks. Therefore, after choosing to "Buy some stonks" (option 1), we can submit as our API token a string that contains `%x` and "walk" on the stack. Note that we can assume the flag is on the stack from the beginning of the `buy_stonks` function.

![image](https://user-images.githubusercontent.com/119416868/205678808-8fc791fb-9342-497f-ab34-95c96be1d11b.png)

Then, after inserting a sequence of `%x` as our API token we will get the content of the stack in _little endian_. 

![image](https://user-images.githubusercontent.com/119416868/205683883-b6fc7dbe-bfc1-4ec6-acc4-d1c8af5654c6.png)

I marked the beginning of our flag. This is "pico" in hex (note that it is in _little endian_). 

![image](https://user-images.githubusercontent.com/119416868/205683568-93e04402-e4c0-46c9-baad-d1bcf4efe3d5.png)

Hence, I will copy from the marked string. With CyberChef we can choose the "swap endianness" option and then convert it from hexa.

![image](https://user-images.githubusercontent.com/119416868/205684947-5b08293a-4eb4-47f5-a1fd-d1132c040124.png)



# Web Exploitation
## GET aHEAD
Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:15931/](http://mercury.picoctf.net:15931/)

**solution:**

🏁 **picoCTF{r3j3ct_th3_du4l1ty_82880908}**

The attached website is quite simple - changes the background with the click of a button.
In Burp Suite I targeted this website.

![image](https://user-images.githubusercontent.com/119416868/206041416-4360464c-800f-447f-8a48-17bfc4802736.png)

Then, I opened it on the browser, turned the intercept on and clicked "Choose Red". Here is the Request:

![image](https://user-images.githubusercontent.com/119416868/206041461-7daa28d6-1abc-4128-9b17-fe7237d14ffc.png)

I pressed "Choose Blue" and then Forward on Burp Suite and received the following Request:

![image](https://user-images.githubusercontent.com/119416868/206041506-b0b523e8-afb9-4086-b8dc-2f8aaeeab4a4.png)

As can be seen above, I marked the HTTP request methods that were used - GET & POST. More HTTP request methods can be found [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods). Note that the name of the challenge is "GET aHEAD", therefore I tried replacing GET with HEAD, which is also a HTTP request method. 

![image](https://user-images.githubusercontent.com/119416868/206041571-ab25d2a4-1376-4f7d-ba81-29de44b2eef0.png)

But, Ooops!💣⬜ I got a blank page!

![image](https://user-images.githubusercontent.com/119416868/206041617-92658127-80e8-4dd9-a090-ce2834248173.png)

So, I clicked "Options" in the "Proxy" section and chose to intercept responses.

![image](https://user-images.githubusercontent.com/119416868/206041692-2b819c75-bc1c-41f7-aec3-0c59f3c40d07.png)

And after forwarding the request again - the flag was revealed.

![image](https://user-images.githubusercontent.com/119416868/206041735-e182646e-4de6-483c-8ee8-fe83f5b2e283.png)





