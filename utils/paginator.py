from rest_framework import pagination
from rest_framework.response import Response


class HeaderPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.page.next_page_number() if self.page.has_next() else '',
                'previous': self.page.previous_page_number() if self.page.has_previous() else ''
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })
