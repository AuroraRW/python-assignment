Note: In order to get a tcpdump including payload use the following command (or you
can use wireshark):  
tcpdump -X –n –i interface –s 1500 –c 100 tcp  
# Q1  
Write a search engine that will take a file (like an html source page) and extract all of
the email addresses. It will then print them out in an ordered list. The file may
contain a lot of messy text (i.e. Candice@home is not valid. There can be a lot of
ampersands in the text occupying meaning other than email delimiters!) . (Use the
provided dump for your example)  
# Q2  
Write a program using RE’s that will open a tcpdump file and parse each packet looking
for ascii text in the payload. It will print out the src IP address for each packet followed
by all payload ascii sequences found in that packet. In the print out, separate each new
string group with a ‘///’ delimiter. Be sure to remove all the periods that tcpdump uses
for non-ascii characters!  
# Q3  
Extend your program in Q2 to prompt the user for one or more search strings. Locate
every instance of any of these strings in the payloads of the dump. Words like
“password”, “login”, etc. Search should be case independent. Print the src & dst IP
address for each packet that contains the search string and then print any contiguous
ascii characters (up to 20 max) on either side of the search string to show some
context.
