# Format a string of names like 'Bart, Lisa & Maggie'.

def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]