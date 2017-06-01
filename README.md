This is the Osprey webpage creator.
Articles are made in using the webpage creator.
Here is an example of a basic article.

\title{}
\\this is a comment\\
\\if nothing in the title bracked it takes it from the page title\\
\paragraph{This is the first paragraph.  All this will be formated using
paragraph tags.}
\section{Section 2, 2}
\paragraph{I also spoke about this in my other \link{page2,
/page/page2}.  Here is a list of items \list{stuff, seperate by commas,
item3, more stuff}.  This is the last sentence of this paragraph}
\paragraph{Final paragraph.  \image{caption, images/image.jpg}  If no
caption is listed then one wont be shown.}

So here is a short list of items

\title{title if different from page title}

\paragraph{content}

\section{section title, 2}

\link{word,href}

\list{x,y,z}

\image{caption, file}

\image{, file}      #for no caption

\\captions are not parsed into the html\\

the number in section is used for the header number i.e.
\section{section, 3} is "<h3>section</h3>"
\title{} is always "<h1></h1>"
all <, > or \ at parsing not used in code will produce an error.

