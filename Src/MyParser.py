from html.parser import HTMLParser

class MyParser(HTMLParser):
  links = list()
  metaData = list()
  pageTitle = None
  getTitle = False


  def handle_starttag(self, tag, attrs):
    if tag == 'a' :
      for ele in attrs:
        if ele[0] == 'href':
          self.links.append(ele[1])
    elif tag == 'meta':
      tempData= list()
      for ele in attrs:
        tempData.append((ele[1]))
      self.metaData.append(tempData)
    elif tag == 'title':
      self.getTitle = True

  def handle_data(self, data):
    if self.getTitle:
      self.pageTitle = data
      self.getTitle = False