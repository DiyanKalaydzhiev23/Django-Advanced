class ReadWriteSerializerMixin:
    SAFE_METHODS = ['GET']

    read_serializer = None
    write_serializer = None

    def get_serializer_class(self):
        if self.request.method in self.SAFE_METHODS:
            return self.read_serializer
        return self.write_serializer
