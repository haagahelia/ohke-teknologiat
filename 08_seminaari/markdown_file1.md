Note: These examples were written with VS Code that has the "Markdown PDF" extension installed. It also
can be used to preview the markdown output. Right click on the .md file tab and select "Open Preview".

# Level 1 (=chapter) heading

Normal text. *Italic text inside asterisk/star* 

## Level 2 (=subchapter) title

Normal text. **Strong text inside double asterisks/stars**

[Text to show on the link](https://web.microsoftstream.com/) 

## Bulleted items - unordered list with one start **and a space**

* Potato
* Carrot
* Onion

## Ordered list with just giving all of them: 1. 

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

% Not all markdown versions support all markup syntax you can find. E.g. this % mark does nothing for me in VS Code that has the
Markdown PDF installed. 

Also this footnote thing is not working here
Let's do some footnotes[^note]
Let's do second footnote[^note]

> Another nice quote

That quote was from a nice guy. [@Nice Guy]. This syntax doesn't work either.

<hr />

Look into the *Markdown* source code for how to add images linked from internet 

![Special Result Day 2022](https://pbs.twimg.com/media/FPxeW6CXoAs2GiI?format=png&name=small)
Well, failed to find Markdown way to add this as tooltip for the image: "Special Result Day 2022"

...or taken from local images folder 

![Are Nato nukes at Russia's border like Kremlin has always claimed?](images/WhereAreNATONukesjpg.jpg)

Note: You can invoke the list of the other files in VS Code when you type ctrl+space or type in dot/"the full stop" character  .

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

