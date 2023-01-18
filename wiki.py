import wikipediaapi

wiki = wikipediaapi.Wikipedia(language="es", extract_format=wikipediaapi.ExtractFormat.WIKI)

search = input("Que desea consultar en wikipedia? ")

page_py = wiki.page(search)

if page_py.exists():
    print("Page - Sumary: %s" % page_py.summary[0:500])
else: 
    print("La consulta no existe")
    