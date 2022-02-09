# MD Language
Markdown language is a language similar to HTML that is used for writing .md files. There are many different formats that can be used to alter the look of the font and the text.
Markdown language is much simpler to write than pure HTML, as HTML requires several tags that take quite a while. There are a lot of programs that can make writing HTML easier, but markdown language is simple enough on its own. It is possible to use HTML and Markdown language together in one page. Markdown is easier to write, but HTML is more customizable and has more features. However, HTML and Markdown code needs to be separate (e.g. not in the same line) and HTML is usually not indented when writing it in Markdown language.

New lines are created by simply adding a blank line in between. Note that there has to be a blank line between paragraphs, otherwise they are combined into one paragraph.

Adding two whitespaces after a line allows the text to have a linebreak. ALternatively use the HTML tag for a linebreak, which is \<br>

Linebreak example  
linebreak example<br>
linebreak example

For **bold** text, use a double asterisk ( \**\<text>**).

For *italic* text, use a single asterisk ( \*\<text>* ).

For both ***bold and italic***, use triple asterisks  (\***\<text>**)

For ~~strikethoughs~~, use double tildes (\~~)

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

# Headings  
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

Use triple backticks or indent 4 spaces before a line to write longer code (only on certain markdown processors). Example:

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

To add a tooltip with the link, add the tooltip text right after the URL using quotation marks, like this: \[\<text>](\<link URL>"\<tooltip>").

Otherwise, for writing quick links, simply close a URL in angle brackets (\<URL>)

For URLs, use \%20 as spaces instead of just spacing the words in a URL.

Links can be formatted like normal text (Italic, bold, quoted, etc)


Reference style links can be used. These links are tidier and easier to read when written in the code, but produce the same output as a normal link when the page is read by software. To use such links, firstly create a reference link that is stored anywhere in the md file. The label for this link is closed in square brackets (\[ ] ). This is followed by the URL, and finally an optional title for the link that is closed in either quotation marks or brackets. To reference this link, the linked text is closed in square brackets (\[ ]), followed by the label which is also in square brackets.
An example of the reference format: \[\<label>]: \<URL> (optional title)  
An example of the link format: \[\<text>] [\<label>]  
An example using the reference link format:

[My Github page][1]

The code is available so you can see what is going on

[1]: https://github.com/Ezs377/Programming-notes (Github page)

## Github specific md language:
Github utilises its own version of markdown language, Github Flavored Markdown (GFM). This version allows people to add in more features using markdown language. Not all markdown language processors (software) can run all features, so ensure these features can be displayed with your software before writing the code.  

**Tables**
A table is created by using hyphens ( \- ) and pipes ( \|\)
| For example | This is a header |
| ----------- | ---------------- |
| This is text | This is more text | 

| Use \----- in a row | to separate headers | from text |
| :--- | :---: | ---: |
| Left indent, \:--- | Middle indent, \:---: | Right indent, ---: |

Heading ID's can be used to scroll automatically to a heading using a link.  
### To use a heading ID, add curly brackets with the ID inside ( \{ } )  
Then link it in a link by using a hashtag instead of a slash  
Some markdown processors (like Github) automatically generate heading IDs based on the heading. In this case, no curly brackets are needed. Hover over the chain icon beside a heading to get the heading id, then put it in the brackets. Usually, a hashtag (\#), followed by words. All lowercase, and use dashes (\-) as spaces if the heading has multiple words.  
For example:   
[Link that goes to headings](#Headings)

Emojis can be inserted by copy-pasting an emoji or using emoji shortcodes. Note that shortcodes for emojis can be different for each markdown processor.  
😀 This was copy-pasted  
:smiley: This was using shortcode :smiley  
Shortcodes can be looked up or show up sometimes as autofillers in certain markdown processors (like in Github)  
[A list of emoji and their shortcodes](https://gist.github.com/rxaviers/7360908)
