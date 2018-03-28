import models
import store

m1 = models.Member("zoheer",33)
m2 = models.Member("ahmad" ,15)

p1 = models.Post("python","Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.")
p2 = models.Post("html","Hypertext Markup Language (HTML) is the standard markup language for creating web pages and web applications. With Cascading Style Sheets (CSS) and JavaScript, it forms a triad of cornerstone technologies for the World Wide Web.[4] Web browsers receive HTML documents from a web server or from local storage and render them into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.")
p3 = models.Post("CSS","Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language.[1] Although most often used to set the visual style of web pages and user interfaces written in HTML and XHTML, the language can be applied to any XML document, including plain XML, SVG and XUL, and is applicable to rendering in speech, or on other media. Along with HTML and JavaScript, CSS is a cornerstone technology used by most websites to create visually engaging webpages, user interfaces for web applications, and user interfaces for many mobile applications")

msotre = store.MemberStore()
msotre.add(m1)
msotre.add(m2)
print msotre.get_by_id(2)
print msotre.entity_exists(2)
msotre.delete(2)
msotre.get_all()

pstore = store.PostStore()
pstore.add (p1)
pstore.add (p2)
pstore.add (p3)
print pstore.entity_exists(1)
print pstore.get_by_id(1)
pstore.get_all()
