edit_txt = '<img alt="PinkToyz" src="https://pinktoyz.com/wp-content/uploads/2023/05/PinkToyz-Logo-Website-Header-2.png" style="max-width: 280px;"/>'
#print(edit_txt[:4]+' class="card-img-top"'+edit_txt[4:])


import re

texto = '<img class="card-img-top mt-2" alt="" data-lazy-sizes="(max-width: 305px) 100vw, 305px" data-lazy-src="https://precisionglobal.marketing/wp-content/uploads/2023/05/LOGO-PGM-1-02.webp" data-lazy-srcset="https://precisionglobal.marketing/wp-content/uploads/2023/05/LOGO-PGM-1-02.webp 305w, https://precisionglobal.marketing/wp-content/uploads/2023/05/LOGO-PGM-1-02-300x300.webp 300w, https://precisionglobal.marketing/wp-content/uploads/2023/05/LOGO-PGM-1-02-150x150.webp 150w" decoding="async" height="305" src="data:image/svg+xml,%3Csvg%20xmlns=\'http://www.w3.org/2000/svg\'%20viewBox=\'0%200%20305%20305\'%3E%3C/svg%3E" style="max-width: 100%; height: auto;" width="305">'

# Utiliza una expresión regular para buscar el valor de data-lazy-src
patron = r'data-lazy-src="([^"]+)"'
resultado = re.search(patron, texto)

if resultado:
    valor_data_lazy_src = resultado.group(1)
    print("Valor de data-lazy-src:", valor_data_lazy_src)
else:
    print("No se encontró data-lazy-src en el texto.")
