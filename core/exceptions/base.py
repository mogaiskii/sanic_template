from sanic import response


class ServiceException(Exception):
    status_code = 500
    error_message = 'something went wrong'

    def get_json_response(self):
        return response.json({'error': self.error_message}, status=self.status_code)
