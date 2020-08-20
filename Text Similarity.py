#Text Similarity
text1 = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed."
text2 = """Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[28]
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[29]
Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system with reference counting.
Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3.
The Python 2 language was officially discontinued in 2020 (first planned for 2015), and "Python 2.7.18 is the last Python 2.7 release and therefore the last Python 2 release."[30] No more security patches or other improvements will be released for it.[31][32] With Python 2's end-of-life, only Python 3.5.x[33] and later are supported.
Python interpreters are available for many operating systems. A global community of programmers develops and maintains CPython, a free and open-source[34] reference implementation. A non-profit organization, the Python Software Foundation, manages and directs resources for Python and CPython development."""

set1 = set(text1)
set2 = set(text2)
#tokenization
token1 = text1.split()
token2 = text2.split()


#stopwords ->is,am ,are they,them,us i,we,the,and ,or,not,was,were...
import nltk
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))

set1 = set1.difference(stopwords)
set2 = set2.difference(stopwords)

union = set1.union(set2)
intersection = set1.intersection(set2)

jaccardsIndex = len(intersection)/len(union)

print(jaccardsIndex*100)


