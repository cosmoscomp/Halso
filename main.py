print("Welcome to Halso. Type 'help'.")
initstash = 'Origin:'
values = {}
initcmd = input(f"{initstash}$$: ")
while True:
  if initcmd == 'help':
    print("Welcome to Halso, key storage.\n")
    print("To create a db: new\n To add values: add\n")
    print("To delete values: del\n To find: find")
    initcmd = input(f"{initstash}$$: ")
  elif initcmd == 'new':
    dbnew = input('Name of DB: ').strip()
    initstash = f'{dbnew}:'
    truebyte = True
    print(f'DB {dbnew} has been made.')
    initcmd = input(f"{initstash}$$: ")
  elif initcmd == 'add':
    if truebyte:
      truebyteask = input("Key To Add: ")
      tbas = input("Value to key: ")
      values[truebyteask] = tbas
      print(f'{tbas} to {truebyteask} as been made.')
      initcmd = input(f"{initstash}$$: ")
    else:
      print("No DB in use.")
      initcmd = input(f"{initstash}$$: ")
  elif initcmd == 'del':
    askdel = input("Key to del: ").strip()
    try:
      values.pop(askdel)
      print(f'Key {askdel} deleted with value {values[askdel]}')
    except:
      print("Not Found.")
      initcmd = input(f"{initstash}$$: ")
  elif initcmd == 'find':
    askfind = input("Key to find: ")
    try:
      print(f"Key {askfind} to {values[askfind]}")
    except:
      print("Not Found")
    initcmd = input(f"{initstash}$$: ")