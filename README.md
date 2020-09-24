# Alphabetical-Sort
Sorts the given assignment text into alphabetical order, ignoring case sensitivity. **Text is tokenized using regular expressions**

## Assumptions:
### 1. Structure of text does not need to be maintained.
### 2. Each sentence is treated as independent of context
   - i.e Sentences from a quote will be split as normal sentences
   - e.g The Cosmic AC said, "I WILL DO SO. I HAVE BEEN DOING SO FOR A HUNDRED BILLION YEARS. MY PREDECESSORS AND I HAVE BEEN ASKED THIS QUESTION MANY TIMES. ALL THE DATA I HAVE REMAINS INSUFFICIENT."
        ### becomes : 
           The Cosmic AC said, I WILL DO SO
           I HAVE BEEN DOING SO FOR A HUNDRED BILLION YEARS
           MY PREDECESSORS AND I HAVE BEEN ASKED THIS QUESTION MANY TIMES
           ALL THE DATA I HAVE REMAINS INSUFFICIENT
        and is then processed by the sorting algorithm
### 3. The previous assumption means phrases may start with lowercase letters
  - e.g "Will you keep working on it?" asked Man.
    ### becomes :
        Will you keep working on it
        asked Man
    and is then processed by the sorting algorithm
### 4. Any and all sentences that do not begin with a letter are trimmed until the first character is a letter.
  - e.g "Go ahead," said Jerrodine. "It will quiet them down." (Jerrodette II was beginning to cry, also.)
    ### becomes :
        Go ahead, said Jerrodine
        It will quiet them down
        (Jerrodette II was beginning to cry, also
    ### where the last phrase is trimmed to just : 
        Jerrodette II was beginning to cry, also
