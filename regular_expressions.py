import re
str1="M.S Dhoni(born in 7th july,1981),"\
    "is a former international cricketer who captained"\
    "the indian national cricket team in limited-overs"\
    " from 2007 to 2017 and in Test cricket from 2008 to 2014."\
    " He is currently the captain of Chennai"\
    "Super Kings, a franchise based team of "\
    "Indian Premier League."
matches1=re.findall("is",str1)
print(matches1)
matches2=re.search("He",str1)
print(matches2)
matches3=re.split(str1,"he")
print(matches3)
matches4=re.match(str1,"league")
print(matches4)