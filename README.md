# picoCTF-2021
my solutions to picoCTF 2021


# General Skills
## Obedient Cat
This file has a flag in plain sight (aka "in-the-clear"). [Download flag.](picoCTF-2021-assets/Obedient-Cat/flag)

**solution:**

:triangular_flag_on_post: **picoCTF{s4n1ty_v3r1f13d_f28ac910}**

when opening the file in Notepad++ - the flag is right there.

![image](https://user-images.githubusercontent.com/119416868/204558531-1793b137-32c7-4def-8d01-bdd1f53fa5bb.png)

## Python Wrangling
Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](picoCTF-2021-assets/Python-Wrangling/ende.py) using [this password](picoCTF-2021-assets/Python-Wrangling/pw.txt) to get [the flag](picoCTF-2021-assets/Python-Wrangling/flag.txt.en)?

**solution:**

:triangular_flag_on_post: **picoCTF{4p0110_1n_7h3_h0us3_6008014f}**

We have 3 files here - python script, a password (a string) and a flag (a string). When looking at the python script there are two interesting strings:

![image](https://user-images.githubusercontent.com/119416868/205485956-f1dde24c-7cfe-4fd3-94ef-6a309980b9d1.png)

sys.argv[0] refers to the python script. We can assume from the script and the help_msg that we need to use the flag -e if we would like to encrypt and the flag -d if we would like to decrypt.

![image](https://user-images.githubusercontent.com/119416868/205485937-0be2977b-4222-4a0a-8370-6498a20b35e8.png)

Now, we will enter the password that was given to us - 6008014f6008014f6008014f6008014f and reveal the correct flag.

## Wave a flag
Can you invoke help flags for a tool or binary? [This program](picoCTF-2021-assets/Wave-A-Flag/warm) has extraordinarily helpful information...

**solution:**

:triangular_flag_on_post: **picoCTF{b1scu1ts_4nd_gr4vy_d6969390}**

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

:triangular_flag_on_post: **picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}**

`nc mercury.picoctf.net 22342` is giving us a list of numbers. I thought that these numbers represent ASCII characters. Therefore, I redirect this list to a file called `inputNetcat.txt`.

Note that I used the command `bash` for the next commands.
Then, I ran a code that goes line by line and convert the number to its ASCII charecter: `while read -r line; do printf \\$(printf "%o" $line); done < inputNetcat.txt`.

![image](https://user-images.githubusercontent.com/119416868/205496322-83f27e37-5565-4c4e-bb83-75aebe2df488.png)


# Cryptography
## Mod 26
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}

**solution:**

:triangular_flag_on_post: **picoCTF{next_time_I'll_try_2_rounds_of_rot13_aFxtzQWR}**

cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE} is encrypted with ROT13. Hence, for example, c becomes p, v becomes i and so on.


# Forensics
## information
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](picoCTF-2021-assets/information/cat.jpg)

**solution:**

:triangular_flag_on_post: **picoCTF{the_m3tadata_1s_modified}**

When opening the image there is a cute :cat2: but it doesn't help us. We will look at the meta-data of this image with exiftool (`exiftool cat.jpg`).

![image](https://user-images.githubusercontent.com/119416868/205489998-a9afe0cb-9206-4bdd-8a0c-7914c95095d1.png)

The License field looks like Base64 - and when decoding it we will reveal the flag.
:cat:


# Reverse Engineering
## Transformation
I wonder what this really is... [enc](picoCTF-2021-assets/Transformation/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

**solution:**

:triangular_flag_on_post: **picoCTF{16_bits_inst34d_of_8_e141a0f7}**

In the site CyberChef I chose the Magic option with Intensive mode and found the flag.

# Binary Exploitation
## Stonks
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](picoCTF-2021-assets/Stonks/vuln.c) `nc mercury.picoctf.net 33411`











