from django.shortcuts import render

# Create your views here.
def index(request):
    productos=[
        {"codigo":1,"nombre":"Producto 1","descripcion":"Descripción Producto 1","stock":10,"precio":"$1.000.-"},
        {"codigo":2,"nombre":"Producto 2","descripcion":"Descripción Producto 2","stock":20,"precio":"$2.000.-"},
        {"codigo":3,"nombre":"Producto 3","descripcion":"Descripción Producto 3","stock":30,"precio":"$3.000.-"},
        {"codigo":4,"nombre":"Producto 4","descripcion":"Descripción Producto 4","stock":40,"precio":"$4.000.-"},
    ]
    return render(request, 'inicio/default.html',{"articulos":productos})