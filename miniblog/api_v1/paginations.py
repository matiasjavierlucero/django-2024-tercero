from rest_framework import pagination

class MiPaginador(pagination.PageNumberPagination):
    page_size = 20
    page_query_params = 'pagina'
