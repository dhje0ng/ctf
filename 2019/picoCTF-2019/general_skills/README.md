# PicoCTF 2019(General Skills)

<small> [ Write-Up ] </small>
<hr>
<h5> 2Warm - 50pt </h5>
<p> Can you convert the number 42 (base 10) to binary (base 2)? </p>
<p> Answer : 101010 </p>
<strong> Flag : picoCTF{101010} </strong>
<hr>

<h5> Lets Warm Up - 50pt </h5>
<p> If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII? </p>
<p> Answer : 0x70 - > p </p>
<strong> Flag : picoCTF{p} </strong>
<hr>

<h5> Warmed Up - 50pt </h5>
<p> What is 0x3D (base 16) in decimal (base 10) </p>
<p> Answer : 0x3D -> 61 </p>
<strong> Flag : picoCTF{61} </strong>
<hr>

<h5> Bases - 100pt </h5>
<p> What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases </p>
<p> Answer : bDNhcm5fdGgzX3IwcDM1 -> l3arn_th3_r0p35 </p>
<strong> Flag : picoCTF{l3arn_th3_r0p35} </strong>
<hr>

<h5> First Grep - 100pt </h5>
<p> Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_4_6b0be85ad029e98c683231bdafec396c on the shell server. </p>
<p> Answer : cat file | grep 'picoCTF' </p>
<strong> Flag : picoCTF{grep_is_good_to_find_things_ad4e9645} </strong>
<hr>

<h5> Resources - 100pt </h5>
<p> We put together a bunch of resources to help you out on our website! If you go over there, you might even find a flag! https://picoctf.com/resources (link) </p>
<strong> Flag : picoCTF{r3source_pag3_f1ag} </strong>
<hr>

<h5> strings it - 100pt </h5>
<p> Can you find the flag in file without running it? You can also find the file in /problems/strings-it_2_865eec66d190ef75386fb14e15972126 on the shell server. </p>
<p> Answer : strings strings | grep 'picoCTF' </p>
<strong> Flag : picoCTF{5tRIng5_1T_d5b86184} </strong>
<hr>

<h5> what's a net cat? - 100pt </h5>
<p> Using netcat (nc) is going to be pretty important. Can you connect to 2019shell1.picoctf.com at port 4158 to get the flag? </p>
<p> Answer : nc 2019shell1.picoctf.com 4158 </p>
<strong> Flag : picoCTF{nEtCat_Mast3ry_700da9c7} </strong>
<hr>

<h5> Based - 200pt </h5>
<p> To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc 2019shell1.picoctf.com 31615. </p>
<p> Answer : Binary > Octal > Hex to Ascii </p>
<strong> Flag : picoCTF{learning_about_converting_values_502ff297} </strong>
<hr>

<h5> First Grep: Part 2- 200pt </h5>
<p> Can you find the flag in /problems/first-grep--part-ii_3_b4bf3244c2886de1566a28c1b5a465ae/files on the shell server? Remember to use grep. </p>
<p> Answer : grep -r picoCTF </p>
<strong> Flag : picoCTF{grep_r_to_find_this_3675d798} </strong>
<hr>

<h5> plumbing - 200pt </h5>
<p> Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to 2019shell1.picoctf.com 21957. </p>
<p> Answer : nc 2019shell1.picoctf.com 21957 | grep picoCTF </p>
<strong> Flag : picoCTF{digital_plumb3r_c1082838} </strong>
<hr>

<h5> whats-the-difference - 200pt </h5>
<p> Can you spot the difference? kitters cattos. They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server </p>
<p> Answer : Hex Editor to Data Checksum </p>
<strong> Flag : picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j3lly} </strong>
<hr>

<h5> where-is-the-file - 200pt </h5>
<p> I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_4_f26b413d005c16c61f127740ab242b35. </p>
<p> Answer : cat .* </p>
<strong> picoCTF{w3ll_that_d1dnt_w0RK_cb4a5081} </strong>
<hr>

<h5> flag_shop - 300pt </h5>
<p> There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc 2019shell1.picoctf.com 11177. </p>
<p> Answer : Integer Overflow </p>

```html
Buy Flags
Defintely not the flag Flag
send(9999999999999)
Buy Flags
1337 Flag
Enter(1)
```

<strong> picoCTF{m0n3y_bag5_b9f469b5} </strong>
<hr>

<h5> mus1c - 300pt </h5>
<p> I wrote you a song. Put it in the picoCTF{} flag format </p>
<code> Hint : Rockstar Programming Language </code><br><br>
<p> Answer : Decimal -> ASCII </p>
<p> https://codewithrockstar.com/online </p>
<p> https://tomeko.net/online_tools/dec_to_ascii.php?lang=en </p>
<strong> Flag : picoCTF{rrrocknrn0113r} </strong>
<hr>

<h5> 1_wanna_b3_a_r0ck5tar - 350pt </h5>
<p> I wrote you another song. Put the flag in the picoCTF{} flag format </p>
<code> Hint : Rockstar Programming Language </code><br><br>
<code> Hint2 : if & else are not supported </code><br><br>

```html
Listen to the music             
If the music is a guitar 
Say "Keep on rocking!"          
Listen to the rhythm
If the rhythm without Music is nothing
Else Whisper "That ain't it, Chief"
```

<p> https://codewithrockstar.com/online </p>
<p> https://tomeko.net/online_tools/dec_to_ascii.php?lang=en </p>
<strong> Flag : picoCTF{BONJOVI} </strong>