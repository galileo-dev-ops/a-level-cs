# OCR Code Challenges
This is a repository of all code challenges recommended by OCR.


# DISCLAIMER

Last updated: October 26, 2023

__By clicking the link below you agree to the Terms and Conditions as set out in this disclaimer.__

[Click to skip](#caesar-cipher)

### Interpretation and Definitions

#### Interpretation

The words of which the initial letter is capitalized have meanings defined under the following conditions.
The following definitions shall have the same meaning regardless of whether they appear in singular or in plural.

#### Definitions

For the purposes of this Disclaimer:

- __Company__ (referred to as either "the Company", "We", "Us" or "Our" in this Disclaimer) refers to Caesar Cipher Docs.
- __Service__ refers to the Website or the Application or both.
- __You__ means the individual accessing the Service, or the company, or other legal entity on behalf of which such individual is accessing or using the Service, as applicable.
- __Website__ refers to Caesar Cipher Docs, accessible from [https://github.com/galileo-dev-ops/code-challenges-ocr](https://github.com/galileo-dev-ops/code-challenges-ocr)
- __Application__ means the software program provided by the Company downloaded by You on any electronic device named Caesar Cipher.

### Disclaimer

The information contained on the Service is for general information purposes only.

The Company assumes no responsibility for errors or omissions in the contents of the Service.

In no event shall the Company be liable for any special, direct, indirect, consequential, or incidental damages or any damages whatsoever, whether in an action of contract, negligence or other tort, arising out of or in connection with the use of the Service or the contents of the Service. The Company reserves the right to make additions, deletions, or modifications to the contents on the Service at any time without prior notice.

The Company does not warrant that the Service is free of viruses or other harmful components.


### External Links Disclaimer

The Service may contain links to external websites that are not provided or maintained by or in any way affiliated with the Company.

Please note that the Company does not guarantee the accuracy, relevance, timeliness, or completeness of any information on these external websites.


### Errors and Omissions Disclaimer

The information given by the Service is for general guidance on matters of interest only. Even if the Company takes every precaution to ensure that the content of the Service is both current and accurate, errors can occur. Plus, given the changing nature of laws, rules and regulations, there may be delays, omissions or inaccuracies in the information contained on the Service.

The Company is not responsible for any errors or omissions, or for the results obtained from the use of this information.

### Fair Use Disclaimer

The Company may use copyrighted material which has not always been specifically authorized by the copyright owner. The Company is making such material available for criticism, comment, news reporting, teaching, scholarship, or research.

The Company believes this constitutes a "fair use" of any such copyrighted material as provided for in section 107 of the United States Copyright law.

If You wish to use copyrighted material from the Service for your own purposes that go beyond fair use, You must obtain permission from the copyright owner.

### Views Expressed Disclaimer

The Service may contain views and opinions which are those of the authors and do not necessarily reflect the official policy or position of any other author, agency, organization, employer or company, including the Company.

Comments published by users are their sole responsibility and the users will take full responsibility, liability and blame for any libel or litigation that results from something written in or as a direct result of something written in a comment. The Company is not liable for any comment published by users and reserves the right to delete any comment for any reason whatsoever.

### No Responsibility Disclaimer

The information on the Service is provided with the understanding that the Company is not herein engaged in rendering legal, accounting, tax, or other professional advice and services. As such, it should not be used as a substitute for consultation with professional accounting, tax, legal or other competent advisers.

In no event shall the Company or its suppliers be liable for any special, incidental, indirect, or consequential damages whatsoever arising out of or in connection with your access or use or inability to access or use the Service.

### "Use at Your Own Risk" Disclaimer

All information in the Service is provided "as is", with no guarantee of completeness, accuracy, timeliness or of the results obtained from the use of this information, and without warranty of any kind, express or implied, including, but not limited to warranties of performance, merchantability and fitness for a particular purpose.

The Company will not be liable to You or anyone else for any decision made or action taken in reliance on the information given by the Service or for any consequential, special or similar damages, even if advised of the possibility of such damages.

---
---
## Caesar Cipher

### Summary

The Caesar Cipher program implements the following features:
 - Graphical Interface
 - Encryption and decryption
 - User choice of phrase and key
 - Robust design to minimalise errors and improve user experience
 - Brute-force attack system with a dictionary lookup feature for possible matches
 - Saving of encryption and decryption results in a text file, including previous messages.

### Requirements and Running

#### ONLINE ####
To run this program online, use the following link to the project Repl:

```
https://replit.com/@pmkhambhaita/Caesar-Cipher
```

#### OFFLINE ####

To run this program offline, the following are required:
 - Python 3.x
 - Tkinter library
 - ~ 8MB free space

In a terminal, enter the directory of the program and type:

```bash
python3 main.py
```

### Usage

A GUI window will open upon running. There are 3 main elements to the GUI - the entry box where a message is entered, and the two buttons for encrypting and decrypting.
#### To encrypt:
 - Enter the message you wish to encrypt in the text box
 - Press the "Encrypt" button
 - A pop-up window will appear, enter the key you wish to use.
 - Confirm the encryption by typing "Confirm" (not case-sensitive). Any other character will abort the encryption
 - A message will appear stating the encrypted message, after which a popup to save the encrypted message appears.

#### To decrypt:
 - Enter the message you wish to decrypt into the text box
 - Press the decrypt button
 - A pop-up window will appear, enter the key used on the message.
 - A message will appear stating the decrypted message, after which a popup to save the decrypted message appears.

#### To brute-force:
 - Enter the message you wish to decrypt into the text box
 - Press the decrypt button
 - A pop-up window will appear prompting for the key used. Enter either zero or any value outside the range of 1 ≤ n ≤ 26.
 - Another pop-up window will appear to confirm the bruteforce. Type "Confirm" (not case-sensitive) to proceed. Any other character will abort the attack.
 - The brute-force will then take place. Based on the arrangement of letters, various popups will appear as to possible keys. These will also be highlighted in the saved text file with an arrow. eg. ----> Key 1: Test.
 - The brute_force.txt file is saved and a pop-up confirming its success will appear.

### About the caesar_cipher function

The caesar_cipher itself is much shorter than expected, due to the use of an ASCII system rather than an alphanumeric system. I utilised the fact that letters are represented by ascending ASCII numbers (lowercase a being 001 and so on). By using this, you can simply add the key to the ASCII representation of each letter and convert back into alphanumeric characters. This allows for a much shorter program, as well as more versatility surrounding the characters on which the cipher is applied, as it is a short matter to exclude all non-alpha characters, which enables for much longer strings to be used. 


Any questions/bugs, please raise an issue!

Galileo
