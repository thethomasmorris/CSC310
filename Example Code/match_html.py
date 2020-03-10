from array_stack import ArrayStack #call a class from a different file

def is_matched_html(raw):
  """Return True if all HTML tags are properly match; False otherwise."""
  S = ArrayStack()
  j = raw.find('<')               # find first '<' character (if any)
  while j != -1:
    k = raw.find('>', j+1)        # find next '>' character
    if k == -1:
      return False                # invalid tag
    tag = raw[j+1:k]              # strip away < >
    if not tag.startswith('/'):   # this is opening tag
      S.push(tag)
    else:                         # this is closing tag
      if S.is_empty():
        return False              # nothing to match with
      if tag[1:] != S.pop():      # tag[1:] strip away '/'
        return False              # mismatched delimiter
    j = raw.find('<', k+1)        # find next '<' character (if any)
  return S.is_empty()             # were all opening tags matched?

if __name__ == '__main__':
    print (is_matched_html('<body>EKU CS is one of the best Computer Science program in KY.</body>'))   #return True
    print(is_matched_html('<p></p>'))
    print (is_matched_html('<p>EKU CS is one of the best Computer Science program in KY.</li>'))     #return False

    print (is_matched_html('<body><center><h1> The Little Boat </h1></center><p> The storm tossed '
                           'the little boat like a cheap sneaker in an old washing machine. The '
                           'three drunken fishermen were used to such treatment, of course, but '
                           'not the tree salesman, who even as a stowaway now felt that he had '
                           'overpaid for the voyage. </p><ol><li> Will the salesman die? </li><li> '
                           'What color is the boat? </li><li> And what about Naomi? </li></ol></body>'))     #return True
