url_list = [
    "https://data.consejeria.cdmx.gob.mx/index.php/gaceta",
    "https://www.gob.mx/conamer/archivo/documentos",
    "https://datos.gob.mx/busca/dataset",
    "https://www.cfe.mx/Pages/default.aspx",
    "https://www.gob.mx/cre",
    "http://www.ift.org.mx/transparencia/organo-interno-control/marco-normativo",
    "https://www.dof.gob.mx/",
    "https://www.gob.mx/conamer",
    "http://www.diputados.gob.mx/USIEG/Ubicacion.html",
    "https://www.senado.gob.mx/64/",
    "https://www.gob.mx/sct",
]


def get_url_list():
    return url_list


def get_url(index=0):
    return url_list[index] if len(get_url_list()) > index else ""
