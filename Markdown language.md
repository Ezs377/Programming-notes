# MD Language
Markdown language is a language similar to HTML that is used for writing .md files. There are many different formats that can be used to alter the look of the font and the text.
Markdown language is much simpler to write than pure HTML, as HTML requires several tags that take quite a while. There are a lot of programs that can make writing HTML easier, but markdown language is simple enough on its own. 

New lines are created by simply adding a blank line in between. Note that there has to be a blank line between paragraphs, otherwise they are combined into one paragraph.

Adding two whitespaces after a line allows the text to have a linebreak. ALternatively use the HTML tag for a linebreak, which is \<br>

Linebreak example  
linebreak example<br>
linebreak example

For **bold** text, use a double asterisk ( \**\<text>**).

For *italic* text, use a single asterisk ( \*\<text>* ).

For both ***bold and italic***, use triple asterisks  (\***\<text>**)

For lists:
- Use numbers to make a numbered list. Example:

1. One
2. Two
3. Three
  4. Indented four (has 2 spaces before number)

* Use a single asterisk ( \* ) at the start of a line to create bullet points

- Or alternatively, use a dash ( \- )
  - Adding 2 spaces before a dash or number creates a sub-point

Text indented by 2 whitespaces will also follow the indent of the list. The same also applies to other types of text formatting. 
For writing code, use 8 spaces instead of 4.  
Example:

- First item

  Indented paragraph

- Second item

# Headings are created by using a hashtag ( \# ). More hashtags mean smaller font. A maximum of 6 hashtags can be used for 6 different heading sizes
## Tier 2 heading
### Tier 3 heading
#### Tier 4 heading
##### Tier 5 heading
###### Tier 6 heading

> A right arrow ( \> ) is used to write quotes

Using a backslash ( \\ ) will cancel out the next character afterwards, useful for writing certain characters without accidentally formatting the text. Example:

## Heading not backslashed
\## Heading backslashed

To write code in the text, use a backtick symbol ( \` )(it's usually right under the esc key). Codes can only be read if the md file is run on Github. Otherwise it will just show up as normal text.
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

To write a horizontal line breaker, use a triple dash or asterisk on a line by itself.
***

Images can be imported by using \![\<alternative name>](\<image URL>). If the image is located in the Github repository then the URL link of the image in the Github page can be used as the URL (e.g. https://github.com/Ezs377/Programming-notes/blob/main/Images/Programming%20paradigms.jpg). If the URL is wrong or there is no image the alternative text is used instead.

Links are imported the same way, except without the exclamation mark, like this: \[\<text>](\<link URL>).

To add a tooltip with the link, add the tooltip text right after the URL using quotation marks, like this: \[\<text>](\<link URL> \"<tooltip>")

Otherwise, for writing quick links, simply close a URL in angle brackets (\<URL>

For URLs, use \%20 as spaces instead of just spacing the words in a URL.

Links can be formatted like normal text (Italic, bold, quoted, etc)

Reference style links can be used. These links are tidier and easier to read when written in the code, but produce the same output as a normal link when the page is read by software. To use such links, firstly create a reference link that is stored anywhere in the md file. The label for this link is closed in square brackets (\[ ] ). This is followed by the URL, and finally an optional title for the link that is closed in either quotation marks or brackets. To reference this link, the linked text is closed in square brackets (\[ ]), folloed by the label which is also in square brackets.
An example of the reference format: \[\<label>]: \<URL> (optional title)  
An example of the link format: \[\<text>] [\<label>]  
An example using the reference link format:

[My Github page][1]

The code is avaialble so you can see what is going on

[1]: https://github.com/Ezs377/Programming-notes (Github page)


