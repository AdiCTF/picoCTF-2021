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

There are two ways to solve this challenge:
#### Way 1
Opening the program in HxD and searching (with ctrl+f) "pico" - this will find us the beginning of the flag.

#### Way 2
Trying to run the program in wsl. When adding the flag -h - it would reveal us the correct flag.



# Cryptography
## Mod 26
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}

**solution:**

:triangular_flag_on_post: **picoCTF{next_time_I'll_try_2_rounds_of_rot13_aFxtzQWR}**

cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE} is encrypted with ROT13. Hence, for example, c becomes p, v becomes i and so on.
