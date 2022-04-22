Note: These examples were written with VS Code that has the "Markdown PDF" extension installed. It also
can be used to preview the markdown output. Right click on the .md file tab and select "Open Preview". Test your Markdown markup also in GitHub.

# Level 1 (=chapter) heading

Normal text. *Italic text inside asterisk/star* 

## Level 2 (=subchapter) title

Normal text. **Strong text inside double asterisks/stars**

[Text to show on the link](https://web.microsoftstream.com/) 

## Bulleted items - unordered list with one start **and a space**

* Potato
* Carrot
* Onion

## Ordered list with just by giving all options the ordinal 1.  Easily to shuffle later!

1. ready
1. steady
1. go!

Inline code examples can be written inside backticks:` (life) => 42`

```
// code blocks with three backticks

if(true) {
    console.log('Hello, world!');
}

```


> Quotes you can add with the bigger than sign, so they look like this.


| code | country |
| :--: | :-----: |
| KEN  | Kenia   |
| FIN  | Finland |
| ABS  | Absurdia |

<hr />

Look into the *Markdown* source code for how to add images linked from internet, this is the general architecture of the Finnish Finna service: 

![Alternative text for e.g. people with impaired vision](https://www.kiwi.fi/download/attachments/200048777/Ohjelmistoarkkitehtuuri.png?version=1&modificationDate=1607524001948&api=v2)


...or taken from local 'images' folder, like this complicated Wikipedia image of server architectures: 

![Wikipedia's sample picture of server architecture](images/1200px-Wikimedia_Server_Architecture_(simplified).svg.png)

Note: You can invoke the list of the other files in VS Code when you type ctrl+space or type in dot/"the full stop" charsacter  .

Three ways to write the Horizontal rule:
<hr />

---

***

This is how you can create the ...

**Table of Contents**

[Level 1 (=chapter) heading](#level-1-chapter-heading)

[Level 2 (=subchapter) title](#level-2-subchapter-title)

[Bulleted items - unordered list with one start and a space](#bulleted-items---unordered-list-with-one-start-and-a-space)

Open the markdown file in GitHub.com and use it to copy the link that you need in creation of the table of contents,
just keep the part starting with the #

### Link to second file in same folder
[Link to the second file](markdown_file2.md)


## One "official" source for markdown syntax

[CommonMark.org Markdown in 60 seconds](https://commonmark.org/help/)

[CommonMark.org Markdown tutorial in 10 minutes](https://commonmark.org/help/tutorial/)

Though, these are pieces [Markdown syntax that did not work](markdown_not_supported_syntax.md) in VS Code markdown preview nor in GitHub version of the Markdown.