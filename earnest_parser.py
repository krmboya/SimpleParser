import re, urllib2

def ReadFile(filename):
  infile = open(filename, 'r')
  return infile.read()

def ParseInput(stream):
  pattern = '<dl><dt><strong><strong>(.+?):</strong></strong></dt><dd><span.+?>(.+?)</span><br></dd></dl>'
  output = re.findall(pattern, stream)
  return output

def Sanitize(stream):
  stage_directions_pattern = '<span\sclass="stage">.+?</stage>'
  definitions_pattern = '<a\shref=.+?>.+?</a>'
  directions = re.findall(stage_directions_pattern, stream)
  for instance in directions:
    stream = stream.replace(instace, '')
  vocabulary_links = re.findall(definitions_pattern, stream)
  for instance in vocabulary_links:
    stream = stream.replace(instance, '')
  return stream

def main():
  stream = ReadFile('text.txt')
  output = ParseInput(stream)
  tree = {}
  for  line in output:
    if tree.has_key(line[0]):
      tree[line[0]].append(line[1])
    else:
      tree[line[0]] = [line[1]]
  metadata = {}
  for character in tree:
    no_of_lines = len(tree[character])
    no_of_questions = 0
    no_of_exclamations = 0
    no_of_words = 0
    for line in tree[character]:
      no_of_questions+=len(re.findall('\?', line))
      no_of_exclamations+=len(re.findall('!', line))
      no_of_words+=len(line.split(' '))
    character_data = {}
    character_data['no_of_lines'] = no_of_lines
    character_data['no_of_questions'] = no_of_questions
    character_data['no_of_exclamations'] = no_of_exclamations
    character_data['no_of_words'] = no_of_words
    metadata[character] = character_data
  max_lines, max_q, max_exc, max_words = 0, 0, 0, 0
  for character in metadata:
    if metadata[character]['no_of_lines'] > max_lines:
      max_lines = metadata[character]['no_of_lines']
      max_lines_character = character
    if metadata[character]['no_of_questions'] > max_q:
      max_q = metadata[character]['no_of_questions']
      max_q_character = character
    if metadata[character]['no_of_exclamations'] > max_exc:
      max_exc = metadata[character]['no_of_exclamations']
      max_exc_character = character
    if metadata[character]['no_of_words'] > max_words:
      max_words = metadata[character]['no_of_words']
      max_words_character = character
  print 'The character with:'
  print 'The most number of lines is ' + max_lines_character
  print 'The most number of words is ' + max_words_character
  print 'The most number of questions is ' + max_q_character
  print 'The most number of exclamations is ' + max_exc_character

if __name__ == '__main__':
  main()
