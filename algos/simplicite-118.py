def erase(cc:str):
  cc = list(cc)
  if cc[0] == ' ':
    if cc[1] != ' ':
      cc[0] = ''
  for i in range(1,len(cc)):
    if cc[i] == ' ':
      if cc[i-1] != ' ' or cc[i+1] != ' ':
        cc[i] = ''
  if cc[len(cc)-1] == ' ':
    if cc[len(cc)-2] != ' ':
      cc[len(cc)-1] = ''
  cc = "".join(cc)
  return cc
