Markdown language is a language similar to HTML that is used for writing .md files. There are many different formats that can be used to alter the look of the font and the text.
Images can be imported by using ![<alternative name>](<image URL). If the image is located in the Github repository then the URL link of the image in the Github page can be used as the URL (e.g. https://github.com/Ezs377/Programming-notes/blob/main/Images/Programming%20paradigms.jpg). If the URL is wrong or there is no image the alternative text is used instead.
For **bold** text, use a double asterisk ( **<text>**).
For *italic* text, use a single asterisk ( *<text>* ).
For lists:
- Use numbers to make a numbered list. Example:

  1. One
  2. Two
  3. Three
  
* Use a single asterisk ( * ) at the start of a line to create bullet points

- Or alternatively, use a dash ( - )
  - Adding 2 spaces before a dash creates a sub-bullet point

# Headings are created by using a hashtag ( # ). More hashtags mean smaller font. A maximum of 6 hashtags can be used for 6 different heading sizes
## Tier 2 heading
### Tier 3 heading
#### Tier 4 heading
##### Tier 5 heading
###### Tier 6 heading

> A right arrow ( > ) is used to write quotes

To write code in the text, use a backtick symbol ( ` )(it's usually right under the esc key). Codes can only be read if the md file is run on Github. Otherwise it will just show up as normal text.
`This is short code`

Use triple backticks or indent 4 spaces before a line to write longer code. Example:

    Written with 4-spaces indent
	if x = 2:
		print ('cool')

You can also specify the programming language code you're writing to make the colors come out as well 
```Python
# Written with triple backticks in Python
x = 5
while x <= 10:
	x += 1
print ("done")
```

